package main

import (
	"testing"
)

func TestBlockManager_Deduplication(t *testing.T) {
	bm := NewBlockManager()
	data := []byte("netapp-data-block")

	// Write same data under two different logical IDs
	err1 := bm.Write("id1", data)
	err2 := bm.Write("id2", data)

	if err1 != nil || err2 != nil {
		t.Fatalf("Write failed: %v, %v", err1, err2)
	}

	// Verify logical mapping
	if len(bm.index) != 2 {
		t.Errorf("Expected 2 logical entries, got %d", len(bm.index))
	}

	// Verify physical deduplication
	if len(bm.blocks) != 1 {
		t.Errorf("Deduplication failed: expected 1 physical block, got %d", len(bm.blocks))
	}

	// Verify reference count via the pointer
	hash := bm.index["id1"]
	if bm.blocks[hash].refCount != 2 {
		t.Errorf("Expected refCount 2, got %d", bm.blocks[hash].refCount)
	}
}

func TestBlockManager_CleanupOnDelete(t *testing.T) {
	bm := NewBlockManager()
	data := []byte("temporary-data")

	bm.Write("id1", data)
	bm.Write("id2", data)

	// Delete first reference
	bm.Delete("id1")
	if len(bm.blocks) != 1 {
		t.Fatal("Physical block should still exist for id2")
	}

	// Delete final reference
	bm.Delete("id2")
	if len(bm.blocks) != 0 {
		t.Errorf("Physical block was not garbage collected, count: %d", len(bm.blocks))
	}
}

func TestBlockManager_OverwriteAttempt(t *testing.T) {
	bm := NewBlockManager()
	data := []byte("initial-data")

	bm.Write("id1", data)
	err := bm.Write("id1", []byte("new-data"))

	if err == nil {
		t.Error("Expected error when writing to an existing blockID, but got nil")
	}
}

func TestBlockManager_Concurrency(t *testing.T) {
	bm := NewBlockManager()
	data := []byte("concurrent-data")

	const workers = 100
	done := make(chan bool)

	for i := 0; i < workers; i++ {
		go func(id int) {
			blockID := string(rune(id))
			bm.Write(blockID, data)
			done <- true
		}(i)
	}

	// Wait for all goroutines
	for i := 0; i < workers; i++ {
		<-done
	}

	// If locking is correct, we should have 'workers' logical IDs but only 1 physical block
	if len(bm.blocks) != 1 {
		t.Errorf("Concurrency failure: expected 1 physical block, got %d", len(bm.blocks))
	}

	hash := ""
	for _, h := range bm.index {
		hash = h
		break
	} // Get any hash
	if bm.blocks[hash].refCount != workers {
		t.Errorf("RefCount mismatch: expected %d, got %d", workers, bm.blocks[hash].refCount)
	}
}
