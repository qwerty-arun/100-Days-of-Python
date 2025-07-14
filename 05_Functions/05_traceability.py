# Improve traceability

def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

order = [100, 120, 180]

for price in order:
    final_amount = add_vat(price, 10)
    print(f"Original price: {price}, Final with VAT: {final_amount}")