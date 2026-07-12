import time

def precise_sleep(seconds):
  end = time.perf_counter() + seconds
  while time.perf_counter() < end:
    pass