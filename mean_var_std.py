import numpy as np

def calculate(list):
  mylist=np.array(list)
  if len(mylist)!=9:
    raise ValueError("List must contain nine numbers.")

  else:
    mylist=mylist.reshape(3,3)
    mean1=np.mean(mylist,axis=0).tolist()
    mean2=np.mean(mylist,axis=1).tolist()
    mean=np.mean(mylist).tolist()

    var1=np.var(mylist,axis=0).tolist()
    var2=np.var(mylist,axis=1).tolist()
    var=np.var(mylist).tolist()

    std1=np.std(mylist,axis=0).tolist()
    std2=np.std(mylist,axis=1).tolist()
    std=np.std(mylist).tolist()

    max1=np.max(mylist,axis=0).tolist()
    max2=np.max(mylist,axis=1).tolist()
    max0=np.max(mylist).tolist()

    min1=np.min(mylist,axis=0).tolist()
    min2=np.min(mylist,axis=1).tolist()
    min0=np.min(mylist).tolist()

    sum1=np.sum(mylist,axis=0).tolist()
    sum2=np.sum(mylist,axis=1).tolist()
    sum0=np.sum(mylist).tolist()

    mydict= {
    'mean': [mean1, mean2, mean],
    'variance': [var1, var2, var],
    'std': [std1, std2, std],
    'max': [max1, max2, max0],
    'min': [min1, min2, min0],
    'sum': [sum1, sum2, sum0]
  }
  return mydict