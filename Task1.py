def cel_to_feh(degree_in_c):
    degree_in_f = (degree_in_c*9/5)+32
    return degree_in_f
def feh_to_cel(degree_in_f):
    degree_in_c = (degree_in_f-32)*(5/9)
    return degree_in_c
def cel_to_kel(degree_in_c):
    degree_in_kel = (degree_in_c)+273.15 
    return degree_in_kel
def kel_to_cel(degree_in_kel):
    degree_in_c = (degree_in_kel)-273.15 
    return degree_in_c
def feh_to_kel(degree_in_f):
    degree_in_kel = (degree_in_f - 32) * (5/9) + 273.15
    return degree_in_kel
def kel_to_feh(degree_in_kel):
    degree_in_f = (degree_in_kel - 273.15) * 9/5 + 32 
    return degree_in_f


degree =float(input("Please enter degree: "))
measurement = input("Please enter measurement: ")

if measurement == "Celsius" or measurement == "celsius" or measurement == "c" or measurement == "C":
    print(cel_to_feh(degree))
    print(cel_to_kel(degree))
elif measurement == "Fahrenheit" or measurement == "fahrenheit" or measurement == "f" or measurement == "F":
    print(feh_to_cel(degree))
    print(feh_to_kel(degree))
elif measurement == "Kelvin" or measurement == "kelvin" or measurement == "k" or measurement == "K":
    print(kel_to_cel(degree))
    print(kel_to_feh(degree))
else: print("Measurement not valid")