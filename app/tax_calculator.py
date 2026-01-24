from tax_rules_2026 import PERSONAL_ALLOWANCE, TAX_BRACKETS

def calculate_tax(income):
    taxable_income = max(0, income - PERSONAL_ALLOWANCE)
    tax = 0
    remaining_income = taxable_income

    for bracket_limit, rate in TAX_BRACKETS:
        if remaining_income <= 0:
            break

        amount_in_bracket = min(remaining_income, bracket_limit)
        tax += amount_in_bracket * rate
        remaining_income -= amount_in_bracket

    return tax


if __name__ == "__main__":
    income = float(input("Enter annual income (₦): "))
    tax = calculate_tax(income)
    print(f"Estimated Tax: ₦{tax:,.2f}")
