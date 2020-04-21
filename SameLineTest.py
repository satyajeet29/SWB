#An example of printing in the same line
import time

def backline():
    print('\r', end='')                     # use '\r' to go back


for i in range(101):                        # for 0 to 100
    s = str(i) + '%'                        # string for output
    print(s, end='')                        # just print and flush
    backline()                              # back to the beginning of line
    time.sleep(0.2)                         # sleep for 200ms