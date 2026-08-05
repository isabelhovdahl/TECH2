# Exercise 1 (Part B) — Comparing Savings Offers

# Note: this import only works if "ex1.py" is in the same folder as this
# file, and your working directory is set to that folder.
from ex1_solution import effective_interest_rate

# Offer (i): 5.9% compounded quarterly
eff_rate1 = effective_interest_rate(r=0.059, n=4)
print(f"Offer (i): 5.9% compounded quarterly gives an effective rate of {100 * eff_rate1:.2f}%.")

# Offer (ii): 6% compounded twice a year
eff_rate2 = effective_interest_rate(r=0.06, n=2)
print(f"Offer (ii): 6% compounded twice a year gives an effective rate of {100 * eff_rate2:.2f}%.")
