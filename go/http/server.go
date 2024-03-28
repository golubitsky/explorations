package main

import (
	"fmt"
	"net/http"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(200)
	fmt.Fprint(w, "{\"hello\":\"world\"}")
}

func contactHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprint(w, "<h1>Contact Page</h1>")

}

func main() {
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/contact", contactHandler)
	fmt.Println("Starting server on :3000")
	http.ListenAndServe(":3000", nil)
}
