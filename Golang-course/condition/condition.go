package main

import "fmt"

func main() {
	// myMoney := 100
	// if myMoney > 100 {
	// 	fmt.Println("You can buy this things")
	// } else {
	// 	fmt.Println("Not enough money")
	// }
	var score int
	fmt.Println("Grade Calculator")
	fmt.Scanf("%d", &score)
	fmt.Println("Score = ", score)
	if score >= 80 {
		fmt.Println("You got A grade.")
	} else if score >= 70 {
		fmt.Println("You got B grade.")
	} else if score >= 60 {
		fmt.Println("You got C grade.")
	} else if score >= 50 {
		fmt.Println("You got D grade.")
	} else {
		fmt.Println("You got F grade.")
	}
}
