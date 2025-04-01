#Simple Python
x =150
y=“Marceille"
name = "anna"
surname = "Grey"
student_name = name + " " + surname
#Python is using indent
a = 10
b = 5
c = a ** b
d = a / b
e = a * b
f = a % b


#a == b 
#a || b
#a === b
#a != b
#a ^^ b 
#a && b

print(x)
print(y)
print(student_name)
print(c)
print(d)
print(e)
print(f)

#Task
#1. Write IF ELSE statemant to validate if x is larger than y return true if yes

def result (x , y) :
  if (x > y):
    return True
  return False

print(result(100,200))

#2. Write IF ELSE statemant to validate if x is larger than y and less than b return true if yes

def result (x , y , b) :
  if (x > y) and (x < b):
    return True
  return False

print(result(300, 200, 400))





