def checkio(number):
    #Your code here
    if number % 3 == 0 and number % 5 == 0 :
        number = "Fizz Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    else:
        number = str(number)
    return str(number)

print checkio(15)
print checkio(6)
print checkio(5)
print checkio(7)
