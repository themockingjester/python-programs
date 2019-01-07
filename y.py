# program of atm
amount=int(input("enter amount"))
n=amount
t=n//2000 #number of 2000 rupee notes
n=n%2000
f=n//500  #number of 500 rupee notes
n=n%500
o=n//100  #number of 100 rupee notes
print("num ber of 2000,500,100 = ",t,f,o)

