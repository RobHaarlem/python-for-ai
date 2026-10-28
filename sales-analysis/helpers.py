def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity*price

def format_currency(amount):
    """Format number as a currency"""
    return f'€{amount:,.2f}'