def importing_data (url):
    df = pd.read_excel(url)
    return(df)

def df_clean_up (df_input):
    df = df_input.copy()
    # 2(1)
    df.drop(columns=["pdf"], inplace = True) 
    df.drop(columns=["href formula"], inplace = True)
    df.drop(columns=["href"], inplace = True)
    df.drop(columns=["Source"], inplace = True)
    df.drop(columns=["Unnamed: 21"], inplace = True)
    df.drop(columns=["Unnamed: 22"], inplace = True)
    df.drop(columns=["Unnamed: 11"], inplace = True)
    df.drop(columns=["Case Number.1"], inplace = True)
    df.drop(columns=["original order"], inplace = True)
    df.drop(columns=["Case Number"], inplace = True)
    df.drop(columns = ["Name"], inplace = True)
    df.drop(columns = ["Time"], inplace = True)
    # 2(2)
    df.dropna(how = "all", inplace = True) #We use this formula to get rid of all rows that solely contain null values
    # 2(3)
    df.dropna(subset = "Age", inplace = True)
    pd.set_option('display.max_rows', 50)

    return df




def df_formating(df_input):
    df = df_input.copy()
# 3(1)
    df.columns = [i.replace(" ","").lower() for i in df.columns]
# 3(2)
    # Convert the 'Date' column to datetime format
    # Replace 'Date' with the actual name of the date column in your DataFrame
    # Assuming the date format is "02 Mar-2024"
    df["date_clean"] = pd.to_datetime(df['date'], format='%d-%b-%Y', errors='coerce')
    df.sample(50)
    df = df.dropna(subset=["date_clean"])
    # Display the DataFrame with the converted 'Date' column
    print("\nDataFrame with 'Date' column in datetime format:")
    #print(df)
    # Define the date range
    start_date = '1843-01-01'
    end_date = '1980-12-31'
    # Convert dates to datetime format
    start_date = pd.to_datetime(start_date,format="%Y-%m-%d")
    end_date = pd.to_datetime(end_date,format="%Y-%m-%d")
    # Filter out rows within the date range
    df_filtered = df[((df['date_clean'] >= end_date))]
    # to view updated data frame
    df_filtered.head(100)
 # 3(3)
    sexes = {" M": "M", "M ": "M", "lli":"other", "M x 2": "M", "N":"M", ".":"other"}
    df["sex"] = df["sex"].replace(sexes)
    types = {" Provoked": "Provoked", "Questionable": "Unconfirmed", "?": "Unconfirmed", "Unverified":"Unconfirmed", "Under investigation": "Unconfirmed", "Invalid": "Unconfirmed", "Boat": "Watercraft"}
    df["type"]=df["type"].replace(types)
 # 3(4)
    injury = {"FATAL": "FATAL", "fatal": "FATAL", "Fatal": "FATAL"}
    df["injury"] = df["injury"].replace(injury)
 # 3(5)
    activity = {"0": "Undetermined", }
    df["activity"] = df["activity"].replace(activity)
# 3(6)
    df["age"] = pd.to_numeric(df['age'], errors="coerce" )
# 3(7)
    for i in df:
      if df[i].dtype == "object":
         df[i] = df[i].str.strip()
      else:
         i
    pd.set_option('display.max_rows', 50)
    return df



def df_hypothesis_age(df_input):
    df = df_input.copy()
    grouped_age = df.groupby('age') #We group by age
    grouped_age_size = grouped_age.size().sort_values(ascending= False) #We use the size method to see the frequency of each element in the column
    dataframe_age = grouped_age_size.reset_index(name='size') #We create a new dataframe to see the results better
    sns.set(style="whitegrid")

    # Plotting the bar plot using catplot for better control over figure size
    age_chart = sns.catplot(
        x="age", 
        y="size", 
        data=dataframe_age, 
        kind='bar',
        height=10,      # Height of the plot
        aspect=3       # Aspect ratio (width/height)
    )
    # Set the axis labels and title

    age_chart.set_axis_labels("Size", "Age")
    age_chart.fig.suptitle("Age to shark attack relationship graph", y=1.02)

    # Plotting a smaller version of the graph with the most relevant numbers
    age_chart2 = sns.catplot(
        x="age", 
        y="size", 
        data=dataframe_age.head(10), 
        kind='bar',
        height=5,      # Height of the plot
        aspect=1       # Aspect ratio (width/height)
    )
    # Set the axis labels and title
    age_chart2.set_axis_labels("Age", "Size")
    age_chart2.fig.suptitle("Top 10 ages most likely to get attacked by a shark", y=1.02)
        
    return dataframe_age.head(10), age_chart, age_chart2


def df_hypothesis_sex(df_input):
    df = df_input.copy()
    grouped_sex = df.groupby('sex')
    grouped_sex_size = grouped_sex.size().sort_values(ascending= False)
    dataframe_sex = grouped_sex_size.reset_index(name='size')

    sns.set(style="whitegrid")
    sex_graph = sns.barplot(x="sex", y="size", data=dataframe_sex)
    sex_graph.set(xlabel='Sex', ylabel='Size', title='Shark attacks by sex')
    sns.despine()

    grouped_age_sex = df.groupby(["age", "sex"]) 
    grouped_age_sex_size = grouped_age_sex.size().sort_values(ascending= False)
    dataframe_age_sex = grouped_age_sex_size.reset_index(name='size') #We create a new dataframe to see the results better
    pd.set_option('display.max_rows', None)

    return display(dataframe_sex), display(sex_graph), display(dataframe_age_sex.head(50))#We want to see the 50 most common ages



def df_hypothesis_activity(df_input):
    df = df_input.copy()
    grouped_activity = df.groupby("activity")
    sorted_group_sizes = grouped_activity.size().sort_values(ascending=False)
    dataframe_activity = sorted_group_sizes.reset_index(name='size')
    pd.set_option('display.max_rows', None)
    
    activity_graph = sns.catplot(
    x="activity", 
    y="size", 
    data=dataframe_activity.head(10), 
    kind='bar',
    height=10,      # Height of the plot
    aspect=3      # Aspect ratio (width/height)
    )
    # Set the axis labels and title
    activity_graph.set_axis_labels("Activity", "Size")

    return display(dataframe_activity.head(25)), display(activity_graph)



def df_hypothesis_country_state(df_input):
    df = df_input.copy()
    #countries
    grouped_country = df.groupby('country') 
    grouped_country_size = grouped_country.size().sort_values(ascending= False)
    dataframe_country = grouped_country_size.reset_index(name='size') 
    pd.set_option('display.max_rows', None)
    
    #countries graph
    sns.set(style="whitegrid")
    country_graph = sns.catplot(
        x="country", 
        y="size", 
        data=dataframe_country.head(10), 
        kind='bar',
        height=5,      
        aspect=3 
    )
    country_graph.set_axis_labels("Country", "Size")

    #states
    grouped_state = df.groupby('state') 
    grouped_state_size = grouped_state.size().sort_values(ascending= False)
    dataframe_state = grouped_state_size.reset_index(name='size') 
    pd.set_option('display.max_rows', None)

    #states graph
    sns.set(style="whitegrid")
    state_graph = sns.catplot(
        x="state", 
        y="size", 
        data=dataframe_state.head(10), 
        kind='bar',
        height=5,      
        aspect=3 
    )
    state_graph.set_axis_labels("State", "Size")

    return display(dataframe_country.head(50),dataframe_state.head(50), country_graph, state_graph)



def df_hypothesis_injury(df_input):
    df = df_input.copy()
    grouped_injury = df.groupby('injury') 
    grouped_injury_size = grouped_injury.size().sort_values(ascending= False)
    dataframe_injury = grouped_injury_size.reset_index(name='size') 
    pd.set_option('display.max_rows', None)

    sns.set(style="whitegrid")
    injury_graph = sns.catplot(
        x="injury", 
        y="size", 
        data=dataframe_injury.head(10), 
        kind='bar',
        height=10,      
        aspect=3 )
    injury_graph.set_axis_labels("Injury", "Size")
    
    return display(dataframe_injury.head(50), injury_graph)



def df_hypothesis_fatal(df_input):
    df = df_input.copy()
    fatal_attacks = df[df["injury"] == "FATAL"] #We create a data frame that only contains rows with attacks that were FATAL

    grouped_inj_state_country = fatal_attacks.groupby(['injury', 'country', "state"])
    sorted_group_sizes = grouped_inj_state_country.size().sort_values(ascending=False)
    dataframe_inj_state_country = sorted_group_sizes.reset_index(name='size')
    pd.set_option('display.max_rows', None)
    
    return display(dataframe_inj_state_country.head(50))



def df_hypothesis_injury_country_state(df_input):
    df = df_input.copy()

    grouped_inj_state_country = df.groupby(['injury', 'country', "state"])
    sorted_group_sizes = grouped_inj_state_country.size().sort_values(ascending=False)
    dataframe_inj_state_country = sorted_group_sizes.reset_index(name='size')
    pd.set_option('display.max_rows', None)

    return display(dataframe_inj_state_country.head(50))


def df_hypothesis_type(df_input):
    df = df_input.copy()

    grouped_type = df.groupby('type') 
    grouped_type_size = grouped_type.size().sort_values(ascending= False)
    dataframe_type = grouped_type_size.reset_index(name='size') 
    pd.set_option('display.max_rows', None)
    
    return display(dataframe_type) 



