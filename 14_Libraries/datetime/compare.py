from datetime import date

d1 = date(2025, 8, 16)
d2 = date(2026, 1, 1)

if d1 < d2:
    print(f"{d1} comes before {d2}")
else:
    print(f"{d1} comes after {d2}")