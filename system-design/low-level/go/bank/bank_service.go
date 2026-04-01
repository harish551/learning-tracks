package main

import (
	"errors"
	"fmt"
	"sync"
)

// Account represents a single user's bank account.
// Each account has its own mutex so operations on different accounts
// can proceed concurrently without blocking each other.
type Account struct {
	mu      sync.RWMutex
	id      string
	name    string
	balance float64
}

// Deposit adds the given amount to the account balance.
// Returns an error if the amount is non-positive.
func (a *Account) Deposit(amount float64) error {
	if amount <= 0 {
		return errors.New("deposit amount must be positive")
	}
	a.mu.Lock()
	defer a.mu.Unlock()
	a.balance += amount
	return nil
}

// Withdraw subtracts the given amount from the account balance.
// Returns an error if the amount is non-positive or exceeds the balance.
func (a *Account) Withdraw(amount float64) error {
	if amount <= 0 {
		return errors.New("withdrawal amount must be positive")
	}
	a.mu.Lock()
	defer a.mu.Unlock()
	if a.balance < amount {
		return fmt.Errorf("insufficient funds: balance=%.2f, requested=%.2f", a.balance, amount)
	}
	a.balance -= amount
	return nil
}

// GetBalance returns the current account balance.
// Uses a read-lock so multiple goroutines can read simultaneously.
func (a *Account) GetBalance() float64 {
	a.mu.RLock()
	defer a.mu.RUnlock()
	return a.balance
}

// GetName returns the account holder's name.
func (a *Account) GetName() string {
	a.mu.RLock()
	defer a.mu.RUnlock()
	return a.name
}

// GetID returns the account ID.
func (a *Account) GetID() string {
	return a.id // immutable after creation, no lock needed
}

// Bank manages multiple accounts and provides aggregate operations.
// It uses a RWMutex for the accounts map so that creating accounts
// is serialised, but reading multiple accounts can happen concurrently.
type Bank struct {
	mu       sync.RWMutex
	accounts map[string]*Account
	nextID   int
}

// NewBank creates a new Bank instance.
func NewBank() *Bank {
	return &Bank{
		accounts: make(map[string]*Account),
	}
}

// CreateAccount creates a new account with the given name and initial deposit.
// Returns the newly created Account and its ID.
func (b *Bank) CreateAccount(name string, initialDeposit float64) (*Account, error) {
	if initialDeposit < 0 {
		return nil, errors.New("initial deposit cannot be negative")
	}

	b.mu.Lock()
	defer b.mu.Unlock()

	b.nextID++
	id := fmt.Sprintf("ACC-%04d", b.nextID)

	account := &Account{
		id:      id,
		name:    name,
		balance: initialDeposit,
	}
	b.accounts[id] = account
	return account, nil
}

// GetAccount retrieves an account by its ID.
// Returns an error if the account does not exist.
func (b *Bank) GetAccount(id string) (*Account, error) {
	b.mu.RLock()
	defer b.mu.RUnlock()

	acc, ok := b.accounts[id]
	if !ok {
		return nil, fmt.Errorf("account %s not found", id)
	}
	return acc, nil
}

// TotalDepositors returns the total number of accounts in the bank.
func (b *Bank) TotalDepositors() int {
	b.mu.RLock()
	defer b.mu.RUnlock()
	return len(b.accounts)
}

// TotalAmount returns the sum of all account balances across the bank.
func (b *Bank) TotalAmount() float64 {
	b.mu.RLock()
	defer b.mu.RUnlock()

	var total float64
	for _, acc := range b.accounts {
		total += acc.GetBalance()
	}
	return total
}

// ListAccounts prints a summary of all accounts.
func (b *Bank) ListAccounts() {
	b.mu.RLock()
	defer b.mu.RUnlock()

	fmt.Println("╔════════════╤══════════════════╤═════════════╗")
	fmt.Println("║ Account ID │ Name             │     Balance ║")
	fmt.Println("╠════════════╪══════════════════╪═════════════╣")
	for _, acc := range b.accounts {
		fmt.Printf("║ %-10s │ %-16s │ %11.2f ║\n", acc.GetID(), acc.GetName(), acc.GetBalance())
	}
	fmt.Println("╚════════════╧══════════════════╧═════════════╝")
}
