def fizzbuzz(num):
    if num > 0:
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
def main():
    
        for i in range(1,100+1):
            fizzbuzz(i)
    
main()    
        
        
        