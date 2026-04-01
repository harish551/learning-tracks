package main

import (
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"sync"
)

type PhysicalBlock struct {
	data     []byte
	refCount int
}

type BlockManager struct {
	index  map[string]string         // logicalID -> hash
	blocks map[string]*PhysicalBlock // hash -> physical data
	mu     sync.Mutex
}

func NewBlockManager() *BlockManager {
	return &BlockManager{
		index:  make(map[string]string),
		blocks: make(map[string]*PhysicalBlock),
	}
}

func (bm *BlockManager) Write(blockID string, data []byte) error {
	bm.mu.Lock()
	defer bm.mu.Unlock()

	if _, ok := bm.index[blockID]; ok {
		return errors.New("block ID already exists")
	}

	// High-performance hex encoding
	hashBytes := sha256.Sum256(data)
	hash := hex.EncodeToString(hashBytes[:])

	if block, ok := bm.blocks[hash]; ok {
		block.refCount++
		bm.index[blockID] = hash
		return nil
	}

	bm.blocks[hash] = &PhysicalBlock{
		data:     data,
		refCount: 1,
	}
	bm.index[blockID] = hash
	return nil
}

func (bm *BlockManager) Delete(blockID string) error {
	bm.mu.Lock()
	defer bm.mu.Unlock()

	hash, ok := bm.index[blockID]
	if !ok {
		return errors.New("block not found")
	}

	block := bm.blocks[hash]
	block.refCount--

	// Logic cleanup: only delete from blocks if refCount hits 0
	if block.refCount == 0 {
		delete(bm.blocks, hash)
	}

	// remove the logical index
	delete(bm.index, blockID)
	return nil
}
