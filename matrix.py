import math
f1 = 220
f2 = 230
l1 = 64
l2 = 64
l1b = 50
l2b = 50
l1c = 40
l2c = 40
l1d = 30
l2d = 30
l1e = 20
l2e = 20
f1b = f1*2
f2b = f2*2
f1c = f1*3
f2c = f2*3
f1d = f1*4
f2d = f2*4
f1e = f1*5
f2e = f2*5
for n in [f1, f1b, f1c, f1d, f1e]:
    maxf2c = max(n, f2c)
    minf2c = min(n, f2c)
    s = 0.24 / (0.021 * minf2c + 19)
    f2cDiff = maxf2c-minf2c
    f2cRow = math.exp(-3.5 * s * f2cDiff) - math.exp(-5.75 * s * f2cDiff)

    for loudc in [l1, l1b, l1c, l1d, l1e]:
        f2cRowDiss1 = l1 * l2c * f2cRow
        f2cRowDissb = l1b * l2c * f2cRow
        f2cRowDissc = l1c * l2c * f2cRow
        f2cRowDissd = l1d * l2c * f2cRow
        f2cRowDisse = l1e * l2c * f2cRow
    pass
pass
print(f2cRowDiss1+f2cRowDissb+f2cRowDissc+f2cRowDissd+f2cRowDisse)