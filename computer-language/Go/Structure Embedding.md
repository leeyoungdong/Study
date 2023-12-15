# **구조체 임베딩**
## **보편적인 코드 재사용**
- 이때까지 보편적으로 **상속**을 통해 코드를 재사용하고, **객체 지향 언어** 대부분은 **상속을 지원**한다.
- 하지만 **상속 관계가 깊어지면** 클래스들이 **거대한 트리 구조**가 되어 **여러 문제**를 유발한다.
- 따라서 **디자인 패턴**에서는 상속보다는 **조합**을 강조한다.

<br>

## **Go에서의 상속? 조합?**
- **상속**은 위의 내용을 포함한 **여러 문제**가 있기 때문에 **Go**에서는 **상속을 없앴다.**
- 따라서 **사용자 정의 타입**을 **조합**하여 **구조체를 정의**하는 방식으로 **객체를 재사용**한다.
- 이처럼 **사용자 정의 타입**을 **구조체 필드**로 지정하는 것을 **임베딩**이라 한다.
    ~~~go
    type 타입명 struct {
        타입1   // 임베디드 필드
        타입2   // 임베디드 필드
        ...
    }

    type 타입1 struct {
        ...
    }

    type 타입2 struct {
        ...
    }
    ~~~

<br>

---
## **임베디드 필드**
- **. 연산자**로 임베디드 필드의 **내부 필드**에 **바로 접근**할 수 있다.
- 하지만 임베디드 필드의 **내부 필드**와 **이름이 같은 필드**가 있을 때는 **임베디드 필드의 타입**도 적어주어야 한다.
    ~~~go
    package main

    import "fmt"

    type Option struct {
        name string
        value string
    }

    type emItem struct {
        name string
        price float64
        quantity int
        Option	// 임베디드 필드
    }

    func main() {
        shoes := emItem{
            name:     "Sports Shoes",
            price:    300000,
            quantity: 2,
            Option:   Option{"color", "red"},
        }

        fmt.Println(shoes)

        // name 필드에 접근
        fmt.Println(shoes.name)

        // 임베디드 필드인 Option 구조체의 내부 필드인 value에 접근
        fmt.Println(shoes.value)


        // 임베디드 필드인 Option 구조체의 내부 필드인 name에 접근
        // Item 구조체에 이름이 같은 필드가 있으므로 Option 타입을 명시
        fmt.Println(shoes.Option.name)
    }
    ~~~
    ~~~
    실행 결과

    {Sports Shoes 300000 2 {color red}}
    Sports Shoes
    red
    color
    ~~~

<br>

**위의 코드에 대한 구조체 임베딩**
![Alt text](image.png)
<br>

## **메서드 재사용**
- **구조체 임베딩** 시 **임베디드 필드가 포함된 구조체**에서 **임베디드 필드에 정의된 메서드**를 **사용**할 수 있다. 

- **다음 코드**를 보면 확실히 이해 될 것이다.
    1. **emItem** 구조체에 **Cost() 메서드**를 정의한다.
    2. **emItem**을 **DiscountItem**의 **임베디드 필드**로 확장한다.
    3. **main 함수**에서 **DiscountItem** 타입인 **eventShoes**를 선언한다.
    4. 마지막으로 **DiscountItem**에서 **Item 타입**에 정의된 **Cost() 메서드**를 호출한다.

    ~~~go
    package main

    import "fmt"

    type emItem struct {
        name string
        price float64
        quantity int
    }

    func (t emItem) Cost() float64 {
        return t.price * float64(t.quantity)
    }

    type DiscountItem struct {
        emItem
        discountRate float64
    }

    func main() {
        shoes := emItem{"Women's Walking Shoes", 30000, 2}

        eventShoes := DiscountItem{emItem{"Sport Shoes", 50000, 3},10.00}

        fmt.Println(shoes.Cost())       // 60000
        fmt.Println(eventShoes.Cost())  // 150000
    }
    ~~~

<br>

---
## **메서드 오버라이딩**(Overriding)
- **임베디드 필드**에 정의된 **메서드**를 **오버라이딩**(Overriding) 할 수도 있다.
    ~~~go
    func (t DiscountItem) Cost() float64 {
        return t.emItem.Cost() * (1.0-t.discountRate/100)
    }
    func main() {
        shoes := emItem{"Women's Walking Shoes", 30000, 2}

        eventShoes := DiscountItem{emItem{"Sport Shoes", 50000, 3},10.00}

        fmt.Println(shoes.Cost())               // 60000
        fmt.Println(eventShoes.Cost())          // 135000
        fmt.Println(eventShoes.emItem.Cost())   // 150000
    }
    ~~~
- **emItem** 타입에 정의된 **Cost() 메서드**와 이름이 같은 메서드를 **DiscountItem** 타입에 추가했다.
- 이로써 **Item**의 **Cost() 메서드**는 **오버라이**딩 되었다.

<br>

---
## **오버로딩**(Overloading)
- Go는 이름이 같은 메서드를 생성할 수 없으므로 **오버로딩을 지원하지 않는다.**
- 따라서 매개변수가 다르더라도 **메서드 이름**을 **다르게** 지정해야 한다.
- 예를 들어, 기본 라이브러리에 있는 **string.Reader** 타입은 **매개변수**에 따라 **다른 메서드** 세 개를 제공한다. 
    ~~~go
    func (r *Reader) Read(b []byte) (n int, e error)
    func (r *Reader) ReadByte(b byte) (b byte, e error)
    func (r *Reader) ReadRune(ch rune) (ch rune, size int, e error)
    ~~~