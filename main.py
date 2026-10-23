#  Calculators Functions 

def add(*nums): #addition 
  for n in nums:
    value = 0
    value = value + n 
  return value

def subtract(*nums): #subtraction
  for n in nums:
    value = 0 
    value = value - n
  return value

# frontend 

# receive numbers as input
try: 
  user=int(input("How many numbers do have on your calculation"))
except ValueError:
  print("Invalid Input")
  print("Enter a valid non zero positive number")

operationNums=[]
for i in range(user):
  try:
    numbers=int(input(f"Enter {i}st number:"))
  except ValueError:
    print("Invalid Number")
    print("Counting it as 0")
  else:
    operationNums.append(numbers)

# receive operation type and perform operation
def takeop():
  operation =input("Enter Operation to perform:")

  if operation != int:
   print("Enter a valid operation:")
   takeop()
  else:
    int(operation)

  return operation

userOperation = takeop()

match userOperation:
  case 1:
    print(f"Addition of your given number: {add(*operationNums)}")
  case 2:
    print(f"Subtraction of your given number: {subtract(*operationNums)}")
  