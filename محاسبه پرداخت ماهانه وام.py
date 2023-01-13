# Morteza Lashgari
# Class : Sunday, 10:10


def loan_Interest ():
    P = float(input("Please Enter Loan Amount:"))
    N = int(input("Please Enter Number of Installments:"))
    R = float(input("Please Enter Annual Interest Rate:"))

    if R == 0:
        Monthly_Payment = P / N
        print ('Your Monthly Payment Is :', Monthly_Payment)
        
    else:
     Monthly_Payment = (P + (P*R / 100)) / N
     print ('Your Monthly Payment Is :', Monthly_Payment)


loan_Interest ()    
