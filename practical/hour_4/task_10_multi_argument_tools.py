"""
PRACTICAL CHALLENGE: Multi-Argument Mathematical Tools (LC-H4-P10)
=====================================================
ID: LC-H4-P10
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a set of tools (`calculate_tax(subtotal, rate=0.1)` and `format_currency(amount, currency='USD')`)
and test direct invocations with dictionary inputs.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def calculate_tax(subtotal: float, rate: float = 0.1) -> float:
    """Calculates tax amount on a subtotal."""
    return round(subtotal * rate, 2)

def format_currency(amount: float, currency: str = "USD") -> str:
    """Formats numeric amount with currency code."""
    return f"{currency} {amount:.2f}"

def test_multi_arg_tools():
    tax = calculate_tax(subtotal=150.0, rate=0.08)
    assert tax == 12.0
    formatted = format_currency(amount=162.0, currency="USD")
    assert formatted == "USD 162.00"

if __name__ == '__main__':
    test_multi_arg_tools()
    print("✓ Task 10 passed!")
