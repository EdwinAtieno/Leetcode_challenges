def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


"""
everyday in super,arkets, cashiers have to give back the correct change to customers who pay in cash.
how can they determine chich bills to give back so that the number of bills is the smallest possible?
in tihs exercise, we ask you to find the optimal solution to give back change when a checkout only has $2, $5 and $10 bills.
to make the problem simpler, we'll consider that we have an infinite amounts of bills.
implement the function change(cash) which should returna dictionary whode two, five and ten attributes represent the change
to give back. If it is not possible to give back the change the function should return None. to get the maximum amount of points,
your solution will have to return the correct change with the minimal amounts of bills
"""


def change(cash):
    if cash % 2 == 1:
        return None
    ten = cash // 10
    five = 0
    two = 0
    cash = cash - ten * 10
    if cash % 5 == 0:
        five = cash // 5
    else:
        five = 1
        cash = cash - 5
        two = cash // 2
    return {"two": two, "five": five, "ten": ten}
