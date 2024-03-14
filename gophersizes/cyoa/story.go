package cyoa

import (
	"encoding/json"
	"io"
)

func StoryFromJson(r io.Reader) (Story, error) {
	d := json.NewDecoder(r)
	story := make(Story)

	err := d.Decode(&story)

	if err != nil {
		return nil, err
	}

	return story, nil
}

type Story map[string]Chapter

type Chapter struct {
	Title      string   `json:"title"`
	Paragraphs []string `json:"story"`
	Options    []Option `json:"options"`
}

type Option struct {
	Text    string `json:"text"`
	Chapter string `json:"arc"`
}
