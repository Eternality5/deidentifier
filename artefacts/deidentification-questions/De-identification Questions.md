## Overview of the App
Welcome to D.I.F. a web-application to guide you through the process of de-identifying your data for release. The application is unique as it does not require you to input your study data but rather uses information such as the column names and characteristics of the dataset to provide recommendations.

## 0. Entering Column Names
**Description:** This section is simply about entering their column names and if known the researcher knows the type of column they are adding.

### 0.1 Question
**Question:** What are the names of the columns in the dataset?
**Type:** Multiple textbox input
**Help Tip:** The columns in the dataset are variables measured in the dataset, as opposed to the rows which could be each participant in the dataset.

### 0.2 Question
**Question:** Which of the columns are known quazi-identifiers?
**Type:** 
**Help Tip:** Quazi-identifiers are not directly identifying but they can be used in conjunction with other information to identify an individual. These include names, and post codes. If you are unsure if column is a quazi-identifier, there will be further question to provide clarification.

### 0.3 Question
**Question:** Which of the columns are know direct-identifiers?
**Help Tip:** A direct-identifier can be used to directly identify an individual with no other information, these include, passport numbers, Medicare numbers, or email addresses.

## 1. Persecutor Risk
**Description**: The following questions are relating to finding if the persecutor risk is applicable to the dataset. A persecutor risk is when the a person (the persecutor) is trying to identify specific individual that they know is in the dataset. The persecutor already has information about the person they are attempting to identify. 
**Source:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528029/
**Outcome:** If one of the following question is marked as true the dataset contains a persecutor risk. If there is a persecutor risk this needs to be managed and stricter recommendation will be given. The following article recommends using K-Anonymity when a persecutor threat is present, the disadvantage of this is it reduces the utility otherwise if no threat is present we will use a k-map instead, if possible.

### 1.1 Question 
**Question:** The dataset represents the whole population (e.g., a population registry, or census) or has a large sampling fraction?
**Type:** True/False
**Source:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528029/
**Help Tip:** If the whole population is being disclosed then the persecutor would have certainty that their target is in the disclosed dataset. Also, a large sampling fraction means that their target is very likely to be in the disclosed dataset.
**Outcome:** If This dataset has been flagged as having a persecutor risk.

### 1.2 Question
**Question:** It generally know who participated in the study, such as an internal survey for a single business?
**Type:** True/False
**Source:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528029/
**Help Tip:** The sample may be a dataset from an interview survey conducted in a company and it is generally known who participated in these interviews because the participants missed half a day of work. In such a case it is known within the company, and to an internal intruder, who is in the disclosed dataset.
**Outcome:** This dataset has been flagged as having a persecutor risk.

### 1.3 Question
**Question:** The individuals are likely to self-reveal that they are part of the sample? For example, subjects in clinical trials do generally inform their family, friends, and even acquaintances that they are participating in a trial.
**Type:** True/False
**Source:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528029/
**Help Tip:** Subjects in clinical trials do generally inform their family, friends, and even acquaintances that they are participating in a trial. One of the acquaintances may attempt to re-identify one of these self-revealing subjects. However, it is not always the case that individuals do know that their data is in a dataset. For example, for studies where consent has been waived or where patients provide broad authorization for their data or tissue samples to be used in research, the patients may not know that their data is in a specific dataset, providing no opportunity for self-revealing their inclusion.
**Outcome:** This dataset has been flagged as having a persecutor risk.

## 2. Identifying Quazi-identifiers
**Description:** The following questions are to determine the Quazi-identifiers and quazi-identifying sensitive columns. We will be able to infer information about the columns by using a preset group of known quazi-identifiers. It will also analyse the heightened risk of certain combinations of quazi-identifiers.
These questions will also help to identify quazi-identifiers that may have not previously been considered as a quazi-identifier.
**Source:** https://dataprivacylab.org/projects/identifiability/paper1.pdf
**Outcome:** Questions about K-Annonimity will only be asked in reference to the columns that are quazi-identifiers. The list of identified quazi-identifiers and quazi-identifying-sensitive columns will be included in the report.

### 2.1 Question
*Quazi-identifer Match*
**Condition:** A _column_name_ appears to match a column in our set of know quazi identifiers.
**Question:** Is the _column_name_ equivalent to _known_quazi-identifier_?
**Help Tip:** A quasi-identifier is a combination of attributes or variables that, on their own, might not directly identify an individual, but when combined with other information, could potentially lead to identification. Examples of quasi-identifiers in biomedical research might include age, gender, ethnicity, and postal code. These attributes, although not uniquely identifying an individual, can be used in combination to narrow down the possibilities and potentially re-identify someone.
**Type:** True/False
**Source:** The objective of this question is so a researcher can clarify that the automatic quazi identification system has worked as intended.
The known quazi-identifiers come from the following study.
https://dataprivacylab.org/projects/identifiability/paper1.pdf
**Outcome:** If yes the *column_name* will be added to the list of quazi-identifiers in the report.

### 2.2 Question
*Quazi-identifier definition match*
**Condition:** A _column_name_ appears to match a column in our set of know quazi identifiers.
**Question:** Does the content of _column_name_ match the following definition of the column _column_definition_?
**Source:** There is the potential that our understanding of a word is different to your understanding of a work, such as in the case of address, which could mean a street address or an email address. In the case of street address and email address, email address is a direct identifier and should be removed before release.
**Type:** True/False

### 2.3 Question
*Identifying Sensitive Information*
**Question:** Could any of the columns in your dataset reveal information about another column? Such as in the case of a diseases that is gender specific (prostate cancer), this would reveal the gender of the participant if this disease was include
**Source:** Quazi-identifiers can be infered from columns that may not normally be considered quazi-identifiers. These columns can be used to help identify an individul.  
**Source:** https://www.privitar.com/blog/k-anonymity-an-introduction/
**Type:** Drop Down of Column Names, and a plus for them to add multiple columns
**Outcome:** The report will explain that in order to suppress these columns both columns will need to be supressed otherwise the information can be implied from the other column.

## 3. Current K-Anonymity Value
**Description:** The following questions will be used to to determine if the characteristcs of their dataset that are related to K-Anonymity. 
**Outcome:** Depending on the answers to these questions we will know whether to recommend further deidentification.

### 3.1 Question
**Condition:** Selected false for all question in [[#1. Persecuter Risk]] (Relies on the abecence of a persecuter risk and assumes no membership knowledge)
**Question:** Is your given dataset a subset of a larger dataset?
**Source:** This question is to determine if the researcher has the resources required to use a K-map for their dataset. 
**Help Tip:** Is your dataset a subset of census data or do you posses a greater dataset that your participants are part of.

### 3.2 Question
**Condition:** Answered false to either  [[#3.1 Question]] or true to any of [[#1. Persecuter Risk]]
**Question:** What is the current K-Annonimity of the dataset?
**Type:** Number input
**Source:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528029/
**Help Tip:** K-Annonimity is the minimum number of unique combinations of quazi-identifers found in a dataset, if a single row has a unique combination quazi-identifiers, then the k-annonimity would be 1.
**Outcome:** If (the number is <=5) then the dataset in not sufficiently de-identified, and the data should be further de-identified using K-Annonimity
else the dataset is sufficiently de-identified.

### 3.3 Question
**Condition:** Answered false to all of [[#1. Persecuter Risk]] and true to [[#3.1 Question]]
**Question:** What is the K-Annonimity of the dataset when combined with the larger dataset.
**Type:** Number input
**Source:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2528029/
**Help Tip:** K-Annonimity is the minimum number of unique combinations of quazi-identifers found in a dataset, if a single row has a unique combination quazi-identifiers, then the k-annonimity would be 1.
**Outcome:** If (the number is <=5) then the dataset in not sufficiently de-identified, and the data should be further de-identified using the K-Map method
else the dataset is sufficiently de-identified
