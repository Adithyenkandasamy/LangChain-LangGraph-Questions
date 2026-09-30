"""
PRACTICAL CHALLENGE: Iterative Loop State Simulation (LC-H6-P03)
=====================================================
ID: LC-H6-P03
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Simulate the iterative number guessing loop demonstrated in the lecture:
An agent makes a guess, state receives feedback ('higher' or 'lower'), updates bounds, and repeats until guessed.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def simulate_binary_search_loop(target: int, low: int = 1, high: int = 100) -> list:
    history = []
    guess = (low + high) // 2
    while low <= high:
        history.append(guess)
        if guess == target:
            break
        elif guess < target:
            low = guess + 1
        else:
            high = guess - 1
        guess = (low + high) // 2
    return history

def test_number_guessing():
    target = 42
    guesses = simulate_binary_search_loop(target, low=1, high=100)
    assert guesses[-1] == 42
    assert len(guesses) <= 7  # log2(100) < 7

if __name__ == '__main__':
    test_number_guessing()
    print("✓ Task 03 passed!")
