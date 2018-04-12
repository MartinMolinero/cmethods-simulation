import numpy as np

def main():
  vector = np.loadtxt('chapman-k-vector.txt')
  matrix = np.loadtxt('chapman-k-matrix.txt')
  n = int(input("Introduce número de transiciones: "))
  for i in range (0, n):
    matrix = matrix.dot(matrix)
  print("\nMatrix:")
  print(matrix)
  vector = vector.dot(matrix)
  print("\nVector:")
  print(vector)
    
main()
