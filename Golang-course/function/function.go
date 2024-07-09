package main

import "fmt"

func hello() {
	fmt.Println("Hello")
}

func sum(value1 int, value2 int) int {
	//var result int
	// result := value1 + value2
	// fmt.Println("Result =", result)
	return value1 + value2
}

func plus3value(value1, value2, value3 int) int {
	return value1 + value2 + value3
}

func main() {
	result := sum(600, 1)
	hello()
	fmt.Println("result =", result)
	result2 := plus3value(12, 12, 12)
	fmt.Println("result =", result2)
}
