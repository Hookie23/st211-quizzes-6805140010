def convert(number: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Check for characters that are not Roman numeral symbols
    for char in number:
        if char not in values:
            return "Invalid Roman numeral"

    total = 0

    # Calculate the value
    for i in range(len(number)):
        if i + 1 < len(number) and values[number[i]] < values[number[i + 1]]:
            total -= values[number[i]]
        else:
            total += values[number[i]]

    # Create the correct Roman numeral representation
    roman_values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    correct = ""
    temp = total

    for value, symbol in roman_values:
        while temp >= value:
            correct += symbol
            temp -= value

    # Check whether the original input was a valid Roman numeral
    if correct != number:
        return "Invalid Roman numeral"

    return total