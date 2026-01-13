package main

import "fmt"

func main() {
	// for i := 0; i < 5; i++ {
	// 	fmt.Println(i)
	// }

	// i := 0
	// for i < 3 {
	// 	fmt.Println("Hello World!!")
	// 	i += 1
	// }

	// tempArray := []string{"arin", "dhimar", "is", "working", "as", "an", "intern"}
	// fmt.Println(tempArray)

	// for i, j := range tempArray {
	// 	fmt.Println(i, j)
	// }

	// for i, j := range "XabCd" {
	// 	fmt.Println(j, i)
	// }

	mmap := map[int]string{
		22: "Arin",
		33: "Ashish",
		44: "alvf",
	}

	for i, j := range mmap {
		fmt.Println(i, j)
	}

}
