package main

import (
	"fmt"
	"sync"
)

type Counter struct {
	mu sync.Mutex
	count int
}

func (c *Counter) Increment() {
	c.mu.Lock()
	defer c.mu.Unlock()
	// Increment the counter
	c.count++
}

func (c *Counter) GetCount() int {
	c.mu.Lock()
	defer c.mu.Unlock()

	return c.count
}

func main() {
	counter := &Counter{}

	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func() {
			prev := counter.GetCount()
			counter.Increment()
			fmt.Printf("Current: %d, Prev: %d\n", counter.GetCount(), prev)
			wg.Done()
		}()
	}
	wg.Wait()

	fmt.Println("final count value is ", counter.GetCount())
}