# Donovan Farley-Freeman
# 12/9/24
# Reversing a string using a stack
from arraystack import ArrayStack

def main():
  original = "Sphinx of black quartz, judge my vow"
  new = ""
  stack = ArrayStack()

  for i in original:
    stack.push(i)
  
  for letter in range(len(stack)):
    new += stack.pop()
    
  print(f"\nOriginal: {original}")
  print(f"Reversed: {new}\n")




if __name__ == "__main__":
  main()