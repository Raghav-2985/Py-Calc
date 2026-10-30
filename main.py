# Libraries
import math
#  Predefined Values
user = None
#  Calculators Functions 

def showHelp():
  msg=f"\U0001F44B, Thank you for using Py-Calc(also called Python Calculator). If you want any new feature you can contact us from our GitHub profile \n Here are the following number for each operation: \n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n 5 - Floor  \n 6 - Modulo Division \n 7 - Square (Single number is allowed) \n 8 - Cube (Single number is allowed)\n 9 - Square Root (Single number input is allowed) \n 10 - Cube Root (Single number input is allowed) \n 11 - Abs (Single number input is allowed) \n 12 - Exponential terms (2 number inputs are allowed: 1. The number itself 2. Its power) \n Note: \n Py-Calc is case sensitive and users are requested not to use spaces. \n If user add more number inputs than the allowed number inputs then the rest will be ignored"
  print(msg)

def add(*nums): #addition 
  value = 0
  for n in nums:
    value = value + n 
  return value

def subtract(*nums): #subtraction
  value = nums[0]
  i=0
  while i+1 < len(nums):
    value = value - nums[i+1]
    i = i+1
  return value

def multiply(*nums): # Multiplication
 value =1
 for i in nums:
  value= value * i
 return value

def divide(*nums):  # Division
  value = nums[0]
  i=0
  while i+1 < len(nums):
    value = value / nums[i+1]
  return value

def floorDivide(*nums): # floor division
  value = nums[0]
  i=0
  while i+1 < len(nums):
    value = value // nums[i+1]
  return value

def modulo(*nums): # modulo
  value = nums[0]
  i=0
  while i+1 < len(nums):
    value = value % nums[i+1]
  return value

def square(*num): # square
  value = num[0] ** 2
  return value

def cube(*num): # cube 
  value = num[0] ** 3
  return value

def sqRoot(*num): # square root
  value = math.sqrt(num[0])
  return value

def cuRoot(*num): # cube root
  value = math.cbrt(num[0])
  return value

def doAbs(*num): # abs
  value = abs(num[0])
  return value

def exp(*num): # exponential terms
  value = num[0] ** num[1]
  return value

# frontend 
showHelp()
while True:
# receive operation type and perform operation
  def takeop():
    try:
      operation =int(input("Enter Operation to perform: "))
    except ValueError:
      print("Enter a valid operation")
      takeop()
    return operation

  userOperation = takeop()

  
# receive numbers as input
  try:
    if user == None: 
      user=int(input("How many numbers do have on your calculation: "))
  except ValueError:
    print("Invalid Input")
    print("Enter a valid non zero positive number")

  operationNums=[]
  for i in range(user):
    try:
      numbers=int(input(f"Enter #{i+1} number: "))
    except ValueError:
      print("Invalid Number")
      print("Counting it as 0")
    else:
      operationNums.append(numbers)

# Print Output
  match userOperation:
      case 1:
       print(f"Addition of your given number: {add(*operationNums)}")
      case 2:
       print(f"Subtraction of your given number: {subtract(*operationNums)}")
      case 3:
       print(f"Multiplication of your given number: {multiply(*operationNums)}")
      case 4:
       print(f"Division of your given number: {divide(*operationNums)}")
      case 5:
       print(f"Floor Division of your given number: {floorDivide(*operationNums)}")
      case 6:
       print(f"Modulo Division of your given number: {modulo(*operationNums)}")
      case 7:
       print(f"Square of your given number: {square (*operationNums)}")
      case 8:
       print(f"Cube of your given number: {cube(*operationNums)}")
      case 9:
       print(f"Square Root of your given number: {divide(*operationNums)}")
      case 10:
       print(f"Cube Root of your given number: {divide(*operationNums)}")
      case 11:
       print(f"Abs of your given number: {doAbs(*operationNums)}") 
      case 12:
       print(f"Value of your given exponential term: {exp(*operationNums)}")
      case _:
       print("Invalid Operation")