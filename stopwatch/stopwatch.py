#! python3
# stopwatch.py - A simple stopwatch

import time

# Display the programs's instructions.
print('Press ENTER to begin. Afterwards,\npress ENTER to "click" the stopwatch.\nPress Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')

