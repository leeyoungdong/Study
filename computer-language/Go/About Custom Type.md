# **사용자 정의 타입**
- **사용자 정의 타입**(custom type)은 Go의 기본 타입 외에 **추가로 타입을 정의**할 때 사용한다.
- 또한 **type**이라는 키워드를 사용하여 **생성**한다.
    ~~~go
    type 타입명 타입명세
    ~~~
- **타입명**은 **패키지**나 **함수** 내에서 **유일**해야 한다.

- **타입명세로**는 **다음 목록**들을 사용할 수 있다.
    - **Go의 기본 타입**(string, int, slice, map, channel 등)
    - **구조체**
    - **인터페이스**
    - **함수 서명**

<br>

---
## **사용자 정의 타입의 종류**
- 주로 **구조체나 인터페이**스를 정의할 때 **사용자 정의 타입**을 사용한다.
- 하지만, **기본 타입**이나 **함수 서명**을 **사용자 정의 타입**으로 지정해서 쓰기도 한다.

<br>

### **1. 기본 타입을 사용자 정의 타입으로 사용**
- 현재 코드 문맥에 맞는 **의미를 부여**하기 위해 **기본 타입**을 **사용자 정의 타입**으로 정의한다.
    ~~~go
    type quantity int
    type dozen []quantity

    var d dozen
    for i:=quantity(1); i<=12; i++ {
        d = append(d, i)
    }
    fmt.Println(d)
    ~~~
    ~~~
    실행 결과

    [1 2 3 4 5 6 7 8 9 10 11 12]
    ~~~

<br>

- **기본 타입**을 **매개변수**로 받는 함수에 **사용자 정의 타입**을 **매개변수**로 전달하려면 **기본 타입으로 변환**해야한다.
- 또한, 반대의 경우에도 **기본 타**입을 **사용자 정의 타입**으로 **변환하여 전달**해야 한다.
    ~~~go
    type quantity int

    func main() {
        var q quantity = 3
        display(int(q))
    }

    func display(i int) {
        fmt.Println(3)  // 3
    }
    ~~~

<br>

### **2. 함수 서명을 사용자 정의 타입으로 사용**
- 마찬가지로 **코드 문맥**에 맞는 의미 부여를 위해 **함수 서명의 사용자 정의 타입의 정의**도 유용하다.

    ~~~go
    type quantity int
    type costCalculator func(quantity, float64) float64

    func describe(q quantity, price float64, c costCalculator) {
        fmt.Printf("quantity: %d, price: %0.0f, cost: %0.0f\n", q, price, c(q, price))
    }

    func main() {
        var offBy10Percent, offBy1000Won costCalculator

        offBy10Percent = func(q quantity, price float64) float64 {
            return float64(q) * price * 0.9
        }

        offBy1000Won = func(q quantity, price float64) float64 {
            return float64(q) * price - 1000
        }

        describe(3, 10000, offBy10Percent)
        describe(3, 10000, offBy1000Won)
    }
    ~~~
    ~~~
    실행 결과

    quantity: 3, price: 10000, cost: 27000
    quantity: 3, price: 10000, cost: 29000
    ~~~
    
<br>

- **costCalculator과 서명이 일치하는 함수**를 만들었고 이를 describe() 함수의 매개변수로 전달했다.

- 기본 서명인 **func(quantity, float64) float64**보다 **costCalculator** 타입의 사용
    - **더 가독성이 높아짐**
    - **의미도 분명하게 전달됨**

<br>

### **3. 구조체**
- 구조체는 **여러 속성**을 묶어서 **하나의 타입**으로 정의할 때 사용한다.
- 예를 들어 rect 타입을 **다음과 같이 표기**할 수 있다.
    ~~~go
    type rect struct {
        width float64
        height float64
    }

    func (r rect) area() float64 {
        return r.width * r.height
    }

    func main() {
        r := rect{3, 4}
        fmt.Println("area:", r.area())
    }
    ~~~

<br>

- **struct** 키워드로 **구조체를 정의**했고, 구조체 내부에 **필드명 필드타입 형태**로 필드를 나열했다.
- 이어서 **area() 메서드**를 정의한 후 main 함수에서 **rect 타입**을 사용했다.

<br>

**구조체에 관한 상세내용은 06-03절에서 다룬다.**

<br>

### **4. 인터페이스**
- **Go의 인터페이스**는 **메서드의 묶음**이다.
- 인터페이스에 정의된 메서드와 서명이 같은 메서드가 정의된 타입은 **인터페이스로 사용할 수 있다.**
    ~~~go
    type shaper interface {
        area() float64
    }

    func describe(s shaper) {
        fmt.Println("area:", s.area())
    }

    func main() {
        r := rect{3, 4}
        describe(r)
    }
    ~~~

<br>

- shaper 인터페이스와 rect 타입 사이에는 **아무런 연결 고리가 없다.**
- 하지만 rect 타입이 shaper 인터페이스에 정의된 메서드와 **형태가 같은 메서드**를 가진 것만으로도 **rect 타입**을 **shaper 인터페이스**로 **사용할 수 있다.**

<br>

**인터페이스에 관한 상세내용은 06-04절에서 다룬다.**