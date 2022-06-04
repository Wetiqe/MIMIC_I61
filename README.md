# Predicting Mortality Rate Among Non-traumatic Intracerebral Haemorrhage Patients in Intensive Care Unit (ICU) Using MIMIC-IV Dataset

## Introduction
This is a project for the course 'foundation to data science' at University of Birmingham. 

The team memebers includes: Jianzhang Ni, Jiahui An, Arjun Dave, Yihe(Kathrynn) Zhang.

The project is hosted on GitHub at :https://github.com/Wetiqe/MIMIC_I61, the contributors are corresponding team members. 

The data we used is from MIMIC-IV, the doucment of the database can be found at https://mimic.mit.edu/docs/iv/. MIMIC-IV is not a public available database, they have the following requirments:

* Become a credentialed user on PhysioNet. This involves completion of a training course in human subjects research.
* Sign the data use agreement (DUA). Adherence to the terms of the DUA is paramount.

Our credentialed account is owned by Jianzhang Ni, and the cridential approvement can be found at `./etc/physionet_credential.png`. 

We download the data locally and select the data of our interest based on their document. We are only able to share part of this dataset through the Google Drive :  https://drive.google.com/drive/folders/12Z7bGPTRHWv0kEGcOkqH7kCf7XNEqJCf?usp=sharing


## Project Structure
The original dataset is too large for GitHub repo, so here only contains the code. To make sure the notebook works properly, your working directory should structured as following:

```
MIMIC/
├── analysis
│   ├── etc
│   │   ├── feature_meanings.csv
│   │   ├── lr_feature_importance.html
│   │   └── physionet_credential.png
│   ├── I61.ipynb
│   └── README.md
└── data
    ├── core
    │   ├── admissions.csv
    │   └── patients.csv
    ├── ed
    │   └── vitalsign.csv
    ├── hosp
    │   ├── diagnoses_icd.csv
    │   └── d_icd_diagnoses.csv
    ├── icu
    │   ├── chart_event_filtered.csv
    │   ├── d_items.csv
    │   └── icustays.csv
    └── LICENSE.txt


```

### Analysis folder
`I61` is the main notebook, contains the code we are going to submit. 
The `archive` folder contains the codes we don't modify anymore.

### Data folder
The data is available on the Google Drive: https://drive.google.com/drive/folders/12Z7bGPTRHWv0kEGcOkqH7kCf7XNEqJCf?usp=sharing

The MIMIC dataset is a restricted data source,  all manipulation must follow the instructions in the `LICENSE.txt`. In short, you can't share the code with anyone else, especially on the Internet

# Code for Filtering Data in Chartted Event Table
## Select data from Google Bigquery
We select chart event data from Google Bigquery using SQL, this command took about 15 mins to run. 

``` python
for i in range(5):
    sql = f"""SELECT * 
    FROM `physionet-data.mimic_icu.chartevents`
    WHERE subject_id in {tuple(cohort.index[497*i:497*(i+1)].values.tolist())}
    ORDER BY subject_id"""

    df = pd.read_gbq(sql, project_id='focus-dragon-313813', dialect='standard', use_bqstorage_api=True)
    df.to_csv(f'df{i}.csv')
```
## Pre-filtering
The last command returns milions of rows of data, it is too large for pandas to process, so we won't run it in the notebook. We filtered the items that occurs more than 2 thousands times and saved it as 'chart_event_filtered.csv' which will be placed in `data/icu` folder. 

``` python 
import dask.dataframe as dd
dd_df = dd.read_csv('*.csv')

from dask.distributed import Client
client = Client(n_workers=8, threads_per_worker=4, processes=True, memory_limit='8GB')

df1=dd_df.drop_duplicates(['subject_id','itemid'], keep='first')
df1 = df1.categorize(columns=['itemid'])

item_array = df1.itemid.value_counts().compute()
feature2k=item_array[item_array>2000]

df2 = df1[df1.itemid.isin(feature2k.index)]
df2.compute().to_csv('chart_event_filtered.csv')
``` 

# Code for Model Interpretation
Logistic regression and random forest are interpretable model, however this interpretation and visualization is somehow complicated. And the introduced libary might cause incompatable problems as well, so we put the code we used here and save the correponding results. 
## Logistic Regression
``` python
import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(logreg).fit(X_test_std, y_test)
html = eli5.show_weights(perm, feature_names=list(model_df.columns))

with open('./etc/lr_feature_importance.html','w') as f:
    f.write(html.data)
```

# REFERENCES


Cordonnier, C., Demchuk, A., Ziai, W., & Anderson, C. S. (2018). Intracerebral 
    haemorrhage: current approaches to acute management. The Lancet, 
    392(10154), 1257–1268. https://doi.org/10.1016/s0140-6736(18)31878-6

Carolei, A., Marini, C., di Napoli, M., di Gianfilippo, G., Santalucia, P., Baldassarre, M., 
    Giorgio De Matteis, & di Orio, F. (1997). High Stroke Incidence in the Prospective Community-Based L’Aquila Registry (1994–1998). Stroke, 28(12),         2500–2506. https://doi.org/10.1161/01.str.28.12.2500

Hemphill, J. C., Bonovich, D. C., Besmertis, L., Manley, G. T., & Johnston, S. C. (2001). 
    The ICH Score. Stroke, 32(4), 891–897. 
    https://doi.org/10.1161/01.str.32.4.891

Godinjak, A. G. (2016). Predictive value of SAPS II and APACHE II scoring systems for 
    patient outcome in medical intensive care unit. Acta Medica Academica, 45(2), 89–95.
    https://doi.org/10.5644/ama2006-124.165

Lee, H., Lim, C. W., Hong, H. P., Ju, J. W., Jeon, Y. T., Hwang, J. W., & Park, H. P. 
    (2015). Efficacy of the APACHE II Score at ICU Discharge in Predicting Post-ICU Mortality and ICU Readmission in Critically Ill Surgical Patients.          Anaesthesia and Intensive Care, 43(2), 175–186. 
     https://doi.org/10.1177/0310057x1504300206

Nie, X., Cai, Y., Liu, J., Liu, X., Zhao, J., Yang, Z., Wen, M., & Liu, L. (2021). Mortality 
    Prediction in Cerebral Hemorrhage Patients Using Machine Learning Algorithms in Intensive Care Units. Frontiers in Neurology, 11.               
    https://doi.org/10.3389/fneur.2020.610531

Rahmani, F., Rikhtegar, R., Ala, A., Farkhad-Rasooli, A., & Ebrahimi-Bakhtavar, H. 
    (2018). Predicting 30-day mortality in patients with primary intracerebral hemorrhage: Evaluation of the value of intracerebral hemorrhage and  
    modified new intracerebral hemorrhage scores. Iranian journal of neurology, 17(1), 47–52.

Rajashekar D, Liang JW. Intracerebral Hemorrhage. [Updated 2022 Feb 10]. In: 
    StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2022 Jan-. 
    Available from: https://www.ncbi.nlm.nih.gov/books/NBK553103/


Tatlisumak, T., Cucchiara, B., Kuroda, S., Kasner, S. E., & Putaala, J. (2018). 
    Nontraumatic intracerebral haemorrhage in young adults. Nature Reviews Neurology, 14(4), 237–250. https://doi.org/10.1038/nrneurol.2018.17

Van Asch, C. J., Luitse, M. J., Rinkel, G. J., van der Tweel, I., Algra, A., & Klijn, C. J. 
    (2010). Incidence, case fatality, and functional outcome of intracerebral haemorrhage over time, according to age, sex, and ethnic origin: a    
    systematic review and meta-analysis. The Lancet Neurology, 9(2), 167–176. 
    https://doi.org/10.1016/s1474-4422(09)70340-0

Vilela P, Wiesmann M. Nontraumatic Intracranial Hemorrhage. 2020 Feb 15. In: Hodler 
    J, Kubik-Huch RA, von Schulthess GK, editors. Diseases of the Brain, Head and 
    Neck, Spine 2020–2023: Diagnostic Imaging [Internet]. Cham (CH): Springer; 2020. 
    Chapter 5. Available   from:https://www.ncbi.nlm.nih.gov/books/NBK554334/ doi: 10.1007/978-3-030-38490-6_5

 
