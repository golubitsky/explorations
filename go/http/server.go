package main

import (
	"fmt"
	"net/http"
)

func handlerFunc(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(200)
	fmt.Fprint(w, "{\"hello\":\"world\"}")
}
func main() {
	http.HandleFunc("/", handlerFunc)
	fmt.Println("Starting server on :3000")
	http.ListenAndServe(":3000", nil)
}
