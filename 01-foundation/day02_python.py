customer = "ABC Industries"
invoice_number = "INV-10045"
invoice_amount = 250000
currency = "INR"
overdue_days = 15

print(customer)
print(invoice_number)
print(invoice_amount)
print(currency)
print(overdue_days)

if overdue_days > 30:
    print("Invoice requires attention")
else:
    print("Invoice is within acceptable ageing")

invoices = [
    "INV-1001",
    "INV-1002",
    "INV-1003",
    "INV-1004"
]

for invoice in invoices:
    print(invoice)
print("Number of invoices:", len(invoices))

sap_response = {
    "invoice": {
        "id": "INV-10045",
        "customer": {
            "id": "C10001",
            "name": "ABC Industries"
        },
        "amount": 250000,
        "currency": "INR",
        "overdueDays": 45,
        "status": "OPEN"
    }
}

invoice = sap_response["invoice"]

print("Invoice:", invoice["id"])
print("Customer:", invoice["customer"]["name"])
print("Amount:", invoice["amount"])
print("Currency:", invoice["currency"])
print("Overdue Days:", invoice["overdueDays"])

def calculate_risk(overdue_days, amount):

    if overdue_days > 60 or amount > 500000:
        return "HIGH"

    elif overdue_days > 30:
        return "MEDIUM"

    else:
        return "LOW"

risk = calculate_risk(45, 250000)
print("Invoice Risk:", risk)

risk = calculate_risk(75, 700000)
print("Invoice Risk:", risk)