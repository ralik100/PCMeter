import main
import functions as fun
import time

def test_cpu_usage():
    start=time.time()
    result=fun.cpu_usage(10)
    end=time.time()
    time_elapsed=end-start
    assert 10.1 > time_elapsed > 9.9