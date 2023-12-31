# **매개변수 전달 방식**
> Go는 **값에 의한 호출**(call by value)이 기본이다.

<br>

---
## 값에 의한 호출(call by value)
- 값에 의한 호출은 함수를 호출할 때 **매개변수 값을 복사**해서 함수 내부로 전달한다.
- 함수 내부에서는 전달된 **매개변수의 본래 값**을 **변경할 수 없다.**
- 함수 내부에 본래 값을 **변경하기 위해서**는 **& 연산자**로 변수의 **메모리 주소**를 전달해야 한다.

~~~go
package main

import "fmt"

// inc 함수 내부에서 다루는 i는 main에서 첫 줄에 선언한 i가 아니기 때문에 적용이 되지 않음
func inc(i int) {
    i = i + 1
}

func main() {
    i := 10
    inc(i)
    fmt.Println(i)
}
~~~
~~~
실행 결과

10
~~~

<br>

---
## **참조에 의한 호출**(call by reference)
- 참조에 의한 호출은 매개변수로 **매개변수의 메모리 주소**를 받는다.
- 함수의 **매개변수 타입**을 **포인터**로 지정하면 변수의 값이 아닌 **변수의 메모리 주소**가 전달된다.
- 이렇게 포인터로 메모리 주소에 접근하면 매개변수로 전달된 인수의 **본래 값을 변경할 수 있다.**
~~~go
package main

import "fmt"

func inc(i *int) {
    *i = *i + 1
}

func main() {
    i := 10
    inc(i)
    fmt.Println(i)
}
~~~
~~~
실행 결과

11
~~~