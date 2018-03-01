def get_n(number):
  return len(number) / 2

def square(number):
  return number**2;

def transform(squared, n):
  while(len(str(squared)) < 2*n):
    squared = '0' + str(squared)
  return squared

def return_substring(number, n):
  n2 = int(len(number) - n*2)
  return number[int(n) : n2]

def method():
  number = int(input("Introduce la semilla: "))
  iter = int(input("Introduce las iteraciones: "))
  str_number = number.__str__()
  n = get_n(str_number)
  while(iter > 0 ):
    squared = square(number)
    squared = transform(squared, n)
    string = return_substring(str(squared), n)
    print("\n Result: " + "." + string + "\n Iteracion" + str(iter))
    number = int(string)
    iter = iter - 1

method()
