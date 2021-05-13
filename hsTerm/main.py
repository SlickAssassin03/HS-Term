from .Private import pipes
from threading import Thread, Lock
from getch import getch

class hsTerm():
  def __init__(self):
    """
    hsTerm is a module that allos you to take user input at the same time
    as printing to the terminal. Read the repl docs for more info.


    """
    self.out = pipes.newPipe('out_pipe')       # Generic output pipe.
    self.err_pipe = pipes.newPipe('err_pipe')  # Error output pipe.
    self.in_stack = pipes.inputStack('in')      # Input stack to generate input.
    self.special = {27:'^[', 279165:'^[[A', 279166:'^[[B', 279167:'^[[C', 279168:'^[[D'}

    self.out_lock = Lock()
    self.in_lock = Lock()

  # Generic Input
  def input(self, prompt: str='', timeout_if_already_locked: bool=True):
    """
    Get input from a user, can be used while printing simultaneously.
    Target this with a thread to do it in the background, then use get_key(key) to grab input.

    key: value to be stored to, use get_key(key) to get inputs when they are finished
    prompt: print this before the input part
    """
    if self.in_lock.locked() & timeout_if_already_locked:
      return 0
    self.in_lock.acquire()
    while True:
      _key = ord(getch())
      if _key==10:
        break
      elif _key==127:
        self.in_stack.data.pop()
      elif _key in self.special.keys():
        self.in_stack.push(self.special[_key])
      else:
        self.in_stack.push(chr(_key))
      print(_key)

    out = self.in_stack.pull()
    self.in_lock.release()
    return out

  # Generic Output
  def print(self, *values: object, sep: str=' ', end: str='\n', flush: bool=True):
    """
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    self.out_pipe.push((sep.join([str(value) for value in values]))+end)
    if flush:
      self._flush(self.out_pipe)
  
  # Error Output
  def error(self, value: str, flush: bool=True):
    """
    Output error to terminal without raising it formally.
    """
    self.err_pipe.push(f'\u001b[31m{value}\n')
    if flush:
      self._flush(self.err_pipe)

  # Any Pipe
  def _flush(self, pipe: object):
    """
    Flush a specific pipe.

    pipe: one of the pipes.
    """
    if (len(pipe.data)>0):
      self.out_lock.acquire()
      print(''.join(pipe.data),sep='',end='')
      pipe.clear()
      self.out_lock.release()

# Debug Area
if __name__ == "__main__":
  pass