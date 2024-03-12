package main

import (
	"flag"
	"fmt"
)

func main() {
	filename := flag.String("filename", "gopher.json", "filename of JSON file with CYOA story")
	flag.Parse()

	fmt.Println(*filename)
}
