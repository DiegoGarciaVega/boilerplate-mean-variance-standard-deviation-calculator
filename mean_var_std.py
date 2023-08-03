import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  aux = np.reshape(list, (3, 3)) # RESHAPE INTO 3X3 MATRIX

  calculations = {
    'mean': [
      aux.mean(axis=0).tolist(), # MEAN OF VERTICAL AXIS
      aux.mean(axis=1).tolist(), # MEAN OF HORIZONTAL AXIS
      aux.flatten().mean() # MEAN OF FLATTEN
    ],
    'variance': [
      aux.var(axis=0).tolist(), # VAR OF VERTICAL AXIS
      aux.var(axis=1).tolist(), # VAR OF HORIZONTAL AXIS
      aux.flatten().var() # VAR OF FLATTEN
    ],
    'standard deviation': [
      aux.std(axis=0).tolist(), # STD OF VERTICAL AXIS
      aux.std(axis=1).tolist(), # STD OF HORIZONTAL AXIS
      aux.flatten().std() # STD OF FLATTEN
    ],
    'max': [
      aux.max(axis=0).tolist(), # MAX OF VERTICAL AXIS
      aux.max(axis=1).tolist(), # MAX OF HORIZONTAL AXIS
      aux.flatten().max() # MAX OF FLATTEN
    ],
    'min': [
      aux.min(axis=0).tolist(), # MIN OF VERTICAL AXIS
      aux.min(axis=1).tolist(), # MIN OF HORIZONTAL AXIS
      aux.flatten().min()  # MIN OF FLATTEN
    ],
    'sum': [
      aux.sum(axis=0).tolist(), # SUM OF VERTICAL AXIS
      aux.sum(axis=1).tolist(), # SUM OF HORIZONTAL AXIS
      aux.flatten().sum() # SUM OF FLATTEN
    ]
  }
  return calculations
