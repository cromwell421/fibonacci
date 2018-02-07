def fib(n):
  list = [0,1]
  count = 0
  
  if type(n) is not int:
    print("Error: arg not int")
  
  elif n < 1:
    print("That number is less than 1!!!")
  
  elif n == 1:
    print list[0]

  else:
    for i in range(n-2):
      count = list[-2] + list[-1]
      list.append(count)
    print list


def main():
  choice = (input("Pick an integer 1-100: ")
  fib(choice)

if __name__ == '__main__':
  main()
      
