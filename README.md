# MIMIC I61
This repo contains the code for analyzing patients diagnosed with I61 from the MIMIC dataset.

The description of the dataset can be found here: https://mimic.mit.edu/docs/iv/

The introduction part of the dataset can be found here: https://docs.google.com/document/d/1ONcyFMzL23E_rYXxZ-wL-KQrthpftzEQxCRKOMPKvYQ/edit

If you don't know how to work with GitHub, you can check my blog here:

Use Git locally: https://www.wetiqe.xyz/use-git-locally-45b823846203432282684393866ea36d00

Use GitHub: https://www.wetiqe.xyz/github-bb2f0ed1ff664eeaa227e0bfafd0995d

# Project Structure
The original dataset is too large for GitHub repo, so here only contains the code. To make sure the notebook works properly, your working directory should structured as following:
```
.
├── analysis
│   ├── archive
│   │   ├── cohort_selection.ipynb
│   │   └── example_pipeline.ipynb
│   ├── I61.ipynb
│   └── README.md
└── data
    ├── chart_event_filtered.csv
    ├── core
    │   ├── admissions.csv
    │   ├── patients.csv
    │   └── transfers.csv
    ├── ed
    │   └── vitalsign.csv
    ├── hosp
    │   ├── diagnoses_icd.csv
    │   └── d_icd_diagnoses.csv
    ├── icu
    │   ├── chart_event.csv
    │   ├── d_items.csv
    │   ├── icustays.csv
    │   ├── outputevents.csv
    │   └── procedureevents.csv
    └── LICENSE.txt

```

## Analysis folder
`I61` is the main notebook, contains the code we are going to submit. 
The `archive` folder contains the codes we don't modify anymore.

## Data folder
The data is available on the Google Drive. However `chart_event.csv` is too large for Google Drive, so you might not have a copy now, if you need it, let me know. 

The MIMIC dataset is a restricted data source,  all manipulation must follow the instructions in the `LICENSE.txt`. In short, you can't share the code with anyone else, especially on the Internet. 

# Introduction

Descriptions about I61

Stroke is a major health problem faced by people from all around the globe. Nontraumatic intracerebral haemorrhage (ICH) is a subtype of stroke with a condition where hematoma is formed within the brain parenchyma with or without blood extension into the ventricles (Rajashekar & Liang 2022). ICH affects more than 2 million people in a year and accounts for up to 10–15% of all strokes (Cordonnier et al., 2018; Vilela & Wiesmann, 2020), with long term morbidity and high mortality rate compared to other types of strokes (Tatlisumak et al., 2018). According to Carolei et al. (1997) and Van Asch et al. (2010), approx 35% of ICH patients die within seven days and around 50% within 30 days. Moreover, the global cost of caring for ICH patients is enormous, particularly for those in intensive care units (ICUs). Therefore it becomes important to predict the mortality rate among ICH patients as early as possible.

One of the important scoring methods to determine the mortality rate among ICH patients is the ICH score (Hemphill et al., 2001). This ICH score can be calculated in the first minute of the patient's visit by taking the patient's level of consciousness based on the Glasgow Coma Scale (GCS), haemorrhage volume (cm3), presence or absence of intraventricular haemorrhage, haemorrhage site (supra or infratentorial), and patient's age (Rahmani et al., 2018). However, the limitation of the ICH score is that it needs to be assessed by experienced radiologists and neurologists, leading to high cost, high time consumption and difficult for inexperienced people to use (Nie et al., 2021). Moreover, Acute Physiology and Chronic Health Evaluation (APACHE) II and Simplified Acute Physiology Score (SAPS) II are effective methods to predict the mortality rate in general ICU patients (Lee et al., 2015; Godinjak et al., 2016). These scores use conventional statistical analysis to identify the most relevant covariates from a set of features preselected by domain experts; leading to oversimplification and discretization of model and reduced covariates and deterioration of the model performance (Nie et al., 2021).

# Analysis

## Selected Features

## Feature Engineering

## Data Description

## Modelling
### For Assignment
K-means, logistic regression, (multiple linear regression)

### Further analysis
DNN, KNN, RF, GBDT, SVM, LR 






 
