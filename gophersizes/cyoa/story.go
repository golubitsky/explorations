package cyoa

type Story map[string]Chapter

type Chapter struct {
	Title      string   `json:"title"`
	Paragraphs []string `json:"story"`
	Options    []struct {
	}
}

type Option struct {
	Text    string   `json:"text"`
	Chapter string   `json:"arc"`
	Options []Option `json:"options"`
}
