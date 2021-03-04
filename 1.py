#python 3.7.1

def menu():
   #print what options you have
   print ("welcome to calculator.py")
   print ("your options are:")
   print ("")
   print ("1)Addition")
   print ("2)Subtraction")
   print ("3)Multiplication")
   print ("4)Division")
   print ("5)Quit calculator.py")
   print ("")
   return int(input("choose your option:"))
#THIS ADD TWO NUMBERS GIVEN
def add(a,b):
    print (a,"+",b,"=",a+b)

#THIS SUBTRACTS TWO NUMBERS GIVEN
def sub(a,b):
    print (b,"-",a,"=",b-a)

#THIS MULTIPLIES TWO NUMBERS GIVEN
def mul(a,b):
    print (a,"*",b,"=",a*b)

#THIS DIVISION TWO NUMBERS GIVEN
def div(a,b):
    print (a,"/",b,"=",a/b)
#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      add(int(input("Add this:")),int(input("to this:")))
  elif choice == 2:
      sub(int(input("subtract this:")),int(input("from this:")))
  elif choice == 3:
      mul(int(input("multiply this:")),int(input("by this:")))
  elif choice == 4:
      div(int(input("divide this:")),int(input("by this:")))
  elif choice == 5:
      loop = 0
print ("thank u for using calculator.py!")


