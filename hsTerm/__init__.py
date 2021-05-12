import builtins

def print(*args, **kwargs):
  builtins.print(*args, **kwargs)
  builtins.print("hooked")
