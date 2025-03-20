import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
list1=[]
def probality():
    head=1
    tail=0
    for i in range(0,10000):
        random.randint(0,1)
        if random.randint(0,1)==1:
            head+=1
    total=head/10000
    print(total)
    print(head)

probality()

