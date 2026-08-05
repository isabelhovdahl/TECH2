# Exercise 1 (Part A) — Effective Interest Rate

def effective_interest_rate(r, n=12):
    """Calculate the effective annual interest rate."""
    return (1 + r / n)**n - 1


if __name__ == "__main__":
    annual_rate = 0.09

    # Compounded quarterly
    eff_rate1 = effective_interest_rate(annual_rate, n=4)
    print(f"A {100 * annual_rate:.2f}% annual rate compounded quarterly gives an effective rate of {100 * eff_rate1:.2f}%.")

    # Compounded monthly
    eff_rate2 = effective_interest_rate(annual_rate)
    print(f"A {100 * annual_rate:.2f}% annual rate compounded monthly gives an effective rate of {100 * eff_rate2:.2f}%.")
