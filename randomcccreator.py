import random

def generate_card_number():
    card_number = "4169"
    for _ in range(12):
        digit = random.randint(0, 9)
        card_number += str(digit)
    return card_number

def generate_cvv():
    cvv = ""
    for _ in range(3):
        digit = random.randint(0, 9)
        cvv += str(digit)
    return cvv

def generate_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(23, 30)
    expiry_date = str(month).zfill(2) + "/" + str(year)
    return expiry_date

generated_combinations = set()

while True:
    card_number = generate_card_number()
    cvv = generate_cvv()
    expiry_date = generate_expiry_date()

    combination = (card_number, cvv, expiry_date)

    if combination not in generated_combinations:
        generated_combinations.add(combination)
        print("Kart Numarası:", card_number)
        print("CVV:", cvv)
        print("Bitiş Tarihi:", expiry_date)
        print("--------------------------------")
        if len(generated_combinations) == 100:
            break