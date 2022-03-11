import schedule
import os
import time

NUM = 0


def write_num():
    # print "inside write_num"
    global NUM
    NUM += 2
    with open(os.getcwd() + os.path.sep + "result", "a") as f:
        f.write("\n" + str(NUM) + " Time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

x_schedule = schedule.every(2).seconds.do(write_num)

print x_schedule, type(x_schedule)
print dir(x_schedule)

while NUM < 20:
    schedule.run_pending()
    time.sleep(1)
