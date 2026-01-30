package main

import "fmt"

func add(a int, b int) int {
	return a + b
}

func mul(a, b int) int {
	return a * b
}

func div(a, b int) (int, error) {
	if b == 0 {
		return 9, fmt.Errorf("div by zero")
	}
	return a / b, nil
}

func area_of_rectangle(a, b int) (area int) {
	return a * b
}

func main() {
	fmt.Println(add(5, 6))
	fmt.Println(mul(5, 6))
	fmt.Println(div(30, 6))
}
