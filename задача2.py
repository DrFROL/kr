f = open('mat_dv.txt', 'r')
alg_max = 0
algebra = {}
geometr_max = 0
geometria = {}
maxium8 = 0
maxium9 = 0
maxium10 = 0
maxium11 = 0
max8 = {}
max9 = {}
max10 = {}
max11 = {}
for i in f:
    a = i.split()
    if a[2] == '8':
        if maxium8 < (int(a[3]) + int(a[4])):
            maxium8 = (int(a[3]) + int(a[4]))
            max8.clear()
            max8[a[0], a[1]] = maxium8
    if a[2] == '9':
        if maxium9 < (int(a[3]) + int(a[4])):
            maxium9 = (int(a[3]) + int(a[4]))
            max9.clear()
            max9[a[0], a[1]] = maxium9
    if a[2] == '10':
        if maxium10 < (int(a[3]) + int(a[4])):
            maxium10 = (int(a[3]) + int(a[4]))
            max10.clear()
            max10[a[0], a[1]] = maxium10
    if a[2] == '11':
        if maxium11 < (int(a[3]) + int(a[4])):
            maxium11 = (int(a[3]) + int(a[4]))
            max11.clear()
            max11[a[0], a[1]] = maxium11

    if int(a[3]) > alg_max:
        alg_max = int(a[3])
        algebra.clear()
        algebra[a[0], a[1]] = a[3]
    elif int(a[3]) == alg_max:
        algebra[a[0], a[1]] = a[3]
    if int(a[4]) > geometr_max:
        geometr_max = int(a[4])
        geometria.clear()
        geometria[a[0], a[1]] = a[4]
    elif int(a[4]) == geometr_max:
        geometria[a[0], a[1]] = a[4]




print(max8)
print(max9)
print(max10)
print(max11)

print(algebra)
print(geometria)
f.close()



