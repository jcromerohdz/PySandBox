def tip_caculator():
    print("Wlecome to the tip calculator.")
    total = input("What was the total bill? $")
    persons = input("How many people to split the bill? ")
    tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

    tip_percentage = float(total) * (float(tip)/100.0)
    subtotal = float(total) + tip_percentage
    final_total_by_person = subtotal / int(persons)

    print(f"Each person should pay : ${round(final_total_by_person, 1)}")

tip_caculator()