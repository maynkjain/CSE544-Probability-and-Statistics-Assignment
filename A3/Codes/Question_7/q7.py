from normal_kde import normal_kde
from uniform_kde import uniform_kde
from triangular_kde import triangular_kde
import numpy as np
from numpy import *
import scipy.stats
import math
import matplotlib.pyplot as plt

colors = ['b', 'g', 'r', 'y', 'k', 'm']
Hs = [0.0001, 0.0005, 0.001, 0.005, 0.05]
Xs = np.arange(0, 1.01, 0.01)

def findAndPlotUsingKDE(kde_type):
    print("\nType of KDE: " + kde_type)
    pdfs_for_all_h_and_given_normal = {}

    given_normal = scipy.stats.norm(0.5, pow(0.01, 0.5))
    org_pdfs_for_all_x = []
    for x in Xs:
        org_pdfs_for_all_x.append(given_normal.pdf(x))
    pdfs_for_all_h_and_given_normal["original"] = org_pdfs_for_all_x

    true_mean = np.mean(org_pdfs_for_all_x)
    true_var = np.var(org_pdfs_for_all_x)

    for h in Hs:
        pdfs_for_all_x = []
        for x in Xs:
            if (kde_type == 'normal'):
                pdfs_for_all_x.append(normal_kde(x, h))
            elif (kde_type == 'triangular'):
                pdfs_for_all_x.append(triangular_kde(x, h))
            elif (kde_type == 'uniform'):
                pdfs_for_all_x.append(uniform_kde(x, h))

        sample_mean = np.mean(pdfs_for_all_x)
        sample_var = np.var(pdfs_for_all_x)

        percent_dev_mean = ((sample_mean - true_mean)*100)/true_mean
        percent_dev_var = ((sample_var - true_var)*100)/true_var

        print('\n h = ' + str(h))
        print('Percentage Difference w.r.t True Mean: ' + str(percent_dev_mean))
        print('Percentage Difference w.r.t True Variance: ' + str(percent_dev_var))
        pdfs_for_all_h_and_given_normal[h] = pdfs_for_all_x
    

    fig, plots = plt.subplots(2,3)

    fig.suptitle(kde_type + " KDE")

    i = 0
    j = 0;
    k = 0;
    for key in pdfs_for_all_h_and_given_normal.keys():
        plots[j][k].plot(Xs, pdfs_for_all_h_and_given_normal[key], 'b')
        plots[j][k].plot(Xs, pdfs_for_all_h_and_given_normal['original'], 'r')
        if key != 'original':
            plots[j][k].set_title("h = " + str(key))
        else:
            plots[j][k].set_title("Given Normal")
        k+=1
        if (k == 3):
            j+=1
            k = 0
        i+=1


if __name__ == "__main__":
    findAndPlotUsingKDE('normal')
    findAndPlotUsingKDE('triangular')
    findAndPlotUsingKDE('uniform')
    plt.show()
    