# **다형성**
## **다형성이란?**
- **다양한 타입의 객체**가 **같은 메세지**를 통해 **다양한 방식으로 동작**하게 하는 것을 말한다.
- 다른 언어에서는 **서브타이핑**이나 **메서드 오버로딩** 등으로 다형성을 지원한다.
- 하지만 **Go**에는 그런 것들이 없기 때문에 Go는 **인터페이스**로 다형성을 지원한다.

<br>

**다시 말해 인터페이스 사용으로 타입이나 메서드의 구현방식과 관계없이 다양한 값을 같은 형태로 다룰 수 있다.**

<br>

---
## **인터페이스를 통한 다향성**
- **아래 그림**을 토대로 **하나의 인터페이스**로 서로 다른 **구조체 세 개**를 같은 방식으로 처리해보자.

    ![Alt text](image-1.png)

<br>

- 먼저 **Cost() float64 메서드 서명**을 가진 **Coster 인터페이스**를 만듦.
- Coster 인터페이스를 **매개변수**로 받아 Cost()를 출력해주는 **displayCost() 함수** 만듦.
    ~~~go
    type Coster interface {
        Cost() float64
    }

    func displayCost(c Coster) {
        fmt.Println("cost:", c.Cost())
    }
    ~~~

<br>

- **Item**과 **DiscountItem** 타입을 정의하고 각 타입에 **Cost() float64 메서드**를 정의한다.
    ~~~go
    type Item struct {
        name string
        price float64
        quantity int
    }

    func (t Item) Cost() float64 {
        return t.price * float64(t.quantity)
    }

    type DiscountItem struct {
        Item
        discountRate float64
    }

    // 메서드 오버라이딩
    func (t DiscountItem) Cost() float64 {
        return t.Item.Cost() * (1.0 - t.discountRate/100)
    }
    ~~~

<br>

- **Item**과 **DiscountItem** 타입은 **Cost() float64 메서드**를 가지므로 **Coster 인터페이스**로 사용할 수 있다.
- 두 구조체 둘 다 **displayCost() 함수**를 통해 **Cost()를 출력** 한다.
    ~~~go
    func main() {
        shoes := Item{"Sports Shoes", 30000, 2}
        eventShoes := DiscountItem{shoes, 10.00}

        displayCost(shoes)      // 60000
        displayCost(eventShoes) // 54000
    }
    ~~~

<br>

- 이제 **Rental 타입**을 새로 추가하고 Rental 타입에도 **Cost() 메서드**를 정의해보자.
    ~~~go
    type Rental struct {
        name string
        feePerday float64
        periodLength int
        RentalPeriod
    }

    type RentalPeriod int

    const (
        Days RentlaReriod = iota
        Weeks
        Months
    )

    func (p RentalPeriod) ToDays() int {
        switch p {
            case Weeks:
                return 7
            case Months:
                return 30
            default:
                return 1
        }
    }

    func (r Rental) Cost() float64 {
        return r.feePerday * float64(r.ToDays() * r.periodLength)
    }
    ~~~

<br>

- main 함수에서 **Item**과 **Rental** 타입 값을 생성한다.
- 마찬가지로 생성한 값을 **displayCost() 함수**에 전달하여 **Cost()를 출력**한다.
    ~~~go
    func main() {
        shoes := Item{"Sports Shoes", 30000, 2}
        videos := Rental{"Interstellar", 1000, 3, Days}

        fmt.Println(displayCost(shoes))     // cost: 60000
        fmt.Println(displayCost(videos))    // cost: 3000
    }
    ~~~

<br>

---
## **제네릭 컬렉션**
- **05장**에서 말했듯이, **Go**에서는 배열, 슬라이스, 맵에 **정해진 타입 값**만 담을수 있다.
- 하지만 타입을 **인터페이스**로 지정하면 인터페이스를 **충족하는 타입** 값은 어떤 값이라도 **담을 수 있다.**


<br>

### **ex) Items 타입을 Coster 인터페이스의 슬라이스로 정의해보자.**
~~~go
type Items []Coaster
~~~
- 이렇게 정의하면 **Coaster 인터페이스**로 사용할 수 있는 타입은 **모두** 담을 수 있다.
- 또한 **Items**에도 **Cost() 메소드**를 추가하면 Items를 **Coaster 인터페이스**로 사용할 수 있다.
    ~~~go
    func (ts Items) Cost() (s float64) {
        fot _, t := range ts {
            s += t.Cost()
        }
        return
    }
    ~~~

<br>

- 이제 **Item, DiscountItem, Rental** 모두 **Items 슬라이스** 하나에 담을 수 있게 되었다.
- 또한 모두 **Cost() 메서드**를 가지고 있으므로 **Coster 인터페이스**로 사용할 수 있다.
    ~~~go
    func main() {
        shoes := Item{"Sports Shoes", 30000, 2}
        eventShoes := DiscountItem{shoes, 10.00}
        videos := Rental{"Interstellar", 1000, 3, Days}
        
        items := Items[shoes, eventShoes, videos]

        display(shoes)          // cost: 60000
        display(eventShoes)     // cost: 54000
        display(videos)         // cost: 3000
        display(items)          // cost: 117000
    }
    ~~~