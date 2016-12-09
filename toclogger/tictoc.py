# TODO License?
# Copyright John Ladan, 2016

"""
This tic-toc library partially emulates the tic and toc methods from Matlab.

Timing is started with the `tic()` function, and `toc()` returns the time passed since the last `tic()` call.

Data can also be "logged" with a TocLogger object.
"""
import time

_timer = time.time
if 'perf_counter' in dir(time):
    _timer = time.perf_counter


def tic():
    global tictoc_time
    tictoc_time = _timer()

def toc():
    return _timer() - tictoc_time

class TocLogger:

    def __init__(self):
        self._tictoc_time = _timer()
        self._log = []

    def log(self, message=''):
        self._log.append((message, _timer() - self._tictoc_time))

    def get_times(self):
        dts = []
        for m, t in self._log:
            dts.append(t)
        return [t for m,t in self._log]
            
    def get_diffs(self):
        dts = []
        prev_t = 0
        for m, t in self._log:
            dts.append(t-prev_t)
            prev_t = t
        return dts
            

    def print_log(self):
        prev_t = 0
        for message, t in self._log:
            print("{}\t{}".format(t-prev_t, message))
            prev_t = t
