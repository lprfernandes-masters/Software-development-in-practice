# Rewrite the 8 examples above to PEP Standards.
# https://holypython.com/beginner-python-lessons/lesson-18-python-operators/


# Example 1a: Assignment operator w/ string (=)

greek_island = "Santorini"


# Example 1b: Assignment operator w/ integer & tuple (+=)

earth_age_in_billions = 4.4
universe_age_in_billions = 14
earth_age_in_billions += 0.1

print(earth_age_in_billions)


# 1c: Assignment operator w/ list (=)

asia_wishlist = [
    "Bhutan", "Ha Long", "Laos", "Danxia", "Seoul",
    "Khao Sok", "Cebu", "Chiang Mai", "Ho Chi Minh"
]


# Example 2a: Relational (comparison) operator (==)

msg = "life is beautiful"

if msg == "I love you":
    print("propose")
else:
    print("wait xP")


# Example 2b: Relational (comparison) operator (>=)

net_earnings = 10000000

if net_earnings >= 100000000:
    print("Large Cap")
else:
    print("Small Cap")


# Example 3a: Membership operator (in)

lst = ["soccer", "swimming", "running", "skiing"]

if "rock climbing" not in lst:
    print("boo")

# Example 3b: Membership operator (not in)

web_data = ["techresearch and computervision"]

if "@" in web_data:
    print("e-mail address")
elif "0123456789" in web_data:
    print("phone number")
else:
    print("not e-mail nor phone number")


# Example 4: Arithmetic operator (+, -, *, /, //, **, %)

a = 10 + 20
b = 100 - 1
c = 50 / 7
d = 50 // 7
e = 10 % 8
f = 5 ** 2

print(a, b, c, d, e, f, sep="\n")
