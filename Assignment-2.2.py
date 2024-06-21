import datetime

def get_date(date_string):
    day, month, year = map(int, date_string.split('-'))
    date = datetime.date(year, month, day)
    return date

def newtons(f, derf, x):
    iterations = 0
    while iterations < 10:
        x = x - f(x) / derf(x)
        iterations += 1
    return x


face_value = float(input('Enter the face value of bond: '))
coupon_rate = float(input('Enter the coupon rate per annum(in percentage): '))
coupon_frequency = float(input('Enter the frequency: '))
dirty_price = float(input('Enter Gross(Dirty) price: '))

coupon_value = face_value * coupon_rate / coupon_frequency / 100

maturity_date = get_date(input('Enter the maturity date in the form DD-MM-YYYY: '))
recent_coupon_date = get_date(input('Enter the recent past coupon payment date in the form DD-MM-YYYY: '))
next_coupon_date = get_date(input('Enter the next coupon payment date in the form DD-MM-YYYY: '))
current_date = get_date(input('Enter the current date in the form DD-MM-YYYY: '))

AI = ((current_date - recent_coupon_date).days) / (next_coupon_date - recent_coupon_date).days * coupon_value
clean_price = dirty_price - AI

n = int(((maturity_date - current_date).days) // (365 / coupon_frequency)) + 1

def function(x):
    func = face_value * (x ** n) - clean_price
    for i in range(1, n + 1):
        func += coupon_value * (x ** i)
    return func

def derf(x):
    h = 1e-6
    der = (function(x + h) - function(x)) / h
    return der
    
IRR = newtons(function, derf, 1)
YTM = (1 / IRR - 1) * coupon_frequency * 100

print(f"The Yield to Maturity is: {YTM:.2f}%")
print(f"Accured Interest: {AI:.4f}")