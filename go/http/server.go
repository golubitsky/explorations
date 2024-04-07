package main

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/go-chi/chi/v5"
)

func logRequest(r *http.Request) {
	log := strings.Join([]string{"Processing", r.Method, r.URL.Path}, " ")
	fmt.Println(log)
}
func homeHandler(w http.ResponseWriter, r *http.Request) {
	logRequest(r)

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, "{\"hello\":\"world\"}")
}

func contactHandler(w http.ResponseWriter, r *http.Request) {
	logRequest(r)

	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprint(w, "<h1>Contact Page</h1>")
}

func faqHandler(w http.ResponseWriter, r *http.Request) {
	logRequest(r)

	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprint(w, "<h1>Faq Page</h1>")
}

func main() {
	r := chi.NewRouter()
	r.Get("/", homeHandler)
	r.Get("/contact", contactHandler)
	r.Get("/faq", faqHandler)
	r.Route("/users", func(r chi.Router) {
		r.Get("/{userId}", func(w http.ResponseWriter, r *http.Request) {
			userId := chi.URLParam(r, "userId")
			fmt.Fprint(w, "fetching user ", userId)
		})
	})

	r.NotFound(func(w http.ResponseWriter, r *http.Request) {
		logRequest(r)

		http.Error(w, "Page not found", http.StatusNotFound)
	})
	fmt.Println("Starting server on :3000")
	http.ListenAndServe(":3000", r)
}
