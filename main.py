#  Calculators Functions 

def showHelp():
  msg=f"\U0001F44B, Thank you for using Py-Calc(also called Python Calculator). If you want any new feature you can contact us from our GitHub profile \n Here are the following number for each operation: \n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n Note: Py-Calc is case sensitive and users are requested not to use spaces. \n"
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