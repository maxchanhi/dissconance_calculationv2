import math
f2cal = []
f2cal = input("Enter the fundamental frequencies: ")
f = f2cal.split()
g = 0
result = []
while g < int(len(f)-1):
    f1 = f[g]
    f1SPL = 70
    f1b = float(f1)*2
    f1bSPL = 69.2
    f1c = float(f1)*3
    f1cSPL = 66.7
    f1d = float(f1)*4
    f1dSPL = 57.4
    f1e = float(f1)*5
    f1eSPL = 58.6
    f1f = float(f1)*6
    f1fSPL = 46.1
    f1g = float(f1)*7
    f1gSPL = 0
    f1row = [f1,f1b,f1c,f1d,f1e,f1f,f1g]
    SPLrow = [f1SPL,f1bSPL,f1cSPL,f1dSPL,f1eSPL,f1fSPL,f1gSPL]
    i = 0
    f1rowloudness = []
    o = 0
    while o < 7:
        freq = float(f1row[o])
        if freq > 30 and freq <= 60:
            af = 0.432
            Lu = -15.9
            Tf = 44
        elif freq > 60 and freq <= 80:
            af = 0.409
            Lu = -13
            Tf = 37.5
        elif freq > 80 and freq <= 125:
            af = 0.349
            Lu = -6.2
            Tf = 22.1
        elif freq > 125 and freq <= 200:
            af = 0.330
            Lu = -4.5
            Tf = 17.9
        elif freq > 200 and freq <= 300:
            af = 0.301
            Lu = -2
            Tf = 11.4
        elif freq > 300 and freq <= 500:
            af = 0.276
            Lu = -0.1
            Tf = 6.2
        elif freq > 500 and freq <= 800:
            af = 0.259
            Lu = 0.3
            Tf = 3
        elif freq > 800 and freq <= 1200:
            af = 0.250
            Lu = 0
            Tf = 2.4
        elif freq > 1200 and freq <= 1500:
            af = 0.246
            Lu = -2.7
            Tf = 3.5
        elif freq > 1500 and freq <= 1800:
            af = 0.244
            Lu = -4.1
            Tf = 1.7
        elif freq > 1800 and freq <= 2200:
            af = 0.243
            Lu = -1
            Tf = -1.3
        elif freq > 2200 and freq <= 2900:
            af = 0.243
            Lu = 1.7
            Tf = -4.2
        elif freq > 2900 and freq <= 3500:
            af = 0.243
            Lu = 2.5
            Tf = -6
        elif freq > 3500 and freq <= 4500:
            af = 0.242
            Lu = 1.2
            Tf = -5.2
        elif freq > 4500 and freq <= 5500:
            af = 0.242
            Lu = -2.1
            Tf = -1.5
        elif freq > 5500 and freq <= 7500:
            af = 0.245
            Lu = -7.1
            Tf = 6
        elif freq > 7500 and freq <= 9000:
            af = 0.245
            Lu = -11.2
            Tf = 12.6
        elif freq > 9000 and freq <= 11000:
            af = 0.271
            Lu = -10.7
            Tf = 13.9
        elif freq > 11000:
            af = 0.301
            Lu = -3.1
            Tf = 12.3

        Bf2 = ((0.4 * (10 ** (((SPLrow[i] + Lu) / 10) - 9))) ** af) - (
            0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
        if Bf2 > 0:
            Phlf2 = 40 * math.log10(Bf2) + 94
            lf1row = 2 ** (0.1 * Phlf2 - 4)
        else:
            lf1row = 0
        f1rowloudness.append(lf1row)
        i += 1
        o += 1
    f2 = f[g+1]
    f2b = float(f2)*2
    f2c = float(f2)*3
    f2d = float(f2)*4
    f2e = float(f2)*5
    f2f = float(f2)* 6
    f2g = float(f2)* 7
    f2SPL = 70
    f2bSPL = 69.2
    f2cSPL = 66.7
    f2dSPL = 57.4
    f2eSPL = 58.6
    f2fSPL = 46.1
    f2gSPL = 0
    f2rowloudness = []
    f2frequency = [f2,f2b,f2c,f2d,f2e,f2f,f2g]
    SPLf2row = [f2SPL, f2bSPL, f2cSPL, f2dSPL, f2eSPL, f2fSPL, f2gSPL]
    i = 0
    while i < 7:
        freq = f2frequency[i]
        freq = float(freq)
        if freq > 30 and freq <= 60:
            af = 0.432
            Lu = -15.9
            Tf = 44
        elif freq > 60 and freq <= 80:
            af = 0.409
            Lu = -13
            Tf = 37.5
        elif freq > 80 and freq <= 125:
            af = 0.349
            Lu = -6.2
            Tf = 22.1
        elif freq > 125 and freq <= 200:
            af = 0.330
            Lu = -4.5
            Tf = 17.9
        elif freq > 200 and freq <= 300:
            af = 0.301
            Lu = -2
            Tf = 11.4
        elif freq > 300 and freq <= 500:
            af = 0.276
            Lu = -0.1
            Tf = 6.2
        elif freq > 500 and freq <= 800:
            af = 0.259
            Lu = 0.3
            Tf = 3
        elif freq > 800 and freq <= 1200:
            af = 0.250
            Lu = 0
            Tf = 2.4
        elif freq > 1200 and freq <= 1500:
            af = 0.246
            Lu = -2.7
            Tf = 3.5
        elif freq > 1500 and freq <= 1800:
            af = 0.244
            Lu = -4.1
            Tf = 1.7
        elif freq > 1800 and freq <= 2200:
            af = 0.243
            Lu = -1
            Tf = -1.3
        elif freq > 2200 and freq <= 2900:
            af = 0.243
            Lu = 1.7
            Tf = -4.2
        elif freq > 2900 and freq <= 3500:
            af = 0.243
            Lu = 2.5
            Tf = -6
        elif freq > 3500 and freq <= 4500:
            af = 0.242
            Lu = 1.2
            Tf = -5.2
        elif freq > 4500 and freq <= 5500:
            af = 0.242
            Lu = -2.1
            Tf = -1.5
        elif freq > 5500 and freq <= 7500:
            af = 0.245
            Lu = -7.1
            Tf = 6
        elif freq > 7500 and freq <= 9000:
            af = 0.245
            Lu = -11.2
            Tf = 12.6
        elif freq > 9000 and freq <= 11000:
            af = 0.271
            Lu = -10.7
            Tf = 13.9
        elif freq > 11000:
            af = 0.301
            Lu = -3.1
            Tf = 12.3

        Bf2 = ((0.4 * (10 ** (((SPLf2row[i] + Lu) / 10) - 9))) ** af) - (
            0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
        if Bf2 > 0:
            Phlf2 = 40 * math.log10(Bf2) + 94
            lf1row = 2 ** (0.1 * Phlf2 - 4)
        else:
            lf1row = 0
        f2rowloudness.append(lf1row)
        i += 1
    r = 0
    f2result = []
    while r <= 6:
        minf = min(float(f1row[r]), float(f2frequency[0]))
        maxf = max(float(f1row[r]), float(f2frequency[0]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2rowloudnessdiss = f2rowloudness[0] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2result.append(f2rowloudnessdiss)
        r += 1
    r = 0
    f2bresult = []
    while r <= 6:
        minf = min(float(f1row[r]), float(f2frequency[1]))
        maxf = max(float(f1row[r]), float(f2frequency[1]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2browloudnessdiss = f2rowloudness[1] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2bresult.append(f2browloudnessdiss)
        r += 1
    r = 0
    f2cresult = []
    while r < 7:
        f1r = f1row[r]
        minf = min(float(f1row[r]), float(f2frequency[2]))
        maxf = max(float(f1row[r]), float(f2frequency[2]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2crowloudnessdiss = f2rowloudness[2] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2bresult.append(f2crowloudnessdiss)
        r += 1
    r = 0
    f2dresult = []
    while r < 7:
        minf = min(float(f1row[r]), float(f2frequency[3]))
        maxf = max(float(f1row[r]), float(f2frequency[3]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2drowloudnessdiss = f2rowloudness[3] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2dresult.append(f2drowloudnessdiss)
        r += 1
    r = 0
    f2eresult = []
    while r < 7:
        minf = min(float(f1row[r]), float(f2frequency[4]))
        maxf = max(float(f1row[r]), float(f2frequency[4]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2erowloudnessdiss = f2rowloudness[4] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2eresult.append(f2erowloudnessdiss)
        r += 1
    r = 0
    f2fresult = []
    while r < 7:
        minf = min(float(f1row[r]), float(f2frequency[5]))
        maxf = max(float(f1row[r]), float(f2frequency[5]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2frowloudnessdiss = f2rowloudness[5] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2fresult.append(f2frowloudnessdiss)
        r += 1
    r = 0
    f2gresult = []
    while r < 7:
        minf = min(float(f1row[r]), float(f2frequency[6]))
        maxf = max(float(f1row[r]), float(f2frequency[6]))
        s = 0.24 / (0.021 * minf + 19)
        fdiff = maxf - minf
        f2growloudnessdiss = f2rowloudness[6] * f1rowloudness[r] * (
                    math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
        f2gresult.append(f2growloudnessdiss)
        r += 1
    summed = sum(f2result) + sum(f2bresult) + sum(f2cresult) + sum(f2dresult) + sum(f2eresult) + sum(
        f2fresult) + sum(f2gresult)
    print(summed)
    result.append(summed)
    r = 0
    g += 1
print("Total dissonant:",sum(result))
