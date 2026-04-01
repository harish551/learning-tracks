package main

import "fmt"

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		results <- j * 2
		fmt.Printf("Worker %d started job %d\n", id, j)
	}
}
func main() {
	jobs := make(chan int, 5)
	results := make(chan int)
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)
	for r := 1; r <= 5; r++ {
		fmt.Println(<-results)
	}
}
