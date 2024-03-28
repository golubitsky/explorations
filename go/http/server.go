package main

import (
	"fmt"
	"net/http"
	"strings"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, "{\"hello\":\"world\"}")
}

func contactHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprint(w, "<h1>Contact Page</h1>")
}

func pathHandler(w http.ResponseWriter, r *http.Request) {
	log := strings.Join([]string{"Processing", r.Method, r.URL.Path}, " ")
	fmt.Println(log)

	switch r.URL.Path {
	case "/":
		homeHandler(w, r)
	case "/contact":
		contactHandler(w, r)
	default:
		http.Error(w, "Page not found", http.StatusNotFound)
	}
}

func main() {
	http.HandleFunc("/", pathHandler)
	fmt.Println("Starting server on :3000")
	http.ListenAndServe(":3000", nil)
}
