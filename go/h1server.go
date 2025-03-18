// h1server.go

package main

import (
"strconv"
"fmt" 
"net/http"
"time"
//"io"
)

// content-length limit (bytes), actual length is slightly bigger due to additional headers from Cloudflare
const maxCL = 2000000

func main() {
http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
	rc := http.NewResponseController(w)
	w.Header().Set("Content-Type", "application/json")
	switch r.Method {
	case "POST":
		fmt.Println("Received request: ", r.URL.Path, r.Proto, time.Now().Format(time.RFC3339))
		cl ,_ := strconv.Atoi(r.Header.Get("Content-Length"))
		if cl <= maxCL {
			fmt.Println("accepting request body, size:", cl)
			// Real logic can be put here:
			// rB, err := io.ReadAll(r.Body)
			// After then, can be 201 or 202 depending on the processing time
			w.WriteHeader(http.StatusCreated)
			w.Write([]byte(`{"message": "POST received"}`))
			// response body must be closed or Go will not flush the response status code
			r.Body.Close()
			//w.(http.Flusher).Flush()
			return
		} else {
			fmt.Println("rejecting request body, size:", cl)
			w.WriteHeader(http.StatusRequestEntityTooLarge)   
			w.Write([]byte(`{"message": "POST rejected"}`))
			r.Body.Close()
			//w.(http.Flusher).Flush()
			return
		}

        default:
		fmt.Println("Rejected request: ", r.URL.Path, r. Proto, time.Now().Format(time.RFC3339))
		w.WriteHeader(http.StatusNotFound)
		w.Write([]byte(`{"message": "Unsupported"}`))
		}

	err := rc.Flush()
	if err != nil {
		fmt.Println("Flush failing", time.Now().Format(time.RFC3339))
		}
})

srv := &http.Server{
	Addr:           ":8080",
	ReadTimeout:    10 * time.Second,
	WriteTimeout:   10 * time.Second,
	MaxHeaderBytes: 1 << 14,
}

fmt.Println("Server started: ", time.Now().Format(time.RFC3339))
// for h2: ListenAndServeTLS( ... ), and you need a cert. For cf tunnel->ingree, there is no h2c support
err := srv.ListenAndServe()
	if err != nil {
		fmt.Println("Error starting the server: ", err)
}
