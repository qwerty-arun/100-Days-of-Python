from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

d = Decimal("2.675")

print("Default rounding:", d.quantize(Decimal("0.01")))
print("ROUND_HALF_UP:", d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
print("ROUND_DOWN:", d.quantize(Decimal("0.01"), rounding=ROUND_DOWN))
