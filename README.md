### Introduction

Beach Bliss Adventures & Insurance aims to optimize its vacation planning services and insurance packages, including unique coverage like shark attack insurance. 

To accurately price these insurance packages, we identified several hypotheses to test and analyze:

Sharks attack younger individuals more frequently than older.
The frequency of shark attacks differs between males and females.
Shark attacks occur more frequently in the USA compared to other countries in the world.
There are more fatalities than injuries in the world 
Surfing is the most dangerous activity

### Source
The dataset in the provided link [https://www.sharkattackfile.net/spreadsheets/GSAF5.xls] is a log of shark attack incidents compiled by the Global Shark Attack File (GSAF). It records various details about each shark attack incident, and the entries typically include information like: 

  
Date: when the shark attack occurred.
Country: where the shark attack took place.
Age: of victim, if available.
Activity: what the victim was engaged in at the time of the attack (e.g., swimming, surfing, diving).
Injury: fatal or non-fatal
Species: type of shark


Since the data was in an Excel spreadsheet, we needed to use a function from the Pandas library to read the file using the read_excel method. We were then able to read and manipulate the data in Python as a dataframe. 

We also needed to import seaborn in order to create charts and plots in Python.

## Data Analysis 

To address our hypotheses, we employed various data analysis techniques, including statistical testing, activity specific trend analysis, and demographic segmentation. Our rationale for selecting these methods is grounded in their ability to uncover patterns and correlations within the data that directly inform our insurance pricing strategy.

1)Data Import 2)Data Cleaning 3)Data Standardization 4) Data Filtering



During the Data Cleaning process we discoverd several irrelevant columns of information that were not pertinant to our Business Plan that we deleted. 




## Insights and Recommendations

Our analysis yielded several clear insights:

Age Factor: Younger individuals are more frequently targeted by sharks, suggesting age-based adjustments in insurance rates.
Gender Differences: There are notable differences in shark attack rates between males and females, necessitating gender-specific risk assessments.
Injury Types: Fatalities constitute 9% of all injuries, with leg injuries being the most common.
Activity Risks: Activities such as surfing, swimming, and diving were identified as the most dangerous, highlighting the necessity for activity-specific insurance packages.
Geographic Variation: The frequency of shark attacks is significantly higher in the United States, justifying location-based insurance pricing.

## Commitment to Continuous Improvement
By leveraging these insights, Beach Bliss Insurance demonstrates an exceptional commitment to driving continuous improvement and innovation in its service offerings. The actionable recommendations derived from our data analysis not only enhance the precision of our insurance pricing but also improve overall customer satisfaction and safety.


## Source: 
https://www.sharkattackfile.net/spreadsheets/GSAF5.xls

The dataset in the provided link is a log of shark attack incidents compiled by the Global Shark Attack File (GSAF). This dataset records various details about each shark attack incident, and the entries typically include information like:



[Notebook on GitHub] (https://docs.google.com/presentation/d/1hsMnwhCPld-1M7v_hPyn1199BGjw2ZxJBo6nrpb4zZE/edit?usp=sharing)

