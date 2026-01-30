package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/books/{title}/page/{page}", func(w http.ResponseWriter, r *http.Request) {
		vars := mux.Vars(r)

		title := vars["title"]
		page := vars["page"]

		fmt.Println("Title:", title)
		fmt.Println("Page:", page)
	})

	http.ListenAndServe(":8080", r)
}
