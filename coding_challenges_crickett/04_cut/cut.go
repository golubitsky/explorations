package main

import (
	"fmt"
	"os"
)

func main() {
	args := os.Args
	option := args[1]
	file_name := args[2]
	fmt.Println(option, "asdf", file_name)
}
