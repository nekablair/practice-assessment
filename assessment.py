'''
PREP✅
Parameters: item_cost, money_paid
Return: total and breakdown of how many bills and cents it equates to for your change
-The total change amount to two decimal places.
-A breakdown of the change in terms of bills and coins.
-Proper pluralization of the denominations.
Example:
print(exact_change(10.75, 20))
# Output: "Your total is 9.25: 1 Five Dollar Bill, 2 Two Dollar Bills, and 1 Quarter."
Pseudocode:
-make dictionary/container with all the dollar bills and change and how much it amounts to✅
-iterate through, subtracting each amount sum and appending it to the appropriate bill or cent✅
-create f statement that outputs total amount of money and breakdown as shown in exammple✅
-use conditional logic to output a different return if the amt the person has is less than the item_cost✅
-use conditional logic to output a different return if the person only has one of each bill or cent✅
-consider edge cases for negative numbers✅
'''

def exact_change(item_cost, money_paid):
    change = money_paid - item_cost
    bills = [
        (('One Hundred Dollar Bill', 'One Hundred Dollar Bills'), 100.00), 
        (('Fifty Dollar Bill', 'Fifty Dollar Bills'), 50.00),
        (('Twenty Dollar Bill', 'Twenty Dollar Bills'), 20.00),
        (('Ten Dollar Bill', 'Ten Dollar Bills'), 10.00),
        (('Five Dollar Bill', 'Five Dollar Bills'), 5.00),
        (('Two Dollar Bill', 'Two Dollar Bills'), 2.00),
        (('One Dollar Bill', 'One Dollar Bills'), 1.00),
        (('Quarter', 'Quarters'), 0.25),
        (('Dime', 'Dimes'), 0.10),
        (('Nickel', 'Nickels'), 0.05),
        (('Penny', 'Pennies'), 0.01),
    ]
    results = []
    for name, value in bills:
        total = int(change // value)
        #tuple unpacking
        single, plural = name
        if money_paid - item_cost == 0:
            return "Your total is 0.00."
        elif total == 1:
            results.append(f"{total} {single}")
            change -= total * value
        elif total > 1:
            results.append(f"{total} {plural}")
            change -= total * value
        if money_paid < item_cost:
            return "You can't afford this item."
        #f string for final output
    if len(results) == 1:
        return f"Your total is {money_paid - item_cost:.2f}: {', '.join(results) }."
    
    results[-1] = "and " + results[-1]
    results_str = ", ".join(results)

    #use string formatting in order to make sure the number prints out to 2 decimal places
    return f"Your total is {money_paid - item_cost:.2f}: {results_str}."
