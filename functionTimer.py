#simple snippet to time execution of functions in your scripts
import time

def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print("Total time running %s: %s seconds" %(function.__name__, str(t1-t0)))
    return result
  return function_timer
  
#now just add @fn_timer above any method that you want to time
