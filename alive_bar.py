from alive_progress import alive_bar
import time

for total in 5000, 7000, 4000,0:
    with alive_bar(total) as bar :
        for _ in range (5000) :
            time.sleep(.001)
            bar()