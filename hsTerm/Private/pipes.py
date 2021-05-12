class newPipe():
  def __init__(self, name: str, size: int=None):
    """
    Generic Stack setup for output pipes.

    name: name of the pipe
    size: left as default for no size limit
    """
    self.name = name  # No real use for this at the moment.
    self.size = size  # If set to None, it will not limit the size.
    self.data = []
  
  def push(self, item: object):
    """
    Push an item to the end of the pipe

    item: the item to be added to the pipe
    """
    if (self.size!=None) & ((len(self.data)+1)==self.size):  # If size enforced and list will exceed size limit
      self.pop()  # Pop oldest item in stack.
    self.data.append(item)

  def pop(self, item: int=0):
    """
    Remove an item from the pipe.

    item: leave as deault to pop oldest item
    """
    self.data.pop(item)
  
  def clear(self):
    """
    Remove all items from the pipe.
    """
    self.data = []

class inputPipe():
  def __init__(self, name: str):
    """
    Used to generate current input.
    """
    self.name = name  # No use at the moment.
    self.data = []    # Generic data object again.
  
  def push(self, item):
    """
    Push a character to the stack.
    """
    self.data.append(item)
  
  def pull(self, item):
    """
    Pull the current input and clear the stack.
    """
    with self.data as temp:  # Used so self.data can be cleared and returned.
      self.clear()
      return ''.join(temp)
  
  def clear(self):
    """
    Clear the stack.
    """
    self.data = []