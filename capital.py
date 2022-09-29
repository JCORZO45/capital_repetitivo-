c=int(input("\n Dame el valor del capital: "))
mes=0
n=2*c
while(c<n):
    c=(c*5/100)+c
    mes=mes+1 
    

print("su capital se duplicara en : "+str(mes) + "  meses")