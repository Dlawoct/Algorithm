unit = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
rate = [4.5, 4.0, 3.5, 3.0,2.5,2.0,1.5,1.0,0.0]

rm = 0
al = 0

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        rm += b
        al += b * rate[unit.index(c)]
print('%.6f' %(al/rm))
      