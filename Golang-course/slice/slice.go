package main

import "fmt"

func main() {
	var courseName []string
	courseName = []string{"Java", "Python"}
	fmt.Println(courseName)
	courseName = append(courseName, "C", "C#", "HTML", "CSS")
	fmt.Println(courseName)
	courseWeb := courseName[3:6]
	fmt.Println(courseWeb)
	courseWeb = courseName[:4]
	fmt.Println(courseWeb)
}
