#!/usr/bin/python
import random
import os

os.system("rm data_rt_rr_statwosysdsk.txt")
for x in range(7100):
    RT = round(random.uniform(0, 1) % 0.09,3)
    CUP_usage = round(random.uniform(1, 10) * 9,3)
    KBin = random.randint(5, 10)
    PktIn = KBin * 1024
    KBout = random.randint(5, 10)
    PktOut = KBout * 1024
    f = open("./data_rt_rr_statwosysdsk.txt" , "ar")
    f.write("%0.3f,%0.3f,%i,%i,%i,%i\n" %(RT,CUP_usage , KBin , PktIn , KBout , PktOut))
    f.close()
