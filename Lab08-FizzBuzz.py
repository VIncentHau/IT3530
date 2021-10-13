# Vincent Hau
#10/13/21
#IT 4320
#Fizz Buzz Challenge
 
# prints number 1 to 100
for fizzBuzz in range(1,100):
 
    # Multiples by both 3 & 5, print 'FizzBuzz'
    if fizzBuzz % 15 is 0:
        print("FizzBuzz")                                        
        continue
 
    # Number multiple by 3, print 'Fizz'
    elif fizzBuzz % 3 is 0:    
        print("Fizz")                                        
        continue
 
    # Number multiple by 5, print 'Buzz'
    elif fizzBuzz % 5 is 0:        
        print("Buzz")                                    
        continue
 
    # Print Output
    print(fizzBuzz)