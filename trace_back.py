import traceback
import sys

x = 5
y = 0

try:
    t = x/y
except Exception as e:
    # print traceback.print_exc()
    exception_str = traceback.format_exc()
    print 'Exception Message: ', exception_str, type(exception_str)

sys.exit(0)


