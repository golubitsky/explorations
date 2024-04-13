package main

import (
	"cyoa"
	"flag"
	"fmt"
	"log"
	"os"
)

func main() {
	filename := flag.String("filename", "gopher.json", "filename of JSON file with CYOA story")
	flag.Parse()

	f, err := os.Open(*filename)

	if err != nil {
		log.Fatal("can't open file", *filename, err)
	}

	story, err := cyoa.StoryFromJson(f)

	fmt.Printf("%+v\n", story)
}
