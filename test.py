#!/usr/bin/python3

while True:
    
    user_input = float(input("Enter value: "))
    if user_input == "DONE":    
        break
    else:
        PROCENTAGE = 0.27

        def calc(input, procentage):   
       	    calc = input * procentage
       	    return calc

   	amount_due = calc(user_input, PROCENTAGE)

   	print(str(amount_due))
 
        #".txt" file location on system      
   	with open(".txt", "a") as text_file:  
       	    text_file.write(str(amount_due) + "\n")
       	    text_file.close()
    continue 
