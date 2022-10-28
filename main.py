import numpy as np
import mean_var_std

def calculate(list):
  if(len(list)!=9):
    raise ValueError('List must contain nine numbers.')

  ls= np.array(list)
  ls=ls.reshape(3,3)
  
  #mean of rows & colums:
  mnr=[ls[0,:].mean(),ls[1,:].mean(),ls[2,:].mean()]
  mnc=[ls[:,0].mean(),ls[:,1].mean(),ls[:,2].mean()]
  
  #Variance of rows and columns:
  varr=[ls[0,:].var(),ls[1,:].var(),ls[2,:].var()]
  varc=[ls[:,0].var(),ls[:,1].var(),ls[:,2].var()]
  
  #Standard deviation of rows and columns:
  stdr=[ls[0,:].std(),ls[1,:].std(),ls[2,:].std()]
  stdc=[ls[:,0].std(),ls[:,1].std(),ls[:,2].std()]

  #Finding Max value:
  maxr=[ls[0,:].max(),ls[1,:].max(),ls[2,:].max()]
  maxc=[ls[:,0].max(),ls[:,1].max(),ls[:,2].max()]

#Finding Min value:
  minr=[ls[0,:].min(),ls[1,:].min(),ls[2,:].min()]
  minc=[ls[:,0].min(),ls[:,1].min(),ls[:,2].min()]
  
  #Finding Sum:
  sumr=[ls[0,:].sum(),ls[1,:].sum(),ls[2,:].sum()]
  sumc=[ls[:,0].sum(),ls[:,1].sum(),ls[:,2].sum()]
  
  return{
    'mean': [mnc,mnr,ls.mean()],
    'variance': [varc,varr,ls.var()],
    'standard deviation': [stdc,stdr,ls.std()],
    'max': [maxc,maxr,ls.max()],
    'min': [minc,minr,ls.min()],
    'sum': [sumc,sumr,ls.sum()]
  }
  
print(calculate([0,1,2,3,4,5,6,7,8]))
