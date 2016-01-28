# -*- coding: cp932 -*-
#!/usr/bin/python
#=======================================================================================================================================================================

#This is my fourth project that deals with Mandelbrot and Julia fractals.

#=======================================================================================================================================================================
from fractals_modules import *

print ("Hello, welcome to the Python fractal program!")
# While the argument is still 'true,' it will continue to loop the body of code
while True:
    try:
        option = raw_input("Enter 'j' to create a render of the Julia fractal, 'm' for the Mandelbrot fractal or 'q' to quit： ")
        if option not in ['j', 'm', 'q']: # Limits the input that the variable 'option' is allowed to accept, which in our case is only '1' or '2'
            raise TypeError("Input was not 'j', 'm', or 'q'") # Functions to raise a specific error (ValueError in our case) when input is not within our desired answer from the user
        break # Will break us out of the loop when the user inputs a correct desired answer
    except TypeError: # Functions like the 'raise ValueError,' but in this case it encompasses all the things that aren't numbers in specific
        print ("Please enter only the available given options!")

while (option != 'q'):
    while True:
        try:
            # Following code prompts the user for the required input necessary to make the Julia and Mandelbrot fractals
            n = int(raw_input("Please enter the number of 'n' iterations the fractal will have： "))
            mxx = float(raw_input("Enter the MAX 'x' for our fractal： "))
            mxy = float(raw_input("Enter the MAX 'y' for our fractal： "))
            mnx = float(raw_input("Enter MINIMUM 'x' for our fractal： "))
            mny = float(raw_input("Enter MINIMUM 'y' for our fractal： "))
            break
        except ValueError:
            print ("Please enter a number only, this program will restart the input process again from the beginning")

    # Code calls the module created by Jaime and renders the Julia fractal
    if (option == 'j'):
        renderJulia(n,mnx,mny,mxx,mxy)
        option = raw_input("Enter 'j' to create a render of the Julia fractal again，'m' for the Mandelbrot fractal，or 'q' to quit： ")

    # Code calls the module created by Jaime and renders the Mandelbrot fractal
    elif (option == 'm'):
        renderMandelbrot(n,mnx,mny,mxx,mxy)
        option = raw_input("Enter 'm' to create a render of the Mandelbrot fractal again, 'j' for the Julia fractal or 'q' to quit： ")

else:
    print ("\n")
    print ("You have chosen to quit!")
    print ("Thank you for using the program!")
    print ("Credits for the fractal module go to the awesome TA Jaime Vargas")
    print ("\n")
    Cancel_FC = raw_input("Press 'Enter' on the keyboard to close the console.")

        
    
    


