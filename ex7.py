def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"


num = 15
result = fizzbuzz(num)
print(result) 

num = 9
result = fizzbuzz(num)
print(result) 

num = 25
result = fizzbuzz(num)
print(result) 

num = 7
result = fizzbuzz(num)
print(result)  
