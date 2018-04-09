import numpy as np

def main():
  matrix = np.loadtxt('matrix.txt')
  print(matrix)
  n = int(input("Introduce número de transiciones: "))
  for i in range (1, n):
    matrix = matrix.dot(matrix)
  print(matrix)
    
main()