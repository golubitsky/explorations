package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"

	"urlshort"
)

func main() {
	yamlFile := flag.String("yaml", "", "YAML filename with list of redirects")
	jsonFile := flag.String("json", "", "JSON filename with list of redirects")
	flag.Parse()

	mux := defaultMux()

	// Build the MapHandler using the mux as the fallback
	pathsToUrls := map[string]string{
		"/urlshort-godoc": "https://godoc.org/github.com/gophercises/urlshort",
		"/yaml-godoc":     "https://godoc.org/gopkg.in/yaml.v2",
	}
	mapHandler := urlshort.MapHandler(pathsToUrls, mux)

	// Build the YAMLHandler using the mapHandler as the
	// fallback
	yamlString := `
- path: /urlshort
  url: https://github.com/gophercises/urlshort
- path: /urlshort-final
  url: https://github.com/gophercises/urlshort/tree/solution
`
	yaml := []byte(yamlString)

	if *yamlFile != "" {
		fromFile, err := os.ReadFile(*yamlFile)
		if err != nil {
			log.Fatal("cannot open ", *yamlFile)
		}
		yaml = fromFile
	}

	yamlHandler, err := urlshort.YAMLHandler(yaml, mapHandler)
	if err != nil {
		panic(err)
	}

	var handler = yamlHandler

	if *jsonFile != "" {
		json, err := os.ReadFile(*jsonFile)
		if err != nil {
			log.Fatal("cannot open ", *jsonFile)
		}

		jsonHandler, err := urlshort.JSONHandler(json, yamlHandler)

		if err != nil {
			log.Fatal("cannot create JSON handler", err)
		}

		handler = jsonHandler
	}

	fmt.Println("Starting the server on :8080")
	http.ListenAndServe(":8080", handler)
}

func defaultMux() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("/", hello)
	return mux
}

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Hello, world!")
}
