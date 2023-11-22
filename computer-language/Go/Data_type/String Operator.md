# **문자열 연산**
## **부분 문자열 추출**
- **[] 연산자**로 문자열의 일부를 **추출**할 수 있다.

- 다음은 **문자열 추출**의 여러가지 방법이다.
    - **s[n:m]** -> 문자열의 s의 n번째 바이트부터 m-1번쨰 바이트까지 추출
    - **s[n:]**  -> 문자열 s의 n번째 바이트부터 마지막 바이트까지 추출
    - **s[:m]**  -> 문자열 s의 처음부터 m-1 바이트까지 추출

- 문자열은 **UTF-8 인코딩**을 사용하므로 **문자에 따라 바이트 수가 달라질 수 있다.**
~~~go
func main() {
	s1 := "hello"
	fmt.Println(s1[1:2])	// e
	fmt.Println(s1[1:])		// ello
	fmt.Println(s1[:2])		// he

	s2 := "안녕하세요"
	fmt.Println(s2[1:2])	// ?
	fmt.Println(s2[1:])		// ??녕하세요
	fmt.Println(s2[:2])		// ?
}
~~~

<br>

---
## **문자열 비교**
- 문자열 두 개에 **비교 연산자**(==, !=, < <=, >=, >)를 사용하면 **문자열**을 **바이트 단위**로 비교한다.
~~~go
fmt.Println(s1==s2) // false
fmt.Println(s1!=s2) // true
fmt.Println(s1>s2)  // false
fmt.Println(s1<s2)  // true
~~~

<br>

---
## **문자열 조합**
- **\+ 연산자나 += 연산자**를 사용하여 여러 문자열을 하나로 **합칠 수 있다.**
~~~go
text := "My name is"
text += "jinhong"
fmt.Println(text)
~~~
~~~
실행 결과

My name is jinhong
~~~

<br>

- **문자열**은 한번 생성되면 **그 값을 변경할 수 없으므로** 조합할 때마다 항상 **새로운 문자열**을 생성한다.
- 그래서 문자열을 **+로** 조합하는 것은 **호율적이지 않다.**
- 따라서 **strings.Join()** 함수를 사용하거나 **bytes.Buffer** 타입을 사용하면 더 효율적이다.

<br>

### 다양한 **문자열 조합** 예시

- **\+ 연산자 이용**
    ~~~go
    package main

    import (
        "fmt"
        "math"
        "unicode"
    )

    func main() {
        var str string
        for i:=0; i<=math.MaxUint8; i++ {
            if s, ok := nextString(i); ok {
                str += s
            }
        }
        fmt.Print(str, "\n")
    }

    func nextString(i int) (s string, ok bool) {
        // 해당 rune 타입의 데이터가 문자인지 검사해주는 함수
        if unicode.IsLetter(rune(i)) {
            return string(i), true
        }
        return "", false
    }
    ~~~

- **strings.Join()** 함수 이용
    ~~~go
    package main

    import (
        "fmt"
        "math"
        "strings"
        "unicode"
    )

    func main() {
        strArr := []string{}
        for i:=0; i<=math.MaxUint8; i++ {
            if s, ok := nextString(i); ok {
                strArr = append(strArr, s)
            }
        }
        fmt.Println(strings.Join(strArr, ""))
    }

    func nextString(i int) (s string, ok bool) {
        // 해당 rune 타입의 데이터가 문자인지 검사해주는 함수
        if unicode.IsLetter(rune(i)) {
            return string(i), true
        }
        return "", false
    }
    ~~~
- **bytesBuffer 타입** 사용
    ~~~go
    package main

    import (
        "bytes"
        "fmt"
        "math"
        "unicode"
    )

    func main() {
        var buffer bytes.Buffer
        for i:=0; i<=math.MaxUint8; i++ {
            if s, ok := nextString(i); ok {
                buffer.WriteString(s)
            }
        }
        fmt.Print(buffer.String(), "\n")
    }

    func nextString(i int) (s string, ok bool) {
        // 해당 rune 타입의 데이터가 문자인지 검사해주는 함수
        if unicode.IsLetter(rune(i)) {
            return string(i), true
        }
        return "", false
    }
    ~~~

    ~~~
    실행 결과

    ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzªµºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ
    ~~~