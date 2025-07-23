# Using Dictionaries instead of repeated case

# This is a list of dictionaries
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 18, "coupon": "P50"}
]

# discount in %, flat off
discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0)) # (0,0) is the default value
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount: {discount}")