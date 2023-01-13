# Morteza Lashgari
# Class : Sunday , 10:10

def loan_Interest():
    P = float(input("Please Enter Loan Amount:"))
    N = int(input("Please Enter Duration:"))
    R = float(input("Please Enter Annual Interest Rate:"))

    N = (N * 12)
    R = (R / 100) / 12

    if R == 0:
        Monthly_Payment = P / N
        print ('Your Monthly Payment Is :', Monthly_Payment)
        
    else:
     Monthly_Payment = (P*(R*(1+R)**N)) / ((1+R)**N - 1)
     print ('Your Monthly Payment Is :', Monthly_Payment)


loan_Interest()    
