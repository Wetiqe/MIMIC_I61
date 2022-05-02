# MIMIC I61
This repo contains the code for analyzing patients diagnosed with I61 from the MIMIC dataset.

The description of the dataset can be found here: https://mimic.mit.edu/docs/iv/

The introduction part of the dataset can be found here: https://docs.google.com/document/d/1ONcyFMzL23E_rYXxZ-wL-KQrthpftzEQxCRKOMPKvYQ/edit

If you don't know how to work with GitHub, you can check my blog here:

Use Git locally: https://www.wetiqe.xyz/use-git-locally-45b823846203432282684393866ea36d00

Use GitHub: https://www.wetiqe.xyz/github-bb2f0ed1ff664eeaa227e0bfafd0995d
## Guidelines for reviewers and authors
https://mimic.mit.edu/docs/community/guidelines/
Authoring or reviewing a MIMIC paper can be challenging due to the complex nature of the data. Our recommendations for authors when writing papers, or for reviewers when reviewing papers, are:

The version of MIMIC should be specified. For example: MIMIC-III v1.4, or MIMIC-IV v1.0. If researchers are using an older version, inquire as to why.
* It is easy to conflate an ICU admission with a hospital admission. Ensure that it is clear.
* Mortality is a common outcome, but can be defined in a number of ways. Some researchers define 30-day mortality from admission, whereas others define it from discharge. Ensure the manuscript is clear. We recommend using 30-days from admission, as this better reflects the severity of illness of the patient on admision to the ICU.
* Avoid vague criteria. For example, “removed patients missing data” is unclear, whereas “removed patients with no heart rate measurements in the first 24 hours of their stay” is much more interpretable.
* Verify that the MIMIC data citation is referenced, and for MIMIC-III that the paper is also cited. See the acknowledgement page for details.
* Most of important of all, code should be included with the paper. The MIMIC data use agreement requires researchers to publish code with their paper, and there is no substitute for code in explicitly describing the methodology. e.g. guidelines for reviewers.

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
Hadm ID: Hospital stays are identified and tracked by the HADM ID, or hospital admission ID

icd_code: International Classification of Diseases (ICD) is used to identify the CODED CLINICAL ENTRY

icd_Version: Version of International Classification of Diseases (ICD)

Anchor_year: Is de identified year occurring sometime between 2100 - 2200, 

anchor_year_group: is a three year long date ranges between 2008 - 2019. For example, if a patient's anchor_year is 2158, and their anchor_year_group is 2011 - 2013 then any hospitalizations for the patient occurring in the year 2158 actually occurred sometime between 2011 - 2013

anchor_age: provides the age of the patient in the given anchor_year

Dod: date of death

Stay_id: unique id to patient ward stay

Temperature: body temperature of the patient during icu stay

Heart rate: heart rate of the patient during icu stay

Resperate: respiratory rate of the patient during icu stay

O2sat: oxygen saturation (amount of oxygen travelling through your body with your red blood cells)

Sbp: systolic blood pressure (pressure caused by your heart contracting and pushing out blood)

Dbp: diastolic blood pressure (the pressure in the arteries when the heart rests between beats

Verbal response:

Sodium: Amount of blood sodium level in a patient

Chloride: Amount of blood chloride level in a patient

Magnesium: Amount of blood magnesium level in a patient

Creatine: Amount of blood creatinine level in a patient

## Modelling
### For Assignment
K-means, logistic regression, (multiple linear regression)

### Further analysis
DNN, KNN, RF, GBDT, SVM, LR 


## REFERENCES


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

 
