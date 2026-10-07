from pyscript import document, display

prices = {
    "cerealPrawns": 100,
    "Shanghai": 100,
    "RiceStired": 100,
    "Coke": 70,
    "XioBao": 60,
    "TuronCream": 60
}


def Order(e):
    subtotal = 0

    for item in prices:
        checkbox = document.getElementById(item)

        if checkbox.checked:
            subtotal += prices[item]

    vat = subtotal * 0.12
    total = subtotal + vat

    display(f"SUBTOTAL: ₱{subtotal:.2f}", target="receipt")
    display(f"VAT: ₱{vat:.2f}", target="receipt")
    display(f"TOTAL: ₱{total:.2f}", target="receipt")