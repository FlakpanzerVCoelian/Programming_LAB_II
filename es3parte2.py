import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset
 
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()
 
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
 
#1
avg=df[["job_country","salary_year_avg"]]
avg=avg.dropna()
print(avg)
 
#2
job_counts = df.groupby('job_country')['job_title_short'].value_counts()
print(job_counts)
 
#3
interval = df.groupby("job_country")["salary_hour_avg"].agg(["min","max"])
print(interval)
 
#4
paesi = df['job_country'].unique()
for paese in paesi:
    dati_paese = df[df['job_country'] == paese]
    dati_lavoro= dati_paese-groupby("job_title_short")["salary_year_avg"].mean()
    dati_lavoro.plot(kind="barh")
    plt.title('Salario medio per lavoro in {}'.format(paese))
    plt.xlabel('Titolo di lavoro')
    plt.ylabel('Stipendio medio')
    plt.show()