#Program to plot/visualize data

import numpy as np
import re
import itertools
import matplotlib.pyplot as plt
#from  read_function import data_load


# delete this function and import from read_function

def data_load(filename, Run_num_start, Run_num_end):
    data = []
    with open(filename,'r') as infile:
        copy = False
        for line in infile:
            if line.strip() == "Run #"+str(Run_num_start):
                copy = True
            elif line.strip() == "Run #"+str(Run_num_end):
                copy = False
            elif copy:
                line = line.split()
                line = line[1:]
                data.append(np.array(line))
    data = np.array(data)    
    return data



def plot(data_1,data_2,final_time_step = 200,initial_time_step = 0,Error=True):
    '''
    # Plot function takes 5 arguments data_1; data_2;  final_time_step; initial_time_step
    # data_1== Expected_data--np array
    # data_2== NN_output -- np array
    # final_time_step== (int) time step till where you want to plt
    # initial_time_step == default value --  zero; int time step from where you want to plot
    # Error-- Boolean if True prints training testing error else prints correct and predicted O/p
    # It plots the data on 2D graph.
    '''
    X_axis=[]
    Y_axis_orig_data=[]
    Y_axis_NN_data=[]
    length= data_1.shape[0]
    
    for i in range(length):  
        X_axis.append(i)
        Y_axis_orig_data.append(int(data_1[i]))
        Y_axis_NN_data.append(int(data_2[i]))
    max_orig= max(Y_axis_orig_data)
    max_NN= max(Y_axis_NN_data)
    Y_max=max(max_orig,max_NN)
    if Error==False:
        plt.ylabel('Output')
        plt.xlabel('No. of Runs')
        plt.plot( X_axis,Y_axis_orig_data, 'ro', X_axis, Y_axis_NN_data, 'bo')
        n=1
    elif Error==True:
        plt.ylabel('Error')
        plt.xlabel('No. of Hidden Units')
        plt.plot( X_axis,Y_axis_orig_data,  X_axis, Y_axis_NN_data )
        n=5
    plt.axis([0,final_time_step, 0, Y_max+n])
       # plt.xticks(X_axis)             ## to show all X axis data; but it looks too cluturred
    plt.show()


if __name__ == '__main__':
   data = data_load('15B-no_0',0,1)
   # print data[2]
   plot(data[100],data[4])
