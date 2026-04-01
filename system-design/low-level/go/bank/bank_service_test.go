package main

import (
	"fmt"
	"math/rand"
	"sync"
	"testing"
)

// ─── Unit Tests ─────────────────────────────────────────────────────────────

func TestCreateAccount(t *testing.T) {
	bank := NewBank()

	acc, err := bank.CreateAccount("Alice", 1000)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if acc.GetName() != "Alice" {
		t.Errorf("expected name Alice, got %s", acc.GetName())
	}
	if acc.GetBalance() != 1000 {
		t.Errorf("expected balance 1000, got %.2f", acc.GetBalance())
	}
	if bank.TotalDepositors() != 1 {
		t.Errorf("expected 1 depositor, got %d", bank.TotalDepositors())
	}
}

func TestCreateAccountNegativeDeposit(t *testing.T) {
	bank := NewBank()
	_, err := bank.CreateAccount("Bad", -100)
	if err == nil {
		t.Fatal("expected error for negative initial deposit")
	}
}

func TestDeposit(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("Bob", 500)

	err := acc.Deposit(200)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if acc.GetBalance() != 700 {
		t.Errorf("expected balance 700, got %.2f", acc.GetBalance())
	}
}

func TestDepositInvalidAmount(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("Bob", 500)

	if err := acc.Deposit(0); err == nil {
		t.Error("expected error for zero deposit")
	}
	if err := acc.Deposit(-50); err == nil {
		t.Error("expected error for negative deposit")
	}
}

func TestWithdraw(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("Charlie", 300)

	err := acc.Withdraw(100)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if acc.GetBalance() != 200 {
		t.Errorf("expected balance 200, got %.2f", acc.GetBalance())
	}
}

func TestWithdrawInsufficientFunds(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("Charlie", 100)

	err := acc.Withdraw(500)
	if err == nil {
		t.Fatal("expected insufficient funds error")
	}
}

func TestWithdrawInvalidAmount(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("Charlie", 100)

	if err := acc.Withdraw(0); err == nil {
		t.Error("expected error for zero withdrawal")
	}
	if err := acc.Withdraw(-10); err == nil {
		t.Error("expected error for negative withdrawal")
	}
}

func TestGetAccount(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("Diana", 100)

	found, err := bank.GetAccount(acc.GetID())
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if found.GetID() != acc.GetID() {
		t.Errorf("expected ID %s, got %s", acc.GetID(), found.GetID())
	}
}

func TestGetAccountNotFound(t *testing.T) {
	bank := NewBank()
	_, err := bank.GetAccount("ACC-9999")
	if err == nil {
		t.Fatal("expected error for non-existent account")
	}
}

func TestTotalAmount(t *testing.T) {
	bank := NewBank()
	bank.CreateAccount("A", 100)
	bank.CreateAccount("B", 200)
	bank.CreateAccount("C", 300)

	total := bank.TotalAmount()
	if total != 600 {
		t.Errorf("expected total 600, got %.2f", total)
	}
}

// ─── Concurrency Tests ─────────────────────────────────────────────────────

// TestConcurrentDeposits verifies that concurrent deposits on the same account
// produce the correct final balance (no lost updates).
func TestConcurrentDeposits(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("ConcurrentUser", 0)

	var wg sync.WaitGroup
	numGoroutines := 1000
	depositAmount := 10.0

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			acc.Deposit(depositAmount)
		}()
	}
	wg.Wait()

	expected := float64(numGoroutines) * depositAmount
	if acc.GetBalance() != expected {
		t.Errorf("expected balance %.2f, got %.2f (lost updates!)", expected, acc.GetBalance())
	}
}

// TestConcurrentWithdrawals verifies that concurrent withdrawals never
// overdraw the account (no race conditions on balance check).
func TestConcurrentWithdrawals(t *testing.T) {
	bank := NewBank()
	initialBalance := 1000.0
	acc, _ := bank.CreateAccount("WithdrawUser", initialBalance)

	var wg sync.WaitGroup
	numGoroutines := 200
	withdrawAmount := 10.0

	var successCount int64
	var mu sync.Mutex

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			if err := acc.Withdraw(withdrawAmount); err == nil {
				mu.Lock()
				successCount++
				mu.Unlock()
			}
		}()
	}
	wg.Wait()

	// successCount * withdrawAmount should exactly equal (initialBalance - finalBalance)
	finalBalance := acc.GetBalance()
	withdrawn := float64(successCount) * withdrawAmount

	if finalBalance < 0 {
		t.Errorf("balance went negative: %.2f (race condition!)", finalBalance)
	}
	if finalBalance+withdrawn != initialBalance {
		t.Errorf("accounting mismatch: initial=%.2f, withdrawn=%.2f, final=%.2f",
			initialBalance, withdrawn, finalBalance)
	}
	t.Logf("Successful withdrawals: %d/%d, final balance: %.2f", successCount, numGoroutines, finalBalance)
}

// TestConcurrentMixedOperations simulates a realistic scenario with deposits,
// withdrawals, and balance reads all happening concurrently on the same account.
func TestConcurrentMixedOperations(t *testing.T) {
	bank := NewBank()
	acc, _ := bank.CreateAccount("MixedUser", 5000)

	var wg sync.WaitGroup

	// 100 depositors
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			acc.Deposit(float64(rand.Intn(50) + 1))
		}()
	}

	// 100 withdrawers
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			acc.Withdraw(float64(rand.Intn(30) + 1))
		}()
	}

	// 50 balance readers
	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			bal := acc.GetBalance()
			// Balance should never go negative
			if bal < 0 {
				t.Errorf("negative balance detected: %.2f", bal)
			}
		}()
	}

	wg.Wait()

	finalBalance := acc.GetBalance()
	if finalBalance < 0 {
		t.Errorf("final balance is negative: %.2f", finalBalance)
	}
	t.Logf("Final balance after mixed operations: %.2f", finalBalance)
}

// TestConcurrentAccountCreation verifies that creating accounts from multiple
// goroutines produces unique IDs and the correct depositor count.
func TestConcurrentAccountCreation(t *testing.T) {
	bank := NewBank()

	var wg sync.WaitGroup
	numAccounts := 100
	ids := make([]string, numAccounts)
	var mu sync.Mutex

	for i := 0; i < numAccounts; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			acc, err := bank.CreateAccount(fmt.Sprintf("User-%d", idx), float64(idx*10))
			if err != nil {
				t.Errorf("failed to create account: %v", err)
				return
			}
			mu.Lock()
			ids[idx] = acc.GetID()
			mu.Unlock()
		}(i)
	}
	wg.Wait()

	if bank.TotalDepositors() != numAccounts {
		t.Errorf("expected %d depositors, got %d", numAccounts, bank.TotalDepositors())
	}

	// Verify all IDs are unique
	idSet := make(map[string]bool)
	for _, id := range ids {
		if idSet[id] {
			t.Errorf("duplicate account ID: %s", id)
		}
		idSet[id] = true
	}
	t.Logf("Successfully created %d accounts concurrently with unique IDs", numAccounts)
}

// TestConcurrentMultiAccountOperations simulates a realistic bank day:
// multiple accounts being operated on by multiple goroutines simultaneously.
func TestConcurrentMultiAccountOperations(t *testing.T) {
	bank := NewBank()

	// Create 5 accounts
	accounts := make([]*Account, 5)
	names := []string{"Alice", "Bob", "Charlie", "Diana", "Eve"}
	for i, name := range names {
		acc, _ := bank.CreateAccount(name, 1000)
		accounts[i] = acc
	}

	initialTotal := bank.TotalAmount()
	t.Logf("Initial total across all accounts: %.2f", initialTotal)

	var wg sync.WaitGroup

	// 200 goroutines doing random operations across random accounts
	for i := 0; i < 200; i++ {
		wg.Add(1)
		go func(workerID int) {
			defer wg.Done()

			acc := accounts[rand.Intn(len(accounts))]
			amount := float64(rand.Intn(50) + 1)

			switch rand.Intn(3) {
			case 0:
				acc.Deposit(amount)
			case 1:
				acc.Withdraw(amount) // may fail, that's okay
			case 2:
				_ = acc.GetBalance() // read operation
			}
		}(i)
	}

	// Concurrently read bank-level stats
	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			_ = bank.TotalDepositors()
			_ = bank.TotalAmount()
		}()
	}

	wg.Wait()

	t.Logf("Final total across all accounts: %.2f", bank.TotalAmount())
	t.Logf("Total depositors: %d", bank.TotalDepositors())

	// All balances should be non-negative
	for _, acc := range accounts {
		if acc.GetBalance() < 0 {
			t.Errorf("account %s has negative balance: %.2f", acc.GetID(), acc.GetBalance())
		}
	}
}

// ─── Simulation (run with `go test -v -run Simulation`) ─────────────────────

// TestBankSimulation provides a verbose simulation you can watch to see
// the bank service operating under concurrent load.
func TestBankSimulation(t *testing.T) {
	bank := NewBank()

	// Step 1: Create accounts
	t.Log("══════════════ Creating Accounts ══════════════")
	alice, _ := bank.CreateAccount("Alice", 1000)
	bob, _ := bank.CreateAccount("Bob", 500)
	charlie, _ := bank.CreateAccount("Charlie", 250)
	t.Logf("Created: %s (Alice: %.2f), %s (Bob: %.2f), %s (Charlie: %.2f)",
		alice.GetID(), alice.GetBalance(),
		bob.GetID(), bob.GetBalance(),
		charlie.GetID(), charlie.GetBalance())

	// Step 2: Concurrent operations
	t.Log("\n══════════════ Running Concurrent Operations ══════════════")
	var wg sync.WaitGroup
	accounts := []*Account{alice, bob, charlie}

	for i := 0; i < 30; i++ {
		wg.Add(1)
		go func(workerID int) {
			defer wg.Done()

			acc := accounts[rand.Intn(len(accounts))]
			amount := float64(rand.Intn(100) + 1)

			if rand.Intn(2) == 0 {
				err := acc.Deposit(amount)
				if err != nil {
					t.Logf("[Worker %02d] ❌ Deposit  %.2f → %s: %v", workerID, amount, acc.GetID(), err)
				} else {
					t.Logf("[Worker %02d] ✅ Deposit  %.2f → %s (bal: %.2f)", workerID, amount, acc.GetID(), acc.GetBalance())
				}
			} else {
				err := acc.Withdraw(amount)
				if err != nil {
					t.Logf("[Worker %02d] ❌ Withdraw %.2f ← %s: %v", workerID, amount, acc.GetID(), err)
				} else {
					t.Logf("[Worker %02d] ✅ Withdraw %.2f ← %s (bal: %.2f)", workerID, amount, acc.GetID(), acc.GetBalance())
				}
			}
		}(i)
	}

	// Concurrently create more accounts
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			name := fmt.Sprintf("User-%d", id)
			acc, _ := bank.CreateAccount(name, float64(rand.Intn(500)))
			t.Logf("[Creator  %d] ✅ Created %s for %s (bal: %.2f)", id, acc.GetID(), acc.GetName(), acc.GetBalance())
		}(i)
	}

	wg.Wait()

	// Step 3: Final report
	t.Log("\n══════════════ Final Bank Report ══════════════")
	t.Logf("Total Depositors : %d", bank.TotalDepositors())
	t.Logf("Total Amount     : %.2f", bank.TotalAmount())

	bank.ListAccounts()

	// Sanity checks
	if bank.TotalDepositors() != 8 { // 3 initial + 5 concurrent
		t.Errorf("expected 8 depositors, got %d", bank.TotalDepositors())
	}
}
