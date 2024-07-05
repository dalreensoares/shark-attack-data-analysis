# Beach Bliss Adventures & Insurance

## Introduction

Beach Bliss Adventures & Insurance is dedicated to enhancing vacation planning services and providing comprehensive insurance packages, including unique coverage such as shark attack insurance. 

To accurately price these insurance packages, we identified five key hypotheses to test and analyze:

1. Sharks attack younger individuals more frequently than older individuals.
2. The frequency of shark attacks differs between males and females.
3. Shark attacks occur more frequently in the USA compared to other countries.
4. There are more fatalities than injuries globally.
5. Surfing is the most dangerous activity.

## Source

The dataset provided by the Global Shark Attack File (GSAF) is available [here](https://www.sharkattackfile.net/spreadsheets/GSAF5.xls). This dataset logs shark attack incidents and includes various details such as:

- Date of the occurrence
- Year of the occurrence
- Type of incident
- Country where the attack occurred
- State where the attack occurred
- Location of the attack
- Activity the victim was engaged in
- Name of the victim
- Sex of the victim
- Age of the victim, if available
- Injury details, including whether it was fatal or non-fatal
- Species of the shark
- Source of the information
- Unknown columns

We used the Pandas library in Python to read and manipulate this Excel data as a dataframe, employing the `read_excel` method. Additionally, we used the Seaborn library to create charts and plots for our analysis.

## Data Analysis

To address our hypotheses, we employed various data analysis techniques, including statistical testing, activity-specific trend analysis, and demographic segmentation. These methods help uncover patterns and correlations within the data that directly inform our insurance pricing strategy.

### Data Analysis Steps

1. **Data Import**
2. **Data Cleaning**
3. **Data Standardization**
4. **Data Filtering**

During the data cleaning process, we discovered and removed several irrelevant columns that were not pertinent to our business plan.

### Hypothesis Testing

#### Hypothesis 1: Age Factor

**Objective:** To identify the most common age among those who have been attacked by sharks.

**Hypothesis:** Sharks attack younger people more frequently than older individuals.

**Approach:**

- Clean the data (remove null and outdated data)
- Identify the most common age attacked by sharks
- Create a graph in Seaborn to visualize the data
- Narrow down to the top 15 age groups

**Results:**

- Shark attacks are most common in the 17-year-old cohort.
- 36% of attacks occur between the ages of 13 and 29.
- Based on this, the premium for this age bracket will be priced higher.


#### Hypothesis 2: Gender Differences

**Objective:** To identify the most common gender among those who have been attacked by sharks.

**Hypothesis:** There is a difference in shark attack rates between males and females.

**Approach:**

- Clean the data (remove null and outdated data)
- Create a table showing the relationship between age and gender
- Use DataFrame `groupby` gender and age
- Create a graph in Seaborn to visualize the data

**Results:**

- Males are attacked 2999 times (85%) compared to females, who are attacked 503 times (15%).
- The most attacked males are 17 years old (143 incidents).
- The most attacked females are 13 years old (28 incidents).

#### Hypothesis 3: Geographic Variation

**Objective:** To identify the most common country where shark attacks occur.

**Hypothesis:** There are more shark attacks in the USA than anywhere else in the world.

**Approach:**

- Clean the data (remove null and outdated data)
- Create a table showing the relationship between country and state by attacks
- Use DataFrame `groupby` country and size
- Create a graph in Seaborn to visualize the data

**Results:**

- The USA has 1615 attacks (45%), the most of any country.
- The next four countries (Australia, South Africa, Bahamas, and Brazil) combined have fewer attacks than the USA.

#### Hypothesis 4: Injury Types

**Objective:** To identify the most common injuries among those who have been attacked by sharks.

**Hypothesis:** There are more fatalities than injuries globally.

**Approach:**

- Clean the data (remove null and outdated data)
- Create a table showing the relationship between injuries in ascending order
- Use DataFrame `groupby` injury and size
- Create a graph in Seaborn to visualize the data

**Results:**

- There are 321 fatalities, constituting 9% of all injuries.
- Leg injuries are the most common among all injuries.

#### Hypothesis 5: Activity Risks

**Objective:** To identify the most dangerous activities among those who have been attacked by sharks.

**Hypothesis:** The most dangerous activities involve water sports.

**Approach:**

- Clean the data (remove null and outdated data)
- Create a table showing the relationship between activity and injury
- Use DataFrame `groupby` activity and size
- Create a graph in Seaborn to visualize the data

**Results:**

- Surfing injuries total 848, making it the most dangerous activity.
- Swimming injuries total 622.
- The top 5 most dangerous activities make up 56% of all injuries.

## Insights and Recommendations

Our analysis provided several clear insights:

- **Age Factor:** Younger individuals are more frequently targeted by sharks, suggesting age-based insurance rate adjustments.
- **Gender Differences:** Notable differences exist in shark attack rates between males and females, necessitating gender-specific risk assessments.
- **Injury Types:** Fatalities constitute 9% of all injuries, with leg injuries being the most common.
- **Activity Risks:** Surfing, swimming, and diving are the most dangerous activities, highlighting the need for activity-specific insurance packages.
- **Geographic Variation:** Shark attacks are significantly more frequent in the United States, justifying location-based insurance pricing.

## Commitment to Continuous Improvement

By leveraging these insights, Beach Bliss Insurance demonstrates a commitment to continuous improvement and innovation in its service offerings. The actionable recommendations derived from our data analysis enhance the precision of our insurance pricing and improve overall customer satisfaction and safety.

[Notebook on GitHub] (https://docs.google.com/presentation/d/1hsMnwhCPld-1M7v_hPyn1199BGjw2ZxJBo6nrpb4zZE/edit?usp=sharing)

