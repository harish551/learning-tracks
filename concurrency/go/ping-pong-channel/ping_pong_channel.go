package main

import (
	"context"
	"fmt"
	"time"
)

func ping(pingChan chan<- string, pongChan <-chan string) {
	for i := 0; i < 10; i++ {
		pingChan <- "ping"
		time.Sleep(time.Second)
		fmt.Println(<-pongChan)
	}
	close(pingChan)
}

func pong(pongChan chan<- string, pingChan <-chan string) {
	for msg := range pingChan {
		fmt.Println(msg)
		time.Sleep(time.Second)
		pongChan <- "pong"
	}
	close(pongChan)
}

func main() {

	pingChan := make(chan string)
	pongChan := make(chan string)

	go ping(pingChan, pongChan)
	go pong(pongChan, pingChan)

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	select {
	case <-ctx.Done():
		fmt.Println("Finished")
	}
}