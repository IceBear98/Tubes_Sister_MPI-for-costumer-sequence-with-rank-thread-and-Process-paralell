# -*- coding: utf-8 -*-
"""
Created on Wed May  8 05:46:24 2019

@author: User
"""

import threading
import time
import multiprocessing
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

number_list = list(range(1,1000))

def count(number):
    i = 0
    for i in range(10**6):
        i += 1
    return i*number
    
def crunch_time(rank):
    crunch = count(rank)
    print("rank : %s, crunch = %s " %(rank,crunch))
    time.sleep(5) #berhenti selama 5 detik


if __name__ == '__main__':
#jalankan secara serial
    start_time = time.clock()
    for rank in number_list:
        crunch_time(rank)
    end_time = time.clock()
    print("start time = " ,start_time)
    print("end time = ",end_time)
    print("Serial time = ",end_time - start_time)

#jalankan secara thread
    start_time = time.clock()
    for rank in number_list:
        t = threading.Thread(target = crunch_time(rank))
        t.start()
        t.join()
    end_time = time.clock()
    print("start time = " ,start_time)
    print("end time = ",end_time)
    print("Thread time = ", end_time - start_time)
    
#jalankan secara parallel
    start_time = time.clock()
    for rank in number_list:
        process = multiprocessing.Process(target = crunch_time(rank))
        process.start()
        process.join()
    end_time = time.clock()
    print("start time = " ,start_time)
    print("end time = ",end_time)
    print("Parallel time = ", end_time - start_time)
    
    
    
