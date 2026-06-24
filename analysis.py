import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
file=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\SuperStoreOrders.csv")
script_dir=os.path.dirname(os.path.abspath(__file__))
save=os.path.join(script_dir,"Graphs and Charts")
if not os.path.exists(save):os.makedirs(save)
def Data_Assessment():
    print(file.head())
    print(file.size)
    print(file.dtypes)
    print(file.isnull().sum())      #No Null Values Found.
    print(file[file.duplicated()])  #No Duplicate Values Found.
Data_Assessment()
