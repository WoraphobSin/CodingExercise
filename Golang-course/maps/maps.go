package main

import "fmt"

var products = make(map[string]float64)

func main() {
	fmt.Println("Products = ", products)

	//add
	products["Macbook"] = 45000
	fmt.Println("Products = ", products)
	products["iPhone"] = 25000
	products["iPad"] = 32000
	fmt.Println("Products =", products)

	//delete
	delete(products, "iPad")
	fmt.Println("Products =", products)

	//update
	products["iPhone"] = 14500
	fmt.Println("Products =", products)

	value1 := products["iPhone"]
	fmt.Println(value1)

	courseName := map[string]string{"101": "Java", "202": "Python"}
	fmt.Println(courseName)
}
