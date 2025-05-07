import pandas as pd
import os

data={
    'Name':["Alice","Garv","Gaurav"],
    'Age':[25,30,35],
    'Location':["America","Kurukshetra","Pehowa"]
}

df=pd.DataFrame(data)



data_dir='data'

os.makedirs(data_dir,exist_ok=True)


file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f" CSV File saved to {file_path}")


