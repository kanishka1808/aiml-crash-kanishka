# tip_calculator.py --- This file calculates tip and total bill

# print() only displays output
# return sends values back from a function

def calculate_tip(bill, tip_percent):

    tip = (bill * tip_percent) / 100
    total = bill + tip

    return {
        "tip": tip,
        "total": total
    }


bill1 = calculate_tip(1000, 10)
bill2 = calculate_tip(2500, 15)
bill3 = calculate_tip(500, 5)

print("Bill 1:", bill1)
print("Bill 2:", bill2)
print("Bill 3:", bill3)