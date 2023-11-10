# **defer**

- **defer 키워드**는 함수가 **종료되기 전까지** 특정 구문의 실행을 **지연**시켰다가, 
- 함수가 **종료되기 직전**에 지연시켰던 구문을 **실행**시킨다.
- 주로 **리소스를 해제**시키거나 **클렌징 작업**이 필요할 때 사용한다.

<br>

**defer 사용 예제**
~~~go
package main

import "fmt"

func main() {
	f1()
}
func f1() {
    fmt.Println("f1-start!")
    defer f2()
    fmt.Println("f1-end!")
}
func f2() {
    fmt.Println("f2-deferred!")
}
~~~
~~~
실행 결과

f1-start!
f1-end!
f2-deferred!
~~~

<br>

- 함수 하나에 **defer** 키워드를 **여러 개** 사용하면,
- defer로 지정한 각 구문은 **스택**(stack)에 쌓였다가 **가장 나중에 쌓인 defer** 구문부터 실행된다.

~~~go
package main

import "fmt"

func f() {
    for i:=0; i<5; i++ {
        defer fmt.Printf("%d", i)
    }
}

func main() {
    f()
}
~~~
~~~
실행 결과

4 3 2 1 0
~~~

<br>

## **다음은 실제 Go 프로그램을 작성할 때 defer을 사용하는 예이다.**
- **파일 스트림 닫기**
    ~~~go
    file,_ := os.Open(path)
    defer file.Close()
    ~~~

- **리소스 잠금 해제하기**
    ~~~go
    mu.Lock()
    defer mu.Unlock()
    ~~~

- **레포터에서 푸터 출력하기**
    ~~~go
    printHeader()
    defer printFooter()
    ~~~

- **데이터베이스 커넥션 닫기**
    ~~~go
    con,_ := Connection()
    defer con.Close()
    ~~~

<br>

**defer 사용 예제**
~~~go
package main

import "fmt"

func enter(s string) { fmt.Println("entering: ", s) }
func leave(s string) { fmt.Println("leaving: ", s) }

func a() {
	enter("a")
	defer leave("a")
	fmt.Println("in a")
}

func b() {
	enter("b")
	defer leave("b")
	fmt.Println("in b")
	a()
}

func main() {
	b()
}
~~~
~~~
실행 결과

entering:  b
in b
entering:  a
in a
leaving:  a
leaving:  b
~~~