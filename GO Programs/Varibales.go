package main

import "fmt"

func main(){
    var int1 int16 =200;
    fmt.Println(int1);

    var int2 int16 =100;
    fmt.Println(int2);

    var y float32 = 2.25;

    fmt.Println(y);
    var a complex128 = complex(6, 2)

    fmt.Println(a)

    fmt.Println(real(a))
    fmt.Println(imag(a))

    bool1:= int1 == int2

    fmt.Println(bool1)

    str:="Arin Dhimar"

}