words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2]) 

#############

x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]

print(x[1])
print(y[3])

#############

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    
print(m[1][2])  

############

str = "Hello world!"
print(str[6])

############

nums = [5, 8, 2]
nums[1] = 42

print(nums)

############

nums = [1, 2, 3]
print(nums + [4, 5, 6])

############

nums = [1, 2, 3]
print(nums * 3) 

############

### to check word is exist
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#############

nums = [10, 9, 8, 7, 6, 5 ]
nums[0] = nums[1] - 5
if 4 in nums:
    print (nums[3])
else
    print (nums[4])
    
    
    ############
    
 x = "hello world"

if "world" in x:
  print("Yes")
  
  ############
  
  nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#############

letters = ['a', 'b', 'z']
if 'z' in letters:
    print (yes)
    
    
###########

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
  
#########

str = "testing for loops"
count = 0

for x in str:
  if(x == 't'):
    count += 1

print(count) 

##########

text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)
  
  #########
  
  list = [2, 3, 4, 5, 6, 7]
  
  for x in list:
      if (x %2 ==  1 and x  > 4):
          print(x)
          break
          
  #########
  
  x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
 
sum = 0

for num in x:
    sum += num

print (sum)

###$##$$$

nums = [1, 2, 3, 4, 5, 6, 7]

res = 0

for x in nums:
    if (x %2==0):
        continue
    else
        res += x
print (res)

###########

numbers = list(range(10))
print(numbers) 

############

nums=list(range(5))
print (nums[4])

###$##$$$#####

numbers = list(range(3, 8))
print(numbers)

##############

numbers = list(range(5, 20, 2)) #awal, akhir,step
print(numbers)

##########

x = list(range(7, 3, -1)) ## -1 adalah backward
print(x)

#########

for i in range(5):
  print("hello!")
  
##$##$$####

x = list(range(0, 99))
print (x[4])

#######$$$####


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#############

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7]) #titik diawal menandakan dimulai dari awal sampai..

#############

list = ['a', 'b', 'c', 'd']
a = list [0:2]

#############

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])  # titik diakhir menandakan hitung sampai akhir

#############

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3]) #mulai,akhir,step

#############


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1::4]) #start from beginning, step

#############

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1]) # urutkan dari baelakang sampai 1

##############

nums = [5, 42, 7, 1, 0]
res = nums[::-1]  # membalikkan list
print(res) 

##############

string  = list(input())
print (string[-1]) #output the last string

###########

for i in range (10):
    if not i ℅ 2 == 0: ## this is as a triger
        print(i+1)



###########



n = int(input())

#sum of consecutive number
x = list(range(n+1))
print (sum(x))

############

############
