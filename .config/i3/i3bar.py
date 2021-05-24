import time
import psutil
from datetime import datetime
from moving_screen import MovingScreen


screen = MovingScreen("GONZITO")
screen.make_screen()
i = 0
while True:
    memory_usage = round(psutil.virtual_memory().used / 1000000000 ,1)
    now = datetime.now()
    time_now = now.strftime("%b-%d-%y %I:%M%p")
    print( "MEM:" + str(memory_usage) + "G " + screen.run_screen(i) + " " + time_now)
    time.sleep(1)
    i += 1
    if i >= screen.get_size()*2:
        i=0
