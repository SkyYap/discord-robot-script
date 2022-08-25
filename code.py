import pyautogui
import time
import random
import copy

path_to_file = 'C:\\Users\\xxxx\\Desktop\\Text.txt'

data = []

with open(path_to_file) as f:
    data = f.readlines()

lines = list(data)
back_up_lines = list(data)

allWindow = [w for w in pyautogui.getAllWindows() if 'Discord' in w.title]

def my_function():
	for i in range(len(allWindow)):
		allWindow[i].maximize();
		time.sleep(1);

		if len(lines) <= 0:
                    lines.extend(back_up_lines)
                
		rnd = random.randint(0, len(lines)-1)
		pyautogui.write(lines[rnd], interval=0.05)
		lines.remove(lines[rnd])
		time.sleep(1);
		pyautogui.press('enter')
		time.sleep(1);
		allWindow[i].minimize();

while True:
 	my_function()
 	time.sleep(1)

