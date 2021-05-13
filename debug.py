from threading import Thread
from hsTerm import main
from time import sleep
main = main.hsTerm()

def input_threaded(prompt):
  def get_input_threadable(prompt):
    main.input(prompt, True)
    return main.in_stack.cache[0]
  try:
    thread = Thread(target=get_input_threadable, args=prompt)
    thread.run()
    return 1
  except:
    return 0

while True:
  if main.in_stack.finished:
    input_threaded(">>> ")
  else:
    x = main.in_stack.data[0]
    main.print("Input received: "+x)
  sleep(1)
  main.print("Looped...")
