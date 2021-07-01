# -*- coding: utf-8 -*-
"""
Created on Sat May  4 07:22:31 2019

@author: User
"""
#menghitung bobot angka dari rank menggunakan MPI dimana menghitung pada rangenya
# range = 10^6

from mpi4py import MPI
import concurrent.futures
import time

comm = MPI.COMM_WORLD
rank = comm.rank

daftar_angka = list(range(1,100))

max_workers = 10

def hitung(angka):
    i = 0
    for i in range(10**6): #range pengaruh terhadap bobot/weight , semakin besar rangenya maka semakin lama prosesnya
        i += 1  #maju satu langkah
    return i*angka #mengembalikan ke i dimana dalam range(10*7)*angka

def evaluasi(rank): #bobot dari rank
    bobot = hitung(rank)
    print('Rank %s, weight %s' % (rank, bobot))
    time.sleep(5) # waktu berhenti


if __name__ == '__main__':
    # Sequential Execution
    start_time = time.clock()
    for rank in daftar_angka:
        evaluasi(rank)
    print('Sequential Execution in %s seconds' % (time.clock() - start_time)) #waktu sesudahnya dikurangi waktu awal
    
    # Thread Pool Execution
    start_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        for rank in daftar_angka:
            executor.submit(evaluasi, rank)
    print('Thread Pool Execution in %s seconds' % (time.clock() - start_time))
    
    # Process Pool Execution
    start_time = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers) as executor:
        for rank in daftar_angka:
            executor.submit(evaluasi, rank)
    print('Process Pool Execution in %s seconds' % (time.clock() - start_time))
 