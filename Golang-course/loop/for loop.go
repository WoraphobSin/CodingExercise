package main

import "fmt"

func main() {
	// i := 0
	// for i < 10 {
	// 	fmt.Println("i = ", i)
	// 	i++
	// }
	// count := 15
	// for j := 0; j < count; j++ {
	// 	fmt.Println("j = ", j)
	// }
	var Input string
	for {
		fmt.Scanf("%s", &Input)
		fmt.Println("input = ", Input)
		if Input == "exit" {
			break
		}
	}
}
