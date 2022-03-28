import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating    when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: The number of iterations it takes for a value to get to 1.
    """
    count = 0
    while(n != 1):
      count += 1
      if(n % 2) == 0:  # n is even
        n = n // 2
      else:                 # n is odd
        n = n * 3 + 1  
    return(count)


def graph_seq3np1(upper_bound):
  """
  Graphs 3n+1 with n being on the X axis and and the number of iterations being on the Y axis. Also keeps track of maximum number of iterations to reach one.
  args: upper_bound (str) starting the range of 3n+1 chosen by the user.
  returns: none
  """
  write_max=turtle.Turtle()
  write_max.up()
  x_axis=turtle.Turtle()
  y_axis=turtle.Turtle()
  window=turtle.Screen()
  graph = turtle.Turtle()
  graph.speed(0)
  window.setworldcoordinates(0,0,10, 10)
  max_so_far = 0
  upper_limit = int(upper_bound)
  for i in range(1,upper_limit+1,1):
    result = seq3np1(i)
    x_axis.goto(i+10,0)
    if result > max_so_far:
      max_so_far = result
      y_axis.goto(0,max_so_far+11)
      write_max.clear()
      write_max.goto(0,max_so_far)
      write_max.write("Maximum so far: " + str(i) +"," + str(max_so_far))
      window.setworldcoordinates(0,0, upper_limit +10, max_so_far +10 )
    graph.goto(i, result)
  window.exitonclick()

def main():
  upper_bound=input("enter a number: ")
  int(upper_bound)
  if upper_bound > str(0):
    start=int(upper_bound)
    for i in range(1,start+1, 1):
      #print(i)
      #print(seq3np1(i))
      print("It takes " + str(seq3np1(i)) +  " iterations for " + str(i) +" to reach 1")
  elif upper_bound < str(0):
    quit()
  graph_seq3np1(upper_bound)
main()