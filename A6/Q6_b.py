import numpy as np
import pandas as pd

data = pd.read_csv('q6.csv', header = None)
prior_prob_values = [0.1, 0.3, 0.5, 0.8]

def calculate_hypotheses_for_prior(p):
    selected_hypotheses = []
    
    #each column contains an instance of w. get the w array and map decisions
    for j in range(len(data.columns)):
        
        w_array_in_col_j = data.iloc[:, j]
        selected_hypotheses.append(MAP_descision(w_array_in_col_j, p))
    
    #print results
    print('For P(H_0) = ' + str(p) + 
          ', the hypotheses selected are ::', selected_hypotheses)
    
def MAP_descision(w, p):
    #by default C = 1
    C = 1
    
    #given mean = 0.5, sigma power 2 = 1.0
    mean = 0.5
    sigma_power_2 = 1.0
    
    #test condition rhs we derived in a part for H_0 or C = 0
    test_condition_rhs = ( sigma_power_2 / (2 * mean) ) * np.log( p/(1-p) )
    
    #if np.sum(w) <= test condition_rhs holds then C = 0 or H_0 is true
    if np.sum(w) <= test_condition_rhs:
        C = 0
    
    #return C
    return C

def main():
    #for each prior value repeat the experiment
    for prior in prior_prob_values:
        calculate_hypotheses_for_prior(prior)
  
if __name__ == "__main__":
    main()
    