import pandas as pd

data = {
    "name": ["Ram", "Shyam", "Hari", "Sita"],
    "age": [20, 21, 22, 23],
    "marks": [80, 55, 90, 70]
}

df = pd.DataFrame(data)

#print dataframe
print(df)
print()

#show ony names and marks
print(df[["name", "marks"]])
print()

#show students with marks>70
print(df[df["marks"] > 70])
print()


#add column "status": Pass if marks>=60 else Fail
import numpy as np
df["status"]=np.where(df["marks"]>=60, "Pass","Fail")
print(df)
