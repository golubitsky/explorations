package main

import (
	"fmt"
	"math"
)

type operation func(a int, b int) int

func (f operation) square(a int, b int) int {
	return int(math.Pow(float64(f(a, b)), 2))
}

func main() {
	// a weird/contrived example
	// following https://www.willem.dev/articles/http-handler-func/

	var add operation = func(a int, b int) int {
		return a + b
	}

	var multiply operation = func(a int, b int) int {
		return a * b
	}

	a := add.square(3, 4)
	b := multiply.square(3, 4)

	fmt.Println(a, b) // => 49 144
}
