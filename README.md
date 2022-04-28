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
│   │   ├── cohort_selection
│   │   └── example_pipeline
│   ├── I61
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
    │   ├── d_hcpcs.csv
    │   ├── diagnoses_icd.csv
    │   ├── d_icd_diagnoses.csv
    │   ├── d_icd_procedures.csv
    │   ├── d_labitems.csv
    │   ├── drgcodes.csv
    │   ├── hcpcsevents.csv
    │   ├── procedures_icd.csv
    │   └── services.csv
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

We might not use the data in `hosp` folder, could be removed in the next version. 

# Introduction

Descriptions about I61

# Analysis

## Selected Features

## Feature Engineering

## Data Description

## Modelling
### For Assignment
K-means, logistic regression, (multiple linear regression)

### Further analysis
DNN, KNN, RF, GBDT, SVM, LR 






 
