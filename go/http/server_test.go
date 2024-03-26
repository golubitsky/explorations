package main

import (
	"io"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestHandlerFunc(t *testing.T) {
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	w := httptest.NewRecorder()

	handlerFunc(w, req)

	res := w.Result()
	defer res.Body.Close()

	data, err := io.ReadAll(res.Body)

	if err != nil {
		t.Errorf("expected no error but got %v", err)
	}

	if string(data) != "<h1>Hello, World</h1>" {
		t.Errorf("got unexpected response body: %v", string(data))
	}

	if res.StatusCode != http.StatusOK {
		t.Errorf("got unexpected status code %d", res.StatusCode)
	}
}
