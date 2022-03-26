f1 = 220
f2 = 233
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
import math
for n in [f1, f1b, f1c, f1d, f1e]:
    for m in [f2, f2b, f2c, f2d, f2e]:
        minf = min(m, n)
        maxf = max(m, n)
        fDiff = maxf-minf
        s = 0.24/(0.021*minf+19)
        diss = math.exp(-3.5 * s * fDiff) - math.exp(-5.75 * s * fDiff)
        for loudf1 in [l1, l1b, l1b, l1c, l1d, l1e]:
            for loudf2 in [l2, l2b, l2c, l2d, l2e]:
                combloud = loudf2 * loudf1
                indieDiss = combloud * diss


            pass
        f = open('cal.txt', 'w')
        indieDiss = "{indieDiss}\n"
        print(indieDiss, end="")
        f.close()
        print(indieDiss)

        pass
    pass
pass






