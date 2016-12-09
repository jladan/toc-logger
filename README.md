Tic Toc Logger
==============

A basic tool for logging how long tasks take in scripts.

Usage
-----

The main feature of the module is a TocLogger object. At initialization, the time is stored. Every call of `TocLogger.log()` saves the time since initialization, much like the "lap" button on a stopwatch. You can optionally label each log entry. Example:

```
from toclogger import TocLogger

# Start the clock
toc = TocLogger()

# ... some long-ish task
toc.log('Performing some longish task')

# ... another long task
# This time with no descriptive message
toc.log()

# Print out the log with times and messages
toc.print_log()
```

Features
--------

Features include:
- no print to stdout mid-program.
- self-contained (does not pollute the namespace).
- multiple independent timers can be created.
- a full sequential log of computation times can be extracted at any point.
- uses the more accurate `time.perf_counter()` when available

Similar works
-------------

This module is of course built upon MATLAB's `tic` and `toc` commands. These are simple commands that say "start tracking time now", and "tell me how long it's been". These are not great profiling tools, but help to quickly find where the slow bits are. E.g. Is it data import that's slow, analyzing the data, or printing it?

There have been code snippets shared about. For example, [Tyler Hartley](https://gist.github.com/tylerhartley/5174230) made `tic()` and `toc()` functions that include tagging the event. Drawbacks are that it uses global variables, and always prints when `toc()` is called, polluting the program output.

There is also [this](https://bfroehle.com/2011/07/18/simple-timer/) `with TicToc()` snippet that avoids global variables, but still prints, and messes with indentation -- annoying when quickly inserting and removing it.
