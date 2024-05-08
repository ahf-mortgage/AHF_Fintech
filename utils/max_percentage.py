
def calculate_balance_percentage(rate, initial_balance):
    """
    Calculates the percentage at which the balance becomes zero.

    Arguments:
    rate -- The interest rate as a decimal (e.g., 0.05 for 5%).
    initial_balance -- The initial balance.

    Returns:
    percentage -- The percentage at which the balance becomes zero.
    """

    percentage = 0  # Initial percentage
    balance = initial_balance

    while balance > 0:
        print("balance ",balance)
        balance *= (1 + rate)
        percentage += 1

    return percentage

# Example usage
rate = 0.05  # 5% interest rate
initial_balance = 1000
percentage = calculate_balance_percentage(rate, initial_balance)

print("Percentage at which balance becomes zero:", percentage)
        
