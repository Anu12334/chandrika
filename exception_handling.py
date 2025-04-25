try:                          #try block will generate an exception
    n = 0
    res = 100 / n
    
except ZeroDivisionError:               #many exception blocks
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:                                 #else define no errors were raised 
    print("Result is", res)
    
finally:
    print("Execution complete.")
