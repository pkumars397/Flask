import pandas as pd

var=pd.DataFrame([1,2,3,4])

var.to_csv("sample.csv",index=False,header=None)