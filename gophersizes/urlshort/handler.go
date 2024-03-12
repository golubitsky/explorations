package urlshort

import (
	"net/http"

	"gopkg.in/yaml.v3"
)

type RedirectHandler struct {
	pathsToUrls map[string]string
	fallback    http.Handler
}

func (m RedirectHandler) handlerFunc(w http.ResponseWriter, r *http.Request) {
	redirect, ok := m.pathsToUrls[r.URL.String()]

	if ok {
		http.Redirect(w, r, redirect, http.StatusSeeOther)
	} else {
		m.fallback.ServeHTTP(w, r)
	}
}

// MapHandler will return an http.HandlerFunc (which also
// implements http.Handler) that will attempt to map any
// paths (keys in the map) to their corresponding URL (values
// that each key in the map points to, in string format).
// If the path is not provided in the map, then the fallback
// http.Handler will be called instead.
func MapHandler(pathsToUrls map[string]string, fallback http.Handler) http.HandlerFunc {
	redirect := RedirectHandler{
		pathsToUrls: pathsToUrls,
		fallback:    fallback,
	}

	return redirect.handlerFunc
}

type PathURLYAML struct {
	Path string `yaml:"path"`
	URL  string `yaml:"url"`
}

type PathURLJSON struct {
	Path string `json:"path"`
	URL  string `json:"url"`
}

func parseYAML(yml []byte) ([]PathURLYAML, error) {
	var paths []PathURLYAML

	err := yaml.Unmarshal([]byte(yml), &paths)

	return paths, err
}

func mapFromYAML(paths []PathURLYAML) map[string]string {
	pathMap := make(map[string]string)
	for _, p := range paths {
		pathMap[p.Path] = p.URL
	}

	return pathMap
}

// YAMLHandler will parse the provided YAML and then return
// an http.HandlerFunc (which also implements http.Handler)
// that will attempt to map any paths to their corresponding
// URL. If the path is not provided in the YAML, then the
// fallback http.Handler will be called instead.
//
// YAML is expected to be in the format:
//
//   - path: /some-path
//     url: https://www.some-url.com/demo
//
// The only errors that can be returned all related to having
// invalid YAML data.
//
// See MapHandler to create a similar http.HandlerFunc via
// a mapping of paths to urls.
func YAMLHandler(yml []byte, fallback http.Handler) (http.HandlerFunc, error) {
	paths, err := parseYAML(yml)
	if err != nil {
		return nil, err
	}

	return MapHandler(mapFromYAML(paths), fallback), nil
}

func parseJSON(json []byte) ([]PathURLJSON, error) {
	var paths []PathURLJSON

	err := yaml.Unmarshal([]byte(json), &paths)

	return paths, err
}

func mapFromJSON(paths []PathURLJSON) map[string]string {
	pathMap := make(map[string]string)
	for _, p := range paths {
		pathMap[p.Path] = p.URL
	}

	return pathMap
}

func JSONHandler(json []byte, fallback http.Handler) (http.HandlerFunc, error) {
	paths, err := parseJSON(json)
	if err != nil {
		return nil, err
	}

	return MapHandler(mapFromJSON(paths), fallback), nil
}
