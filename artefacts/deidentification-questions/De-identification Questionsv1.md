## Overview of the App
Welcome to D.I.F. a web-application to guide you through the process of de-identifying your data for release. The application is unique as it does not require you to input your study data but rather uses information such as the column names and characteristics of the dataset to provide recommendations.

## 0. Data Inventory
**Description:** Identify the types of data and the data fields that need to be de-identified.

### 0.1 Question
**Question:** Do any fields contain unique identifiers?<br>
**Type:** True/False<br>
**Help Tip:** A unique identifier is a piece of information assigned to an individual that is distinct and specific to them. Examples of a unique identifier are customer ID, membership number or account number.

### 0.2 Question
**Question:** Please select all the direct-identifiers present in dataset?<br>
**Type:** Multiple Choice<br>
**Help Tip:**  A direct-identifier can be used to directly identify an individual with no other information, these include, passport numbers, Medicare numbers, or email addresses.

### 0.3 Question
**Question:** Please select all the geographic attributes present in dataset?<br>
**Type:** Multiple Choice<br>
**Help Tip:**  Fields that might indicate geographic locations like addresses, postal codes, or city names.

### 0.4 Question
**Question:** Please select all the time related information present in dataset?<br>
**Type:** Multiple Choice<br>
**Help Tip:** Time related information includes attributes that record when events occurred or when data points were collected.

### 0.5 Question
**Question:** Please select all the information related to financial transactions present in dataset?<br>
**Type:** Multiple Choice<br>
**Help Tip:** Fields related to financial transactions, insurance information, billing records, etc.

### 0.6 Question
**Question:** Please select all the demographic information present in dataset?<br>
**Type:** Multiple Choice<br>
**Help Tip:** Fields such as age, gender, ethnicity, etc.

### 0.7 Question
**Question:** Are there any free-text or narrative fields?<br>
**Type:** True/False<br>
**Help Tip:** Fields that might contain unstructured or semi-structured data, such as medical notes or comments.

