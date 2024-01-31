# **맵리듀스**
## **맵리듀스란?**
- 맵리듀스는 **대용량 데이터**를 **분산**하여 **빠르게 처리**하려고 사용하는 **프로그래밍 모델**이다.
- 구글이 **분산 데이터 처리**에 관한 논문을 발표한 이후 **맵리듀스**가 관심을 받기 시작하였다.
- 이번 절에는 파일 목록 중에서 각 토큰이 파일별로 몇 번 사용됐는지 세는 프로그램을 **맵리듀스 패턴**으로 작성해 본다.

<br>

---
## **맵리듀스 패턴**
- 맵리듀스는 **두 가지 단계**로 나뉜다.
    - 흩어져 있는 데이터 조각을 종류별로 모으는 **맵(map) 단계**
    - 모인 데이터를 모두 취합하여 원하는 형태의 최종 데이터를 추출하는 **리듀스(reduce) 단계**

- 따라서 우리의 프로젝트에 이렇게 **적용**할 수 있다.
    - **맵 단계** -> 파일 목록을 전달받아 각 파일의 토큰 정보를 **수집**한다.
    - **리듀스 단계** -> 수집된 토큰 정보를 바탕으로 최종 요약 정보를 **생성**한다.

    **맵리듀스의 전체적인 흐름(패턴)**
    ![Alt text](image-5.png)

<br>

---
## **맵 단계**
- **각 토큰의 위치 정보**를 나타내는 **partial** 타입을 다음과 같이 정의한다
    ~~~go
    import (
        "text/scanner"
    )

    type partial struct {
        token string
        scanner.Position
    }
    ~~~

<br>

- **text/scanner** 패키지가 제공하는 타입인 **scanner.Position**은 **토큰의 위치 정보**를 담고 있다.
    ~~~go
    type Position struct {
        Filename string // 파일명
        Offset   int    // 오프셋 (byte 단위, 0부터 시작)
        Line     int    // 줄 번호 (1부터 시작)
        Column   int    // 칼럼 변호 (1부터 시작)
    }
    ~~~

<br>

- mapper() 함수는 각 파일의 **토큰**과 토큰의 위치 정보를 **추출**하여 **out 채널**로 전달한다.
    ~~~go
    func mapper(path string, out chan <- partial) {
        file, err := os.Open(path)
        if err != nil {
            return
        }
        defer file.Close()

        // 정상적인 파일이 아닐 경우 바로 반환
        if info, err := file.Stat(); err != nil || info.Mode().IsDir() {
            return
        }

        var s scanner.Scanner
        s.Filename = path
        s.Init(file)

        // 파일의 모든 토큰을 스캔하여 out 채널로 전송
        tok := s.Scan()
        for tok != scanner.EOF {
            fmt.Println(s.Pos())
            out <- partial{s.TokenText(), s.Pos()}
            tok = s.Scan()
        }
    }
    ~~~

<br>

- 다음은 **매퍼**(mapper)를 실행하는 함수이다.
    ~~~go
    func runMap(paths <- chan string) <- chan partial {
        out := make(chan partial)
        go func() {
            for path := range paths {
                mapper(path, out)
            }
            close(out)
        }()
        return out
    }
    ~~~

<br>

- 파일 목록은 **paths 채널**을 통해서 **runMap()** 함수 내부로 **전달**한다.
- 각 **path**에 **mapper()를 실행**하는 작업은 **고루틴**으로 동작한다.
- **mapper()** 함수로 추출된 토큰 정보는 **out 채널**을 통해 **외부로 전달**한다.

<br>

---
## **토큰 정보 취합**
- 맵 단계에서 **추출된 토큰 정보**는 토큰 단위로 그루핑되어 **리듀서**(reduce)로 **전달**된다.
- 토큰 단위로 그루핑된 정보는 **map[string][]scanner.Position** 타입으로 만들어진다.
- **가독성**을 위해 map[string][]scanner.Position을 **커스텀 타입**으로 지정한다.
    ~~~go
    // 키: token
    // 값: token positions
    type intermediate map[string][]scanner.Position
    ~~~

<br>

- **intermediate**에 partical 정보를 **추가**하는 기능은 **addPartial() 메서드**로 작성한다.
    ~~~go
    func (m intermediate) addPartial(p partial) {
        positions, ok := m[p.token]
        if !ok {
            positions = make([]scanner.Position, 1)
        }
        positions = append(positions, p.Position)
        m[p.token] = positions
    }
    ~~~

<br>

- **intermediate**에 partical 정보가 **새로 추가되**면 토큰을 키로 하여 위치 정보를 **추가**한다.
- 마지막으로 **collect()** 함수를 통해 **맵 단계**에서 추출되는 정보를 **취합**한다.
    ~~~go
    func collect (in <- chan partial) intermediate {
        tokenPosition := make(intermediate, 10)
        for t:= range in {
            tokenPosition.addPartial(t)
        }

        return tokenPosition
    }
    ~~~

<br>

---
## **리듀스 단계**
- **reducer()** 함수에서는 **토큰과 토큰의 위치 정보**를 매개변수로 받아 파일별로 **토큰이 사용된 횟수**를 세서 **반환**한다.
    ~~~go
        func reducer(token string, positions []scanner.Position) map[string]int {
        result := make(map[string]int)
        for _, p := range positions {
            result[p.Filename] += 1
        }
        return result
    }
    ~~~

<br>

- 반환 값은 **map[string]int 타입**으로 전달되는데, **파일 이름**이 **키**가 되고 **토큰이 사용된 횟수**는 **값**이 된다.
- **최종 계산 결과** 타입(각 토큰이 파일별로 사용된 회수)인 **summary 구조체**를 정의해 보자.
- **리듀스** 단계를 **여러 고루틴**에서 **병행**으로 처리하는 경우 **뮤텍스 mu 필드**를 지정해줘야 한다.
    ~~~go
    type summary struct {
        // 키 : token
        // 값 : map[string]int
        //		키 : file path
        //		값 : token count
        m map[string]map[string]int

        // 공유 데이터 m을 보호하기 위한 뮤텍스
        mu sync.Mutex
    }
    ~~~

<br>

- 다음 **runRecue()** 함수는 **리듀서**를 실행시킨다.
    ~~~go
    func runReduce(tokenPositions intermediate) summary {
        s := summary{m:make(map[string]map[string]int)}
        for token, positions := range tokenPositions {
            s.mu.Lock()
            s.m[token] = reducer(token, positions)
            s.mu.Unlock()
        }
        return s
    }
    ~~~

<br>

---
## **메인 함수**
1. **runMap()** 의 반환 값인 **<-chan partial**을 **collect()** 함수에 전달한다.
2. **colloct()**의 결과(각각의 파일과 그에 대한 토큰을 하나로 뭉친 구조체)를 **runRedude()** 함수에 전달한다.
3. **runReduce()** 함수를 통해 **최종 계산 결과**인 구조체가 반환된다
~~~go
func main() {
	// 병행 처리를 이용항 파이프라인 구현시 사용할 함수들 (곧 추가할 예정)
	paths := find(parseArge()) // 커맨드 명령으로 받은 PATH 디렉터이 안에 있는 모든 파일을 검색해서 out 채널로 전송한다.
	fmt.Println(runReduce(collect(runMap(paths))))
}
~~~