import math

for f1 in [281.3,538.5,880,1290,1761,2284]:
    for f1SPL in [42.3, 43.4, 55.3, 60, 57.4, 48]:

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

            i = 1
            i += 1
            if i == 1 or i == 7 or i == 13 or i == 20 or i == 27 or i == 34:
                Bf1 = ((0.4*(10**(((f1SPL+Lu)/10)-9)))**af)-(0.4*(10**(((Tf+Lu)/10)-9))**af+0.005135)
                Phlf1 = 40*math.log10(Bf1)+94
                lf1 = 2**(0.1*Phlf1-4)

            else:
                continue


    pass
pass

f2 = 2284
f2SPL =48

if f2>30 and f2<60:
    af = 0.432
    Lu = -15.9
    Tf = 44
elif f2 > 60 and f2 < 80:
    af = 0.409
    Lu = -13
    Tf = 37.5
elif f2>80 and f2 < 125:
    af = 0.349
    Lu = -6.2
    Tf = 22.1
elif f2>125 and f2 < 200:
    af = 0.330
    Lu = -4.5
    Tf = 17.9
elif f2>200 and f2 <300:
    af = 0.301
    Lu = -2
    Tf = 11.4
elif f2 > 300 and f2 < 500:
    af = 0.276
    Lu = -0.1
    Tf = 6.2
elif f2 > 500 and f2 < 800:
    af = 0.259
    Lu = 0.3
    Tf = 3
elif f2 > 800 and f2 < 1200:
    af = 0.250
    Lu = 0
    Tf = 2.4
elif f2 > 1200 and f2 < 1500:
    af = 0.246
    Lu = -2.7
    Tf = 3.5
elif f2 > 1500 and f2 < 1800:
    af = 0.244
    Lu = -4.1
    Tf = 1.7
elif f2 > 1800 and f2 < 2200:
    af = 0.243
    Lu = -1
    Tf = -1.3
elif f2 > 2200 and f2 < 2900:
    af = 0.243
    Lu = 1.7
    Tf = -4.2
elif f2 > 2900 and f2 < 3500:
    af = 0.243
    Lu = 2.5
    Tf = -6
elif f2 > 3500 and f2 < 4500:
    af = 0.242
    Lu = 1.2
    Tf = -5.2
elif f2 > 4500 and f2 < 5500:
    af = 0.242
    Lu = -2.1
    Tf = -1.5
elif f2 > 5500 and f2 < 7500:
    af = 0.245
    Lu = -7.1
    Tf = 6
elif f2 > 7500 and f2 < 9000:
    af = 0.245
    Lu = -11.2
    Tf = 12.6
elif f2 > 9000 and f2 < 11000:
    af = 0.271
    Lu = -10.7
    Tf = 13.9
elif f2 > 11000:
    af = 0.301
    Lu = -3.1
    Tf = 12.3

Bf2 = ((0.4*(10**(((f2SPL+Lu)/10)-9)))**af)-(0.4*(10**(((Tf+Lu)/10)-9))**af+0.005135)
Phlf2 = 40*math.log10(Bf2)+94
lf2 = 2**(0.1*Phlf2-4)
print(lf2)
