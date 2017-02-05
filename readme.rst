Mean and Standrd Deviation Readme
=================================

The :ref:`code-label` takes as input an **array** :math:`x_{i,j}` and an **axis**. 
It returns mean and standard deviation for all elements along the chosen **axis**. 
If **axis** is ``0``, then functions operates on rows, if **axis** is ``1`` then it operates on columns. 
If **axis** is ``None`` than mean and standard deviation of all elements is calculated.

The mean is found by using the following function (assuming **axis** ``0``):

.. math::
   \mu_j = \frac{1}{N} \sum_{i=0}^{N}x_{i,j}

And the standard deviation is found by:

.. math::
   \sigma_j = \sqrt{\frac{1}{N} \sum_{i=0}^{N} (x_{i,j} - \mu)^2}
