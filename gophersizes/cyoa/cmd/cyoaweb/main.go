package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"

	"cyoa"
)

func main() {
	filename := flag.String("filename", "gopher.json", "filename of JSON file with CYOA story")
	flag.Parse()

	f, err := os.ReadFile(*filename)

	if err != nil {
		log.Fatal("can't open file", *filename, err)
	}

	story := make(cyoa.Story)

	decodeErr := json.Unmarshal(f, &story)

	if decodeErr != nil {
		log.Fatal("can't decode JSON", decodeErr)
	}

	fmt.Printf("%+v\n", story)
}
