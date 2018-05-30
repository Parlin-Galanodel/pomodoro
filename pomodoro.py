# -*- coding: utf-8 -*-

import time
import os


def nextsec():
	time.sleep(1)
	global s
	s+=1
	if s == 60:
		s = 0
		nextmin()
	
def nextmin():
	global m
	m+=1
	if m == 60:
		m = 0
		nexthour()
		
def nexthour():
	global h 
	h += 1
	print(h)
	
if __name__ == "__main__":
	t = input("minutes you want to study:\n")
	t = int(t)
	hour, minute = divmod(t,60)
	second = 0
	h,m,s = 0,0,0
	while(h*60+m!=t):
		nextsec()
		print("%d:%d:%d" %(h,m,s))
		os.system('cls' if os.name == 'nt' else 'clear')
	print("done")