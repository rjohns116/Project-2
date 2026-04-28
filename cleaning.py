#Step 1: load in the data to a dataframe from csv
import numpy as np
import pandas as pd

audiovisual = pd.read_csv("/workspaces/Project-2/data/original/Audiovisual.csv")
radio = pd.read_csv("/workspaces/Project-2/data/original/Radio.csv")
television = pd.read_csv("/workspaces/Project-2/data/original/Television.csv")


#Step 2: Inspection (repeat for tv, radio, audiovisual)
# Get a look at the dataframe
# Note what needs to be changed

#File 1: Audiovisual data

#Find out how the data is structured
audiovisual.head(20)

#Size of the dataframe
audiovisual.shape

#Get a look at column names
audiovisual.columns

#Understand data types for each column
audiovisual.info()

#Understand the categories in different categorical variables
audiovisual["Service Type"]
audiovisual["Market"]

##Look for outliers 
audiovisual[" Total Quarterly Hours "].sort_values()


#File 2: Radio

#Find out how the data is structured
radio.head(20)

#Size of the dataframe
radio.shape

#See column names
radio.columns

#See datatypes for each column
radio.info()

#See categorical values for different categorical variables
radio["Market"].unique()
radio["Service Type"].unique()
radio["Broadcast Language"].unique()

#File 3: Television

#Find out how the data is structured
television.head(20)

#Size of the dataframe
television.shape

#See column names
television.columns

#See datatypes for each column
television.info()

#See categorical values for different categorical variables
television["Market"].unique()
television["Service Type"].unique()
television["Broadcast Language"].unique()

# Step 3: Data cleaning - transform each dataframe according to notes 

# Audiovisual

#Convert column names to snake_case
audiovisual.columns = [column_name.strip().replace(" ","_") for column_name in audiovisual.columns]

#Convert all "-" with various spacing to pd.NA
audiovisual = audiovisual.replace(r"^\s*-\s*$", pd.NA, regex=True)

#Convert Broadcast_Quarter to int
audiovisual["Broadcast_Quarter"] = (audiovisual["Broadcast_Quarter"]
                                    .str.strip()
                                    .str.extract(r"(\d)$")
                                    .astype(int)
)

#Convert Total_Quarterly_Hours to int
audiovisual["Total_Quarterly_Hours"] = (audiovisual["Total_Quarterly_Hours"]
                                        .str.replace(",","")
                                        .str.strip()
                                        .astype(int)
)

# Radio

#Remove whitespace from all columns and convert to snake_case
radio.columns = [column_name.strip().replace(" ","_") for column_name in radio.columns]

#Convert all "-" with various spacing to pd.NA
radio = radio.replace(r"^\s*-\s*$", pd.NA, regex=True)

#Convert "Broadcast_Quarter" to "int" type
radio["Broadcast_Quarter"] = (radio["Broadcast_Quarter"]
                              .str.strip()
                              .str.extract(r"(\d)$")
                              .astype(int)
)

#Convert "Total_Quarterly_Hours" to "int" type
radio["Total_Quarterly_Hours"] = (radio["Total_Quarterly_Hours"]
                                  .str.strip()
                                  .str.replace(",","")  
                                  .astype("Int64")                            
)

#Convert "Universe" to "int" type









# Television



# Step 4: Save as a cleaned file













