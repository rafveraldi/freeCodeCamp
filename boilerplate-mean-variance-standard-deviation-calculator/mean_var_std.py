import numpy as np

def calculate(list):
  try:  
    a = np.array(list).reshape(3,3)  
    calculations = {
    'mean': [np.mean(a,axis=0).tolist(), np.mean(a,axis=1).tolist(), np.mean(a).tolist()],
    'variance': [np.var(a,axis=0).tolist(), np.var(a,axis=1).tolist(), np.var(a).tolist()],
    'standard deviation': [np.std(a,axis=0).tolist(), np.std(a,axis=1).tolist(), np.std(a).tolist()],
    'max': [np.max(a,axis=0).tolist(), np.max(a,axis=1).tolist(), np.max(a).tolist()],
    'min': [np.amin(a,axis=0).tolist(), np.amin(a,axis=1).tolist(), np.amin(a).tolist()],
    'sum': [np.sum(a,axis=0).tolist(), np.sum(a,axis=1).tolist(), np.sum(a).tolist()]
    }
  except:
    raise ValueError('List must contain nine numbers.')

  
  return calculations