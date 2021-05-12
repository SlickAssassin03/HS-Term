from .Private import pipes
from threading import Thread, Lock

class hsTerm():
  def __init__(self):
    """
    hsTerm is a module that allos you to take user input at the same time
    as printing to the terminal. Read the repl docs for more info.


    """
    self.stdout = pipes.newPipe('sys.stdout')        # Standard output pipe.
    self.stderr = pipes.newPipe('sys.stderr')        # Standard error pipe.
    self.stdin_stack = pipes.inputPipe('stdin')  # Input stack to generate input.
    self.stdin = pipes.newPipe('stdin')          # Standard input pipe.
    
    self.lock = Lock()
  
  # Standard Output
  def print(self, *values: object, sep: str=' ', end: str='\n', flush: bool=True):
    """
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    self.stdout.push((sep.join([str(value) for value in values]))+end)
    if flush:
      self._flush(self.stdout)
  
  # Standard Error
  def error(self, value: str, flush: bool=True):
    """
    Output error to terminal without raising it formally.
    """
    self.stderr.push(value)
    if flush:
      self._flush(self.stderr)

  # Any Pipe
  def _flush(self, pipe: object):
    """
    Flush a specific pipe.

    pipe: one of the pipes.
    """
    if (len(pipe.data)>0):
      self.lock.acquire()
      print(''.join(pipe.data),file=pipe.name,sep='',end='')
      pipe.clear()
      self.lock.release()

# Debug Area
if __name__ == "__main__":
  pass