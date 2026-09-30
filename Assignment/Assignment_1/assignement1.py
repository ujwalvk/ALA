import math
import sys
from typing import Self
""""
A custom vector class to implement mean, de-meaned vectors and stdandard deviation 
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements
    def mean(self):
        """
        compute arithmetic mean of the vector
        """
        if len(self.elements)==0:
            raise ValueError("Empty vector")
        return sum(self.elements)/len(self.elements)
    
    def demean(self):
        """
        Calculates the de_mean by subtracting the mean from each element of the vector
        """
        mean_value = self.mean()
        new_ele = tuple(x-mean_value for x in self.elements)
        return Vec(new_ele)
    def std(self):
        """
        computes sqrt(average((x - mean)^2)) for a given vector
        """
        demeaned = self.demean()
        squared = tuple(x**2 for x in demeaned.elements)
        return math.sqrt(sum(squared)/len(squared))
    
    def __repr__(self):
        return repr(self.elements)

if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")
if __name__ == "__main__":
    v1 = Vec((12, 32))

    print("Vector:", v1)
    print("Mean:", v1.mean())
    print("Demean:", v1.demean())
    print("Standard Deviation:", v1.std())