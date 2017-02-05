"""This is the answer to the quiz 3 containing a function
that takes two inputs: a dataset represented as a numpy-array,
and an axis argument. The function computes mean and standard deviation of a dataset 
along specified "axis".

"""

import numpy as np # numpy library is imported
# This library should be abbreviated as np for use in this program

def mean_std(arr,axis=0):
    """
    calculate mean and standard deviation of a numpy array along an axis.

    Parameters
    ----------
    arr : numpy array
    axis : {0,1,None}, optional

    Returns
    -------
    mu : numpy array (or a single number) of means.
    std : numpy array (or a single number) of standard deviations.
    full output : tuple(mu,std).

    Asserts
    -------
    axis is either 0,1 or None
        Because axis can not be any other values.
    axis is smaller or equal to the dimension of array
        Because mean or standard deviation can be found only along an existing dimension

    Notes
    -----
    Uses numpy library abbreviated as np.

    Examples
    --------
    >>> a = np.array([[1,2,3],[0,0,0],[-1,-2,-2]])
    >>> print(mean_std(a,1))
    (array([2., 0., -1.66666667]), array([0.81649658, 0., 0.47140452]))
    >>> print(mean_std(a))
    (array([0., 0., 0.33333333]), array([0.81649658, 1.63299316, 2.05480467]))
    >>> print(mean_std(a,None))
    (0.1111111111111111, 1.5947444549341472)
    """
    assert (axis==0 or axis==1 or axis==None), "axis can be either 0,1 or None"
    assert (axis==None or axis<=len(arr.shape)-1), "axis is bigger than the dimension of array"
	
    mu = np.mean(arr,axis=axis)
    std = np.std(arr,axis=axis)
    return mu,std
	
a = np.array([[1,2,3],[0,0,0],[-1,-2,-2]]) # Test array
print(mean_std(a,None)) # Output mean and standard deviation of all elements in array a