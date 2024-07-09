package main

import "fmt"

func zeroValue(ivalue int) {
	ivalue = 0
}

func zeroPointer(ipointer *int) {
	//Input has to be an address
	//Pointer use to store address of data
	*ipointer = 0
}

func main() {
	i := 1
	fmt.Printf("i = %d\nAddress of i = %d\n", i, &i)
	zeroValue(i)
	fmt.Printf("i from zeroValue = %d\nAddress of i from zeroValue = %d\n", i, &i)
	zeroPointer(&i)
	fmt.Printf("i from zeroPointer = %d\nAddress of i from zeroPointer = %d\n", i, &i)
}
