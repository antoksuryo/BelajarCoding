my_boolean = True
print(my_boolean)

print(2 == 3)

print("hello" == "hello")

#

x = 7

print(x != 8)
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)

#

print('a' > 'b')
 
print("Bob" > "Dave")

#

x = (7 > 5)
print (int(x))

#

x = 42
if x > 5:
   print("x is greater than 5") 
   
   #
   
age = 24
if age > 18:
    print ('cool')
    
 #
 
 num = 12
 if num > 5:
    print ('Bigger than 5')
    if num <= 47:
        print ('beetween 5 and 47')
        
#

x = 'a'
if (x < 'c'):
    x += 'b'
if (x > 'z')
    x += 'c'
    
 print (x)
 
 #
 
 x = 4
if x == 5:
   print("Yes")
else:
   print("No")
   
   #
   
   age = int (input())
if age >1 and age < 11:
    print ('Child')
elif age > 11 and age <17:
    print ('Teen')
elif age > 18:
    print ('Adult')
    
    
    ##
print(1 == 1 and 2 == 2)

print(1 == 1 and 2 == 3)

print(1 != 1 and 2 == 2)

print(2 < 1 and 3 > 6)


#

print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 > 6)

#

age = 24
limit = 18
height = 191

if (age > limit and height > 180):
  print("Yes")
  
  #
  
  country = "US"
age = 42

if(country == "US" or country == "GB") and (age > 0 and age < 100): 
  print("Cool")
 
   
   #
num = 3
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3: 
  print("Three")
else: 
  print("Something else")
  ##
  
  i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")
  
  ###
  
  
  i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)
  
  ###
  
  
  # bmi calculator
  
  #your code goes here

weight = float(input()) 
height = float(input()) 
bmi = weight/(height**2) 

if bmi<18.5: 
    print("Underweight") 
elif (bmi >= 18.5) and (bmi < 25):
    print("Normal") 
elif (bmi >= 25) and (bmi < 30):
    print("Overweight") 
else: 
    print("Obesity")
  
  
    