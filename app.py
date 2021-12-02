import random as rand

matrix = [[]]

def print_matrix():
  for row in matrix:
    newstr_arr = str(row).split(',')
    newstr = ''
    for item in newstr_arr:
      newstr += item
    print(newstr)


def main():
  for n in range(5):
    for m in range(5):
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


if __name__ == '__main__':
  main()
