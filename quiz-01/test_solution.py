from solution import convert

# Normal tests
assert convert("I") == 1
assert convert("V") == 5
assert convert("VI") == 6
assert convert("XVI") == 16
assert convert("IV") == 4
assert convert("IX") == 9
assert convert("XIX") == 19

# Boundary tests
assert convert("I") == 1
assert convert("V") == 5

# Invalid Roman numeral tests
assert convert("VX") == "Invalid Roman numeral"
assert convert("XXC") == "Invalid Roman numeral"
assert convert("VC") == "Invalid Roman numeral"

# Invalid character test
assert convert("A") == "Invalid Roman numeral"

print("All tests passed!")