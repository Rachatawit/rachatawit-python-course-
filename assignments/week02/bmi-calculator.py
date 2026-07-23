weight = float(input("Enter Your Weight(Kg)"))
height = float(input("Enter Your Height(M)"))
bmi = weight / (height * height)
print("",bmi)
if bmi<18.5 :
        print("Underweight")
elif bmi>=18.5 :
        print("Normal weight")
elif bmi>=25.0 and bmi<30.0:
        print("Overweight")
else :
        print("Obese")