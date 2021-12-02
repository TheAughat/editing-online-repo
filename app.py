import random as rand

matrix = [[]]

def print_matrix():
  for row in matrix:
    newstr_arr = str(row).split(',')
    newstr = ''
    for item in newstr_arr:
      newstr += item
    print(newstr)


def main(x):
  for n in range(x):
    for m in range(x):
      matrix[n].append(0)
    matrix.append([])
  matrix.pop()
  print_matrix()
  print()
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      rand_num = rand.randint(0, 9)
      matrix[i][j] = rand_num
      matrix[j][i] = rand_num
  print_matrix()
  print()
  for i in range(len(matrix)):
    matrix[i][i] = 0
  print_matrix()
  print()


def create_matrix():
  print('Enter N:')
  n = input()
  main(int(n))


if __name__ == '__main__':
  create_matrix()
