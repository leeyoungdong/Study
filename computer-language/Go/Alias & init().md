# **별칭(alias)과 init() 함수**

## **별칭 (alias)**
- **Go**에서는 패키지 이름에 **별칭**(alias)을 줄 수 있다.
- 주로 패키지 이름이 **길거나 중복되는 패키지**가 있을 때 **별칭**을 사용한다.
- 다음 코드는 전 회에서 만들었던 **lib 패키지**를 **별칭**을 사용하여 **임포트**한 코드이다.

~~~go
package main

import (
	"fmt"
	mylib "package_practice/lib"
)

func main() {
	fmt.Println(mylib.IsDigit('1'))
	fmt.Println(mylib.IsDigit('a'))
}
~~~

<br>

- 또한 Go에서는 임포트한 **패키지를 사용하지 않으면 컴파일 에러**가 난다.
- 하지만 패키지 이름에 **빈 식별자**(_)로 **별칭**을 주면 컴파일 에러가 **발생하지 않는다.**
- 이 기능을 **디버깅**을 할 떄 **유용**하게 쓰인다.

~~~go
package main

import (
	"fmt"
	_ "package_practice/lib"
)

func main() {
	fmt.Println("lib 패키지 사용 잠시 제거")

	//fmt.Println(mylib.IsDigit('1'))
	//fmt.Println(mylib.IsDigit('a'))
}
~~~

<br>

---
## **init() 함수** 
- **init() 함수**는 패키지가 로드될 때 **가장 먼저 호출되는 함수**로,
- 패키지의 **초기화 로직**이 필요할 때 선택적으로 사용하면 된다.

ex)
~~~go
package main

import (
    "fmt"
    "package_practice/lib"
)

var v rune

func init() {
    v = '1'
}

func main() {
    fmt.Println(lib.IsDigit(v))
}
~~~

~~~
실행 결과

true
~~~

<br>

---
## **init() 함수 실행 순서**
- Go 프로그램은 항상 **main() 함수로 시작**된다.
- 하지만 main 패키지가 다른 패키지를 임포트 하고 있으면 **임포트된 패키지를 먼저 불러온다.**
- 또한 임포트된 패키지가 다른 패키지를 임포트 하고 있으면 **관련된 패키지를 먼저 불러온다.**
- 따라서 임포트된 패키지를 **모두 불러온 후 main() 함수가 실행된다.**
---

<br>

**init() 함수 호출 순서**
![Alt text](image/image3.png)

### **따라서 위의 사진의 프로세스 순서는 다음과 같다.**
1. pkg3의 **init()** 함수
2. pkg2의 **init()** 함수
3. pkg1의 **init()** 함수
4. main의 **init()** 함수
5. **main()** 함수