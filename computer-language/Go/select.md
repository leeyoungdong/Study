# **select**
- **select**  문은 **하나의 고루틴**이 **여러 채널**과 통신할 때 사용한다.
- **case**로 **여러 채널을 대기**시키고 있다가 **실행 기능 상태**가 된 **채널**이 있으면 **해당 케이스를 수행**한다.
    ~~~go
    package main

    import (
        "fmt"
        "time"
    )

    func fibonacci(c, quit chan int) {
        x, y := 0, 1
        // 무한 반복문
        for {
            select {
            // 만약 어딘가에서 채널 c의 수신을 받을 준비가 되었다면, 다음 실행문 수행
            case c<-x:
                x, y = y, x+y
            // 만약 채널 quit가 값을 수신 받았다면, 다음 실행문 수행
            case <-quit:
                fmt.Println("quit")
                return
            }
        }
    }

    func main() {
        c := make(chan int)
        quit := make(chan int)
        // 고루틴에서 채널 c로부터 수신받을 값의 송신을 요청함.
        go func() {
            for i:=0; i<10; i++ {
                fmt.Println(<-c)
            }
            quit<-1
        }()
        fibonacci(c, quit)
    }
    ~~~
    ~~~
    실행 결과

    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    quit
    ~~~

<br>

- **select** 문에서 **default** 케이스를 지정하면 **case**에 지정된 **모든 채널**이 **사용 불가능** 상태일 때 **default** 케이스를 **수행**한다.
    ~~~go
    c1 := make(chan int)
    c2 := make(chan int)

    /*...*/

    select {
    case <-c1:
        // c1 채널에 값이 전달됐을 때 수행
    case <-c1:
        // c1 채널에 값이 전달됐을 때 수행
    default:
        // 케이스에 대기하고 있는 채널에 값이 전달되지 않았을 때 수행
    }
    ~~~

    <br>

- **defualt** 케이스는 사용 가능 상태가 **아닐** 경우, **대기하지 않고** 무언가를 **처리**해야 할때 사용한다.
    ~~~go
    func main() {
        tick := time.Tick(100 * time.Millisecond)
        boom := time.After(500 * time.Millisecond)
        for {
            select {
            case <-tick:
                fmt.Println("tick.")
            case <-boom:
                fmt.Println("BOOM!")
            default:
                fmt.Println(".")
                time.Sleep(50 * time.Millisecond)
            }
        }
    }
    ~~~
    