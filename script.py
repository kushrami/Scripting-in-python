#Author : kushrami
#Date : 15 sept 2020

#This script is to create multiple files in python. Where there is specific ordering in naming is required.
#Very simple example is, there is book with 20 chepters and every chepter has 10 examples. and for
# every example you want to generate a unique file name with an order(without doing any mistake). Then here is your solution. 

import os
filename = "Excersice_"
extension = ".py"
for chepter in range(1,21):
    for excersicecount in range(1,11):
        oscommand = "> " + filename + str(chepter) + "_" + str(excersicecount) + extension
        os.system(oscommand)