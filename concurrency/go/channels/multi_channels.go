package main

import (
	"context"
	"fmt"
	"time"
)

func fetchPrimary(primary chan <- string) {
	fmt.Println("Fetching primary data")
	time.Sleep(200 * time.Millisecond)
	primary <- "data from primary"
}

func fetchReplica(replica chan <- string) {
	fmt.Println("Fetching replica data")
	time.Sleep(200 * time.Millisecond)
	replica <- "data from replica"
}

func main() {
	primary := make(chan string)
	replica := make(chan string)

	go fetchPrimary(primary)
	go fetchReplica(replica)

	ctx, cancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
    defer cancel()

	select {
		case p := <-primary:
			fmt.Println("Primary:", p)
		case r := <-replica:
			fmt.Println("Replica:", r)
		case <-ctx.Done():
			fmt.Println("Timeout")
	}
}