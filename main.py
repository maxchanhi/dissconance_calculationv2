import math
f1 = 220
f1SPL = 60
f1b = f1*2
f1bSPL = 50
f1c = f1*3
f1cSPL = 40
f1d = f1*4
f1dSPL = 40
f1e = f1*5
f1eSPL = 30
f1f = f1*6
f1fSPL = 30
f1g = f1*7
f1gSPL = 30

if f1>30 and f1<60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif f1 > 60 and f1 < 80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif f1>80 and f1 < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif f1>125 and f1 < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif f1>200 and f1 <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif f1 > 300 and f1 < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif f1 > 500 and f1 < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif f1 > 800 and f1 < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif f1 > 1200 and f1 < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif f1 > 1500 and f1 < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif f1 > 1800 and f1 < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif f1 > 2200 and f1 < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif f1 > 2900 and f1 < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif f1 > 3500 and f1 < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif f1 > 4500 and f1 < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif f1 > 5500 and f1 < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif f1 > 7500 and f1 < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif f1 > 9000 and f1 < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif f1 > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1SPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1 = 2 ** (0.1 * Phlf2 - 4)
else:
    l1 = 0

if f1b>30 and f1b<60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif f1b > 60 and f1b < 80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif f1b >80 and f1b < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif f1b >125 and f1b < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif f1b >200 and f1b <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif f1b > 300 and f1b < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif f1b > 500 and f1b < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif f1b > 800 and f1b < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif f1b > 1200 and f1b < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif f1b > 1500 and f1b < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif f1b > 1800 and f1b < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif f1b > 2200 and f1b < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif f1b > 2900 and f1b < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif f1b > 3500 and f1b < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif f1b > 4500 and f1b < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif f1b > 5500 and f1b < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif f1b > 7500 and f1b < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif f1b > 9000 and f1b < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif f1b > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1bSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1b = 2 ** (0.1 * Phlf2 - 4)
else:
    l1b = 0

if f1c>30 and f1c<60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif f1c > 60 and f1c < 80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif f1c >80 and f1c < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif f1c >125 and f1c < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif f1c >200 and f1c <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif f1c > 300 and f1c < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif f1c > 500 and f1c < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif f1c > 800 and f1c < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif f1c > 1200 and f1c < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif f1c > 1500 and f1c < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif f1c > 1800 and f1c < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif f1c > 2200 and f1c < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif f1c > 2900 and f1c < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif f1c > 3500 and f1c < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif f1c > 4500 and f1c < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif f1c > 5500 and f1c < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif f1c > 7500 and f1c < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif f1c > 9000 and f1c < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif f1c > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1cSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1c = 2 ** (0.1 * Phlf2 - 4)
else:
    l1c = 0

if f1d>30 and f1d<60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif f1d > 60 and f1d < 80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif f1d >80 and f1d < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif f1d >125 and f1d < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif f1d >200 and f1d <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif f1d > 300 and f1d < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif f1d > 500 and f1d < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif f1d > 800 and f1d < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif f1d > 1200 and f1d < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif f1d > 1500 and f1d < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif f1d > 1800 and f1d < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif f1d > 2200 and f1d < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif f1d > 2900 and f1d < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif f1d > 3500 and f1d < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif f1d > 4500 and f1d < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif f1d > 5500 and f1d < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif f1d > 7500 and f1d < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif f1d > 9000 and f1d < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif f1d > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1dSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1d = 2 ** (0.1 * Phlf2 - 4)
else:
    l1d = 0

freq = f1e
if freq >30 and freq <60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif freq > 60 and freq <80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif freq >80 and freq < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif freq >125 and freq < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif freq >200 and freq <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif freq > 300 and freq < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif freq > 500 and freq < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif freq > 800 and freq < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif freq > 1200 and freq < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif freq > 1500 and freq < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif freq > 1800 and freq < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif freq > 2200 and freq < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif freq > 2900 and freq < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif freq > 3500 and freq < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif freq > 4500 and freq < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif freq > 5500 and freq < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif freq > 7500 and freq < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif freq > 9000 and freq < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif freq > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1eSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1e = 2 ** (0.1 * Phlf2 - 4)
else:
    l1e = 0

freq = f1f
if freq >30 and freq <60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif freq > 60 and freq <80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif freq >80 and freq < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif freq >125 and freq < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif freq >200 and freq <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif freq > 300 and freq < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif freq > 500 and freq < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif freq > 800 and freq < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif freq > 1200 and freq < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif freq > 1500 and freq < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif freq > 1800 and freq < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif freq > 2200 and freq < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif freq > 2900 and freq < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif freq > 3500 and freq < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif freq > 4500 and freq < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif freq > 5500 and freq < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif freq > 7500 and freq < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif freq > 9000 and freq < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif freq > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1fSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1f = 2 ** (0.1 * Phlf2 - 4)
else:
    l1f = 0

freq = f1g
if freq >30 and freq <60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif freq > 60 and freq <80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif freq >80 and freq < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif freq >125 and freq < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif freq >200 and freq <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif freq > 300 and freq < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif freq > 500 and freq < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif freq > 800 and freq < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif freq > 1200 and freq < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif freq > 1500 and freq < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif freq > 1800 and freq < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif freq > 2200 and freq < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif freq > 2900 and freq < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif freq > 3500 and freq < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif freq > 4500 and freq < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif freq > 5500 and freq < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif freq > 7500 and freq < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif freq > 9000 and freq < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif freq > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4 * (10 ** (((f1gSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
if Bf2 > 0:
    Phlf2 = 40 * math.log10(Bf2) + 94
    l1g = 2 ** (0.1 * Phlf2 - 4)
else:
    l1g = 0

for x in [230]:
    f2 = x
    f2b = f2*2
    f2c = f2*3
    f2d = f2*4
    f2e = f2*5
    f2f = f2*6
    f2g = f2*0
    f2SPL = 60
    f2bSPL = 50
    f2cSPL = 40
    f2dSPL = 40
    f2eSPL = 35
    f2fSPL = 30
    f2gSPL = 30
    freq = f2
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2SPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2 = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2 = 0

    freq = f2b
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2bSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2b = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2b = 0

    freq = f2c
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2cSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2c = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2c = 0

    freq = f2d
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2dSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2d = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2d = 0

    freq = f2e
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2eSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2e = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2e = 0

    freq = f2f
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2fSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2f = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2f = 0

    freq = f2g
    if freq > 30 and freq < 60:
        af = 0.432
        Lu = -15.9
        Tf = 44
    elif freq > 60 and freq < 80:
        af = 0.409
        Lu = -13
        Tf = 37.5
    elif freq > 80 and freq < 125:
        af = 0.349
        Lu = -6.2
        Tf = 22.1
    elif freq > 125 and freq < 200:
        af = 0.330
        Lu = -4.5
        Tf = 17.9
    elif freq > 200 and freq < 300:
        af = 0.301
        Lu = -2
        Tf = 11.4
    elif freq > 300 and freq < 500:
        af = 0.276
        Lu = -0.1
        Tf = 6.2
    elif freq > 500 and freq < 800:
        af = 0.259
        Lu = 0.3
        Tf = 3
    elif freq > 800 and freq < 1200:
        af = 0.250
        Lu = 0
        Tf = 2.4
    elif freq > 1200 and freq < 1500:
        af = 0.246
        Lu = -2.7
        Tf = 3.5
    elif freq > 1500 and freq < 1800:
        af = 0.244
        Lu = -4.1
        Tf = 1.7
    elif freq > 1800 and freq < 2200:
        af = 0.243
        Lu = -1
        Tf = -1.3
    elif freq > 2200 and freq < 2900:
        af = 0.243
        Lu = 1.7
        Tf = -4.2
    elif freq > 2900 and freq < 3500:
        af = 0.243
        Lu = 2.5
        Tf = -6
    elif freq > 3500 and freq < 4500:
        af = 0.242
        Lu = 1.2
        Tf = -5.2
    elif freq > 4500 and freq < 5500:
        af = 0.242
        Lu = -2.1
        Tf = -1.5
    elif freq > 5500 and freq < 7500:
        af = 0.245
        Lu = -7.1
        Tf = 6
    elif freq > 7500 and freq < 9000:
        af = 0.245
        Lu = -11.2
        Tf = 12.6
    elif freq > 9000 and freq < 11000:
        af = 0.271
        Lu = -10.7
        Tf = 13.9
    elif freq > 11000:
        af = 0.301
        Lu = -3.1
        Tf = 12.3

    Bf2 = ((0.4 * (10 ** (((f2gSPL + Lu) / 10) - 9))) ** af) - (0.4 * (10 ** (((Tf + Lu) / 10) - 9)) ** af + 0.005135)
    if Bf2 > 0:
        Phlf2 = 40 * math.log10(Bf2) + 94
        l2g = 2 ** (0.1 * Phlf2 - 4)
    else:
        l2g = 0

    minf = min(f1,f2)
    maxf = max(f1,f2)
    s = 0.24/(0.021*minf+19)
    fdiff = maxf-minf
    df1f2l1l2 = l1 * l2 * (math.exp(-3.5 * s * fdiff) - math.exp(-5.75 * s * fdiff))
    minf1b = min(f1b,f2)
    maxf1b = max(f1b,f2)
    s1b = 0.24 / (0.021 * minf1b + 19)
    f1bdiff = maxf1b-minf1b
    df1bf2l1bl2 = l1b * l2 * (math.exp(-3.5 * s1b * f1bdiff) - math.exp(-5.75 * s1b * f1bdiff));
    minf1c = min(f1c, f2)
    maxf1c = max(f1c, f2)
    s1c = 0.24 / (0.021 * minf1c + 19)
    f1cdiff = maxf1c - minf1c
    df1cf2l1cl2 = l1c * l2 * (math.exp(-3.5 * s1c * f1cdiff) - math.exp(-5.75 * s1c * f1cdiff));
    minf1d = min(f1d, f2)
    maxf1d = max(f1d, f2)
    s1d = 0.24 / (0.021 * minf1d + 19)
    f1ddiff = maxf1d - minf1d
    df1df2l1cl2 = l1d * l2 * (math.exp(-3.5 * s1d * f1ddiff) - math.exp(-5.75 * s1d * f1ddiff));
    minf1e = min(f1e, f2)
    maxf1e = max(f1e, f2)
    s1e = 0.24 / (0.021 * minf1e + 19)
    f1ediff = maxf1e - minf1e
    df1ef2l1cl2 = l1e * l2 * (math.exp(-3.5 * s1e * f1ediff) - math.exp(-5.75 * s1e * f1ediff));
    minf1f2b = min(f1, f2b)
    maxf1f2b = max(f1, f2b)
    s12b = 0.24 / (0.021 * minf1f2b + 19)
    f1f2bdiff = maxf1f2b - minf1f2b
    df1f2bl1l2b = l1 * l2b * (math.exp(-3.5 * s12b * f1f2bdiff) - math.exp(-5.75 * s12b * f1f2bdiff))
    minf1bf2b = min(f1b, f2b)
    maxf1bf2b = max(f1b, f2b)
    s1b2b = 0.24 / (0.021 * minf1bf2b + 19)
    f1bf2bdiff = maxf1bf2b - minf1bf2b
    df1bf2bl1bl2b = l1b * l2b * (math.exp(-3.5 * s1b2b * f1bf2bdiff) - math.exp(-5.75 * s1b2b * f1bf2bdiff))
    minf1cf2b = min(f1c, f2b)
    maxf1cf2b = max(f1c, f2b)
    s1c2b = 0.24 / (0.021 * minf1cf2b + 19)
    f1cf2bdiff = maxf1cf2b - minf1cf2b
    df1cf2bl1cl2b = l1c * l2b * (math.exp(-3.5 * s1c2b * f1cf2bdiff) - math.exp(-5.75 * s1c2b * f1cf2bdiff))
    minf1df2b = min(f1d, f2b)
    maxf1df2b = max(f1d, f2b)
    s1d2b = 0.24 / (0.021 * minf1df2b + 19)
    f1df2bdiff = maxf1df2b - minf1df2b
    df1df2bl1dl2b = l1d * l2b * (math.exp(-3.5 * s1d2b * f1df2bdiff) - math.exp(-5.75 * s1d2b * f1df2bdiff))
    minf1ef2b = min(f1e, f2b)
    maxf1ef2b = max(f1e, f2b)
    s1e2b = 0.24 / (0.021 * minf1ef2b + 19)
    f1ef2bdiff = maxf1ef2b - minf1ef2b
    df1ef2bl1el2b = l1e * l2b * (math.exp(-3.5 * s1e2b * f1ef2bdiff) - math.exp(-5.75 * s1e2b * f1ef2bdiff))
    minf1f2c = min(f1, f2c)
    maxf1f2c = max(f1, f2c)
    s12c = 0.24 / (0.021 * minf1f2c + 19)
    f1f2cdiff = maxf1f2c - minf1f2c
    df1f2cl1l2c = l1 * l2c * (math.exp(-3.5 * s12c * f1f2cdiff) - math.exp(-5.75 * s12c * f1f2cdiff))
    minf1bf2c = min(f1b, f2c)
    maxf1bf2c = max(f1b, f2c)
    s1b2c = 0.24 / (0.021 * minf1bf2c + 19)
    f1bf2cdiff = maxf1bf2c - minf1bf2c
    df1bf2cl1bl2c = l1b * l2c * (math.exp(-3.5 * s1b2c * f1bf2cdiff) - math.exp(-5.75 * s1b2c * f1bf2cdiff))
    minf1cf2c = min(f1c, f2c)
    maxf1cf2c = max(f1c, f2c)
    s1c2c = 0.24 / (0.021 * minf1cf2c + 19)
    f1cf2cdiff = maxf1cf2c - minf1cf2c
    df1cf2cl1cl2c = l1c * l2c * (math.exp(-3.5 * s1c2c * f1cf2cdiff) - math.exp(-5.75 * s1c2c * f1cf2cdiff))
    minf1df2c = min(f1d, f2c)
    maxf1df2c = max(f1d, f2c)
    s1d2c = 0.24 / (0.021 * minf1df2c + 19)
    f1df2cdiff = maxf1df2c - minf1df2c
    df1df2cl1dl2c = l1d * l2c * (math.exp(-3.5 * s1d2c * f1df2cdiff) - math.exp(-5.75 * s1d2c * f1df2cdiff))
    minf1ef2c = min(f1e, f2c)
    maxf1ef2c = max(f1e, f2c)
    s1e2c = 0.24 / (0.021 * minf1ef2c + 19)
    f1ef2cdiff = maxf1ef2c - minf1ef2c
    df1ef2cl1el2c = l1e * l2c * (math.exp(-3.5 * s1e2c * f1ef2cdiff) - math.exp(-5.75 * s1e2c * f1ef2cdiff))
    minf1f2d = min(f1, f2d)
    maxf1f2d = max(f1, f2d)
    s12d = 0.24 / (0.021 * minf1f2d + 19)
    f1f2ddiff = maxf1f2d - minf1f2d
    df1f2dl1l2d = l1 * l2d * (math.exp(-3.5 * s12d * f1f2ddiff) - math.exp(-5.75 * s12d * f1f2ddiff))
    minf1bf2d = min(f1b, f2d)
    maxf1bf2d = max(f1b, f2d)
    s1b2d = 0.24 / (0.021 * minf1bf2d + 19)
    f1bf2ddiff = maxf1bf2d - minf1bf2d
    df1bf2dl1bl2d = l1b * l2d * (math.exp(-3.5 * s1b2d * f1bf2ddiff) - math.exp(-5.75 * s1b2d * f1bf2ddiff))
    minf1cf2d = min(f1c, f2d)
    maxf1cf2d = max(f1c, f2d)
    s1c2d = 0.24 / (0.021 * minf1cf2d + 19)
    f1cf2ddiff = maxf1cf2d - minf1cf2d
    df1cf2dl1cl2d = l1c * l2d * (math.exp(-3.5 * s1c2d * f1cf2ddiff) - math.exp(-5.75 * s1c2d * f1cf2ddiff))
    minf1df2d = min(f1d, f2d)
    maxf1df2d = max(f1d, f2d)
    s1d2d = 0.24 / (0.021 * minf1df2d + 19)
    f1df2ddiff = maxf1df2d - minf1df2d
    df1df2dl1dl2d = l1d * l2d * (math.exp(-3.5 * s1d2d * f1df2ddiff) - math.exp(-5.75 * s1d2d * f1df2ddiff))
    minf1ef2d = min(f1e, f2d)
    maxf1ef2d = max(f1e, f2d)
    s1e2d = 0.24 / (0.021 * minf1ef2d + 19)
    f1ef2ddiff = maxf1ef2d - minf1ef2d
    df1ef2dl1el2d = l1e * l2d * (math.exp(-3.5 * s1e2d * f1ef2ddiff) - math.exp(-5.75 * s1e2d * f1ef2ddiff))
    minf1f2e = min(f1, f2e)
    maxf1f2e = max(f1, f2e)
    s12e = 0.24 / (0.021 * minf1f2e + 19)
    f1f2ediff = maxf1f2e - minf1f2e
    df1f2el1l2e = l1 * l2e * (math.exp(-3.5 * s12e * f1f2ediff) - math.exp(-5.75 * s12e * f1f2ediff))
    minf1bf2e = min(f1b, f2e)
    maxf1bf2e = max(f1b, f2e)
    s1b2e = 0.24 / (0.021 * minf1bf2e + 19)
    f1bf2ediff = maxf1bf2e - minf1bf2e
    df1bf2el1bl2e = l1b * l2e * (math.exp(-3.5 * s1b2e * f1bf2ediff) - math.exp(-5.75 * s1b2e * f1bf2ediff))
    minf1cf2e = min(f1c, f2e)
    maxf1cf2e = max(f1c, f2e)
    s1c2e = 0.24 / (0.021 * minf1cf2e + 19)
    f1cf2ediff = maxf1cf2e - minf1cf2e
    df1cf2el1cl2e = l1c * l2e * (math.exp(-3.5 * s1c2e * f1cf2ediff) - math.exp(-5.75 * s1c2e * f1cf2ediff))
    minf1df2e = min(f1d, f2e)
    maxf1df2e = max(f1d, f2e)
    s1d2e = 0.24 / (0.021 * minf1df2e + 19)
    f1df2ediff = maxf1df2e - minf1df2e
    df1df2el1dl2e = l1d * l2e * (math.exp(-3.5 * s1d2e * f1df2ediff) - math.exp(-5.75 * s1d2e * f1df2ediff))
    minf1ef2e = min(f1e, f2e)
    maxf1ef2e = max(f1e, f2e)
    s1e2e = 0.24 / (0.021 * minf1ef2e + 19)
    f1ef2ediff = maxf1ef2e - minf1ef2e
    df1ef2el1dl2e = l1e * l2e * (math.exp(-3.5 * s1e2e * f1ef2ediff) - math.exp(-5.75 * s1e2e * f1ef2ediff))
    minf1ff2 = min(f1f, f2)
    maxf1ff2 = max(f1f, f2)
    s1f2 = 0.24 / (0.021 * minf1ff2 + 19)
    f1ff2diff = maxf1ff2 - minf1ff2
    df1ff2l1fl2 = l1f * l2 * (math.exp(-3.5 * s1f2 * f1ff2diff) - math.exp(-5.75 * s1f2 * f1ff2diff))
    minf1ff2b = min(f1f, f2b)
    maxf1ff2b = max(f1f, f2b)
    s1f2b = 0.24 / (0.021 * minf1ff2b + 19)
    f1ff2biff = maxf1ff2b - minf1ff2b
    df1ff2bl1fl2b = l1f * l2b * (math.exp(-3.5 * s1f2b * f1ff2biff) - math.exp(-5.75 * s1f2b * f1ff2biff))
    minf1ff2c = min(f1f, f2c)
    maxf1ff2c = max(f1f, f2c)
    s1f2c = 0.24 / (0.021 * minf1ff2c + 19)
    f1ff2ciff = maxf1ff2c - minf1ff2c
    df1ff2cl1fl2c = l1f * l2c * (math.exp(-3.5 * s1f2c * f1ff2ciff) - math.exp(-5.75 * s1f2c * f1ff2ciff))
    minf1ff2d = min(f1f, f2d)
    maxf1ff2d = max(f1f, f2d)
    s1f2d = 0.24 / (0.021 * minf1ff2d + 19)
    f1ff2diff = maxf1ff2d - minf1ff2d
    df1ff2dl1fl2d = l1f * l2d * (math.exp(-3.5 * s1f2d * f1ff2diff) - math.exp(-5.75 * s1f2d * f1ff2diff))
    minf1ff2e = min(f1f, f2e)
    maxf1ff2e = max(f1f, f2e)
    s1f2e = 0.24 / (0.021 * minf1ff2e + 19)
    f1ff2eiff = maxf1ff2e - minf1ff2e
    df1ff2el1fl2e = l1f * l2e * (math.exp(-3.5 * s1f2e * f1ff2eiff) - math.exp(-5.75 * s1f2e * f1ff2eiff))
    minf1f2f = min(f1, f2f)
    maxf1f2f = max(f1, f2f)
    s1f2f = 0.24 / (0.021 * minf1f2f + 19)
    f1f2fiff = maxf1f2f - minf1f2f
    df1f2fl1l2f = l1 * l2f * (math.exp(-3.5 * s1f2f * f1f2fiff) - math.exp(-5.75 * s1f2f * f1f2fiff))
    minf1bf2f = min(f1b, f2f)
    maxf1bf2f = max(f1b, f2f)
    s1bf2f = 0.24 / (0.021 * minf1bf2f + 19)
    f1bf2fiff = maxf1bf2f - minf1bf2f
    df1fb2fl1bl2f = l1b * l2f * (math.exp(-3.5 * s1bf2f * f1bf2fiff) - math.exp(-5.75 * s1bf2f * f1bf2fiff))
    minf1cf2f = min(f1c, f2f)
    maxf1cf2f = max(f1c, f2f)
    s1cf2f = 0.24 / (0.021 * minf1cf2f + 19)
    f1cf2fiff = maxf1cf2f - minf1cf2f
    df1fc2fl1cl2f = l1c * l2f * (math.exp(-3.5 * s1cf2f * f1cf2fiff) - math.exp(-5.75 * s1cf2f * f1cf2fiff))
    minf1df2f = min(f1d, f2f)
    maxf1df2f = max(f1d, f2f)
    s1df2f = 0.24 / (0.021 * minf1df2f + 19)
    f1df2fiff = maxf1df2f - minf1df2f
    df1fd2fl1dl2f = l1d * l2f * (math.exp(-3.5 * s1df2f * f1df2fiff) - math.exp(-5.75 * s1df2f * f1df2fiff))
    minf1ef2f = min(f1e, f2f)
    maxf1ef2f = max(f1e, f2f)
    s1ef2f = 0.24 / (0.021 * minf1ef2f + 19)
    f1ef2fiff = maxf1ef2f - minf1ef2f
    df1ed2fl1el2f = l1e * l2f * (math.exp(-3.5 * s1ef2f * f1ef2fiff) - math.exp(-5.75 * s1ef2f * f1ef2fiff))
    minf1ff2f = min(f1f, f2f)
    maxf1ff2f = max(f1f, f2f)
    s1ff2f = 0.24 / (0.021 * minf1ff2f + 19)
    f1ff2fiff = maxf1ff2f - minf1ff2f
    df1fd2fl1fl2f = l1f * l2f * (math.exp(-3.5 * s1ff2f * f1ff2fiff) - math.exp(-5.75 * s1ff2f * f1ff2fiff))
    minf1f2g = min(f1, f2g)
    maxf1f2g = max(f1, f2g)
    s1f2g = 0.24 / (0.021 * minf1f2g + 19)
    f1f2gfiff = maxf1f2g - minf1f2g
    df1df2gl1l2g = l1 * l2g * (math.exp(-3.5 * s1f2g * f1f2gfiff) - math.exp(-5.75 * s1f2g * f1f2gfiff))
    minf1bf2g = min(f1b, f2g)
    maxf1bf2g = max(f1b, f2g)
    s1bf2g = 0.24 / (0.021 * minf1bf2g + 19)
    f1bf2gfiff = maxf1bf2g - minf1bf2g
    df1bdf2gl1bl2g = l1b * l2g * (math.exp(-3.5 * s1bf2g * f1bf2gfiff) - math.exp(-5.75 * s1bf2g * f1bf2gfiff))
    minf1cf2g = min(f1c, f2g)
    maxf1cf2g = max(f1c, f2g)
    s1cf2g = 0.24 / (0.021 * minf1cf2g + 19)
    f1cf2gfiff = maxf1cf2g - minf1cf2g
    df1cdf2gl1cl2g = l1c * l2g * (math.exp(-3.5 * s1cf2g * f1cf2gfiff) - math.exp(-5.75 * s1cf2g * f1cf2gfiff))
    minf1df2g = min(f1d, f2g)
    maxf1df2g = max(f1d, f2g)
    s1df2g = 0.24 / (0.021 * minf1df2g + 19)
    f1df2gfiff = maxf1df2g - minf1df2g
    df1ddf2gl1dl2g = l1d * l2g * (math.exp(-3.5 * s1df2g * f1df2gfiff) - math.exp(-5.75 * s1df2g * f1df2gfiff))
    minf1ef2g = min(f1e, f2g)
    maxf1ef2g = max(f1e, f2g)
    s1ef2g = 0.24 / (0.021 * minf1ef2g + 19)
    f1ef2gfiff = maxf1ef2g - minf1ef2g
    df1edf2gl1dl2g = l1e * l2g * (math.exp(-3.5 * s1ef2g * f1ef2gfiff) - math.exp(-5.75 * s1ef2g * f1ef2gfiff))
    minf1ff2g = min(f1f, f2g)
    maxf1ff2g = max(f1f, f2g)
    s1ff2g = 0.24 / (0.021 * minf1ff2g + 19)
    f1ff2gfiff = maxf1ff2g - minf1ff2g
    df1fdf2gl1fl2g = l1f * l2g * (math.exp(-3.5 * s1ff2g * f1ff2gfiff) - math.exp(-5.75 * s1ff2g * f1ff2gfiff))
    minf1gf2g = min(f1g, f2g)
    maxf1gf2g = max(f1g, f2g)
    s1gf2g = 0.24 / (0.021 * minf1gf2g + 19)
    f1gf2gfiff = maxf1gf2g - minf1gf2g
    df1gdf2gl1gl2g = l1g * l2g * (math.exp(-3.5 * s1gf2g * f1gf2gfiff) - math.exp(-5.75 * s1gf2g * f1gf2gfiff))
    minf1gf2f = min(f1g, f2f)
    maxf1gf2f = max(f1g, f2f)
    s1gf2f = 0.24 / (0.021 * minf1gf2f + 19)
    f1gf2ffiff = maxf1gf2f - minf1gf2f
    df1gdf2fl1gl2f = l1g * l2f * (math.exp(-3.5 * s1gf2f * f1gf2ffiff) - math.exp(-5.75 * s1gf2f * f1gf2ffiff))
    minf1gf2e = min(f1g, f2e)
    maxf1gf2e = max(f1g, f2e)
    s1gf2e = 0.24 / (0.021 * minf1gf2e + 19)
    f1gf2efiff = maxf1gf2e - minf1gf2e
    df1gdf2el1gl2e = l1g * l2e * (math.exp(-3.5 * s1gf2e * f1gf2efiff) - math.exp(-5.75 * s1gf2e * f1gf2efiff))
    minf1gf2d = min(f1g, f2d)
    maxf1gf2d = max(f1g, f2d)
    s1gf2d = 0.24 / (0.021 * minf1gf2d + 19)
    f1gf2dfiff = maxf1gf2d - minf1gf2d
    df1gdf2dl1gl2d = l1g * l2d * (math.exp(-3.5 * s1gf2d * f1gf2dfiff) - math.exp(-5.75 * s1gf2d * f1gf2dfiff))
    minf1gf2c = min(f1g, f2c)
    maxf1gf2c = max(f1g, f2c)
    s1gf2c = 0.24 / (0.021 * minf1gf2c + 19)
    f1gf2cfiff = maxf1gf2c - minf1gf2c
    df1gdf2cl1gl2c = l1d * l2c * (math.exp(-3.5 * s1gf2c * f1gf2cfiff) - math.exp(-5.75 * s1gf2c * f1gf2cfiff))
    minf1gf2b = min(f1g, f2b)
    maxf1gf2b = max(f1g, f2b)
    s1gf2b = 0.24 / (0.021 * minf1gf2b + 19)
    f1gf2bfiff = maxf1gf2b - minf1gf2b
    df1gdf2bl1gl2b = l1d * l2b * (math.exp(-3.5 * s1gf2b * f1gf2bfiff) - math.exp(-5.75 * s1gf2b * f1gf2bfiff))
    minf1gf2 = min(f1g, f2)
    maxf1gf2 = max(f1g, f2)
    s1gf2 = 0.24 / (0.021 * minf1gf2 + 19)
    f1gf2fiff = maxf1gf2 - minf1gf2
    df1gdf2l1gl2 = l1d * l2 * (math.exp(-3.5 * s1gf2 * f1gf2fiff) - math.exp(-5.75 * s1gf2 * f1gf2fiff))

    sum = (df1gdf2l1gl2+df1gdf2bl1gl2b+df1gdf2cl1gl2c+df1gdf2dl1gl2d+df1gdf2el1gl2e+df1gdf2fl1gl2f+df1gdf2gl1gl2g+df1fdf2gl1fl2g+df1edf2gl1dl2g+df1ddf2gl1dl2g+df1cdf2gl1cl2g+df1bdf2gl1bl2g+df1df2gl1l2g+df1fd2fl1fl2f+df1ed2fl1el2f+df1fd2fl1dl2f+df1fc2fl1cl2f+df1fb2fl1bl2f+df1ff2el1fl2e+df1ff2dl1fl2d+df1ff2cl1fl2c+df1ff2bl1fl2b+df1ff2l1fl2+
           df1f2l1l2+df1bf2l1bl2+df1cf2l1cl2+df1df2l1cl2+df1ef2l1cl2+df1f2bl1l2b+df1bf2bl1bl2b+df1cf2bl1cl2b+df1df2bl1dl2b+df1ef2bl1el2b+df1f2cl1l2c+df1bf2cl1bl2c+df1cf2cl1cl2c+df1df2cl1dl2c+df1ef2cl1el2c+df1f2dl1l2d+df1bf2dl1bl2d+df1cf2dl1cl2d+df1df2dl1dl2d+df1ef2dl1el2d+df1f2el1l2e+df1bf2el1bl2e+df1cf2el1cl2e+df1df2el1dl2e+df1ef2el1dl2e)
    print(sum)
pass
