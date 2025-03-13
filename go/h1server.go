// h1server.go

package main

import (
"strconv"
"fmt" 
"net/http"
"time"
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
                w.WriteHeader(http.StatusCreated)
                w.Write([]byte(`{"message": "POST received"}`))
                //w.(http.Flusher).Flush()
                return
            } else {
                fmt.Println("rejecting request body, size:", cl)
                w.WriteHeader(http.StatusRequestEntityTooLarge)   
                w.Write([]byte(`{"message": "POST rejected"}`))
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
srv.ListenAndServe()
}
