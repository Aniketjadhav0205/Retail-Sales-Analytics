from faker import Faker
import numpy as np
import pandas as pd
np.random.seed(42)
from datetime import date
from pathlib import Path


fake = Faker()

customers = []


regions=["Northeast", "Southeast","Midwest","West","Southwest"]

segments = ["VIP", "Regular", "New", "At-Risk"]   
segment_prob = [0.05, 0.70, 0.15, 0.10]                   


for i in range(10000):
    customer = {
        "customer_id": f"C{i+1:05d}",
        "name": fake.name(),
        "email": fake.email(),
        "region": np.random.choice(regions),
        "segment" :np.random.choice(                              
                   segments,
                   p=segment_prob                    # p decides how often each segment is selected
                                                     # VIP = 5%, Regular = 70%, New = 15%, At-Risk = 10%
                   ),                         
     "signup_date":fake.date_between(
                    start_date = date(2022,1,1),
                    end_date = date(2024,12,31)
                                   )
                }
    customers.append(customer)

# Add missing values
for col in ["region", "segment"]:
    mask = np.random.random(len(df)) < 0.05
    df.loc[mask, col] = np.nan

print("\nNull counts:")
print(df.isnull().sum())

df.to_csv(path / "customers.csv", index=False)




     


