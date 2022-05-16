import numpy as np

def calculate(list):
  if (len(list) != 9):
    raise ValueError( "List must contain nine numbers.")
    
  lst = np.array(list)
  print(lst)
  
  rows_mean = [lst[[0,1,2]].mean(), lst[[3,4,5]].mean(), lst[[6,7,8]].mean()]
  cols_mean = ([lst[[0,3,6]].mean(),lst[[1,4,7]].mean(), lst[[2,5,8]].mean()])
  
  rows_var = [lst[[0,1,2]].var(),lst[[3,4,5]].var(), lst[[6,7,8]].var()]
  cols_var = ([lst[[0,3,6]].var(),lst[[1,4,7]].var(), lst[[2,5,8]].var()])
 
  rows_std = [lst[[0,1,2]].std(),lst[[3,4,5]].std(), lst[[6,7,8]].std()]
  cols_std = ([lst[[0,3,6]].std(),lst[[1,4,7]].std(), lst[[2,5,8]].std()])
 
  rows_max = [lst[[0,1,2]].max(),lst[[3,4,5]].max(), lst[[6,7,8]].max()]
  cols_max = ([lst[[0,3,6]].max(),lst[[1,4,7]].max(), lst[[2,5,8]].max()])
 
  rows_min = [lst[[0,1,2]].min(),lst[[3,4,5]].min(), lst[[6,7,8]].min()]
  cols_min = ([lst[[0,3,6]].min(),lst[[1,4,7]].min(), lst[[2,5,8]].min()])
   
  rows_sum = [lst[[0,1,2]].sum(),lst[[3,4,5]].sum(), lst[[6,7,8]].sum()]
  cols_sum = ([lst[[0,3,6]].sum(),lst[[1,4,7]].sum(), lst[[2,5,8]].sum()])
  
  return {
    "mean" : [cols_mean, rows_mean, lst.mean()],
    "variance" : [cols_var, rows_var, lst.var()],
    "standard deviation" : [cols_std, rows_std, lst.std()],
    "max" : [cols_max, rows_max, lst.max()],
    "min" : [cols_min, rows_min, lst.min()],
    "sum" : [cols_sum, rows_sum, lst.sum()]
  }