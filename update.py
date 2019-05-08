# -*- coding: utf-8 -*-
with open("database.txt","a") as f:
	str = input()
	while str!= "end" :
		f.write(str+'\n')
		str = input()
	
