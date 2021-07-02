import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scipy.stats as st 
import csv

#Important!
# The plots will have a cross mark at (0,0) which is not the generated sample but a highlight for the origin
def draw_abcd(x, y, part, n):
    plt.figure(figsize=(15,7))
    plt.step(x, y, where="post", label="eCDF", color='g')
    plt.xticks(x, rotation = 90)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.scatter(x, [0]*len(x), color='blue', marker='x', s=100, label='samples (except 0)')
    title = "eCDF for part (" + part + ") when "

    if (part == 'b'):
        title += ("n = " + str(n)) 
    else:
        title += ("m = " + str(n)) 

    plt.title(title)
    plt.xlabel("Samples")
    plt.ylabel("Pr[X<x]")
    plt.legend(bbox_to_anchor=(1, 1), borderaxespad=0.)
    plt.grid(which="both")
    
    
def calcCDF_1d(x):
    n = len(x)
    x.sort()
    y = []
    yi = 0
    
    for i in x:
        yi += 1/n
        y.append(yi)
    
    return (x, y)

def calcCDF_2d(x):
    
    rows = x.shape[0]
    mp = np.zeros((rows,99))
    for i in range(rows):
        #cdf of each row
        r, c = calcCDF_1d(x[i])
        
        #make a map of f^ values
        for j in range(len(r)):
            mp[i][r[j]-1] = c[j]
        
        prev = 0
        for j in range(99):
            if mp[i][j] == 0:
                mp[i][j] = prev
            else:
                prev = mp[i][j]
            
    # Averaging f^ for each row
    avg = mp.mean(0)
    return avg

def part_ab():
    for n in [10, 100, 1000]:
        x = np.random.randint(1,100,n)
        r, c = calcCDF_1d(x)
        r = np.insert(r,0,0)
        c = np.insert(c,0,0)
        draw_abcd(r,c, 'b', n)

def part_cd():
    for m in [10, 100, 1000]:
        x = np.random.randint(1, 100, size = (m,10))
        y = calcCDF_2d(x)
        x = [i for i in range(1, 100)]

        #adding zeros as asked in the question
        x = np.insert(x,0,0)
        y = np.insert(y,0,0)
        draw_abcd(x,y, 'd', m)

def draw_ef(x,y):
    plt.grid(True)
    plt.step(x, y, where="post", label = "F_Hat")
    plt.xlabel("X")
    plt.ylabel("Pr[X<alpha]")

def normal_based_ci(r,c,z):
    #eCdf - 1.96*sqrt(eCdf*(1-eCdf)/n)
    eCdf = np.asarray(c)        
    n = eCdf.shape[0]
    eCdf = np.around(eCdf, 4)
    sub = np.subtract(1,eCdf)
    mult = np.around(np.multiply(eCdf,sub),4)
    var = np.divide(mult, float(n))    
    se = np.sqrt(var)    
    width_by_2 = np.multiply(z,se)

    #lower val of CI
    lower = np.subtract(eCdf, width_by_2)
    #f_hat + z(alpha/2)*sqrt(f_hat*(1-f_hat)/n)

    #upper val of CI
    upper = np.add(eCdf, width_by_2)
    
    #Plot
    plt.step(r, lower, where="post", label = "Lower CI (Normal)")
    plt.step(r, upper, where="post", label ="Upper CI (Normal)")
    plt.grid(True)
    plt.title("eCDF and CIs")
    plt.xlim([0,2])
        
def dkw_based_ci(r, c, alpha): 
    # epsilon = sqrt(1/2n*ln(2/alpha))
    eCdf = np.asarray(c)        
    n = eCdf.shape[0]
    eCdf = np.around(eCdf, 4)   
    epsilon = math.sqrt(math.log(2/float(alpha))/float(2*n))    

    #lower val of CI
    lower = np.subtract(eCdf, epsilon)
    #upper val of CI
    upper = np.add(eCdf, epsilon)
    
    # Plot
    plt.step(r, lower, where="post", label = "Lower CI (DKW)")
    plt.step(r, upper, where="post", label = "Upper CI (DKW")
    plt.grid(True)
    plt.xlim([0,2])
    plt.title("eCDF and CIs")

def part_ef():
    row = []
    with open("a3_q3.csv") as file:
        reader = csv.reader(file)
        i = 0
        for r in reader:
            if (i!=0): #Modified csv by adding header since first line was being skipped
                row.append(float(r[0]))
            i+=1

    z = 1.96
    r, c = calcCDF_1d(row)  

    draw_ef(r, c)
    normal_based_ci(r, c,z)
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=0.)
    plt.show()

    draw_ef(r, c)  
    dkw_based_ci(r, c, 0.05)
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=0.)
    plt.show()

    draw_ef(r, c)
    normal_based_ci(r, c,z)
    dkw_based_ci(r, c, 0.05)
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=0.)
    plt.show()
    

if __name__ == '__main__':
    #Part a and b
    part_ab()
    #First it will show for part a and b
    plt.show()

    #Part c and d
    part_cd()
    #On closing above, part c and d figures will be shown
    plt.show()

    #Part e and f
    part_ef()


