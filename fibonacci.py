def fib(n):
  list = [0,1]
  count = 0
  if type(n) is int:
    for i in range(n-1):
      count = list[-2] + list[-1]
      list.append(count)
    print list
  else:
    print("Error: arg not int")


def main():
  print 'test'
  fib(25)

if __name__ == '__main__':
  main()
      