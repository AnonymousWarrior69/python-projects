print('Welcome To The Mini Calculator !\n **Created By Abdullahh**')
print('Select Operation:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division')
choice = input('Enter Choice :')
if choice == '1':
  num1 = float(input('Enter First Number :'))
  num2 = float(input('Enter Second Number :'))
  sum = num1 + num2
  print("The Sum Is :", sum)
elif choice == '2' :
  num1 = float(input('Enter First Number :'))
  num2 = float(input('Enter Second Number :'))
  sub = num1 - num2
  print("The Answer Is :", sub) 
elif choice == '3' :
  num1 = float(input('Enter First Number :'))
  num2 = float(input('Enter Second Number :'))
  mltp = num1*num2
  print("The Answer Is :", mltp)
elif choice == '4' :
  num1 = float(input('Enter First Number :'))
  num2 = float(input('Enter Second Number :'))
  dvd = num1/num2
  print("The Answer Is :", dvd)
