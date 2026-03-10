a,b,c,d= map(float, input().split())
tong= (d*3 + c*2 +a +b) /7
if tong >=8:
    print('GIOI')
elif tong < 8 and tong >= 6.5:
    print('KHA')
elif tong <6.5 and tong >=5:
    print('TRUNG BINH')
else :
    print("YEU")