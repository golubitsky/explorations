## Refresh on save

```sh
fswatch -o ./fill_element_with_grid.html | xargs -n1 -I {} osascript -e 'tell application "Google Chrome" to tell the active tab of its first window to reload'
```
