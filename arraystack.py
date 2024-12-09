class ArrayStack:

  def __init__(self):
    """Initialize the variables of the stack class"""
    self.__stack = []
    self.__size = 0

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out

  def __len__(self):
    """Returns the size of the stack"""
    return self.__size

  def __is_empty(self):
    """Returns a boolean based off whether the stack is empty"""
    if self.__size == 0:
      return True
    else:
      return False

  def push(self, element):
    """Adds an element to the top of the stack"""
    self.__stack.append(element)
    self.__size += 1

  def pop(self):
    """Removes the top element in the stack from the stack then returns the removed element"""
    if self.__is_empty() is False:
      top = self.top()
      del self.__stack[-1]
      self.__size -= 1
      return top
    else:
      raise IndexError("Stack index is out of range")

  def top(self):
    """Returns the element at the top of the stack"""
    if self.__is_empty() is False:
      return self.__stack[-1]
    else:
      raise IndexError("Stack index is out of range")