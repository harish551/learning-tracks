package main

import (
	"fmt"
	"time"
)

// worker represents a single consumer in the pool
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Printf("worker %d started job %d\n", id, j)
		// Simulate a time-consuming task
		time.Sleep(time.Second)
		fmt.Printf("worker %d finished job %d\n", id, j)
		results <- j * 2
	}
}

func main() {
	const numJobs = 5
	const numWorkers = 3

	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// 1. Start M workers
	for w := 1; w <= numWorkers; w++ {
		go worker(w, jobs, results)
	}

	// 2. Send N jobs to the channel
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs) // Closing tells workers there are no more jobs

	// 3. Collect the results
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}
