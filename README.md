# DSI-group_project
## Group 6: Emily Fuller, Karthik Nambiar, David Wagenhurst, Vitoria Moreno-Costa

# Problem statement
Some states, including California, warn that living near an oil refinery can increase the risk of cancer. The Smith family is moving to Texas and looking for a new home in Houston. They are looking for information about the cancer rates in neighborhoods close to refineries compared to those in neighborhoods far from refineries. They are also interested in the relative economic health of those communities. We seek to help provide this information for the Smith family as they search for a new home.
 

# Table of Contents
DSI-group-project
- apps
    - presentation_app.py
    - requirements.txt
- Archive (individual team member's files - not needed to replicate analysis)
- cleaned_datasets
    - various datasets and shapefiles generated from notebook 01_Data_Collection_Cleaning
- datasets
    - raw datasets and shapefiles from sources listed in readme
- Notebooks
    - 01_Data_Collection_Cleaning.ipynb
    - 02_Data_GeoPandas_Shapefile.ipynb
- Link to Tableau.txt (link to the Tableau which uses the all_plus_facilities shapefile)

# Data and Steps

	We used the US Energy Information Administration as the source for US Petroleum Refineries locations in 2017, and the US Environmental Protection Agency (EPA)’s Toxic Release inventory as the source of other polluting facilities to serve as the basis for where the industrial pollution sources were. Then, we used the American Community Survey’s information on poverty and usage of the supplemental nutrition assistance program (SNAP) to help understand the economic geography of Texas and how it interacted with Texas. Then, we looked specifically at emissions of toxic chemicals from the 2017 EPA AirToxScreen to understand what chemicals were being emitted, what quantity for each census tract, and how that impacted cancer risks for inhabitants in each census tract. Finally, to tie this to our problem statement, we found the CDC tracker for cancer prevalence. 
	The most important part of our data cleaning was converting the refinery, industrial facility, and facility emissions latitude/longitude locations to tract numbers, as all of the other data sources had tract numbers. We were able to do this by developing a function that took the FCC API to convert coordinates to tract numbers, then grouping together refineries/pollutant facilities in the same census tract. For the other data sources, we filtered the columns down to only the Texas rows, then selected a few columns that were the most important in answering our questions, such as total cancer risk, cancer risk from industrial sources, emissions that we know come from refineries, other health risks, and economic qualities from the tracts. Then, we combined this dataset to the TIGER Texas Census tract shapefiles to create a geopanda database that we used to develop a Streamlit app [source](https://share.streamlit.io/dwagenhurst/streamlit-refineries/main/presentation_app.py) and Tableau visualization [source](https://public.tableau.com/app/profile/vitoria.moreno.costa/viz/TexasRefineriesandCancerRisk/Dashboard2?publish=yes).

# Software Requirements
- censusgeocode==0.5.2
- geopandas==0.9.0
- geopy==2.2.0
- numpy==1.20.3
- pandas==1.3.4
- streamlit==1.9.0


# Sources
- 2016 US Energy Information Administration, US Petroleum Refineries [source](https://koordinates.com/layer/13284-us-petroleum-refineries/)
- 2017 EPA AirToxScreen, [source](https://www.epa.gov/AirToxScreen/2017-airtoxscreen-assessment-results)
- 2019 ACS Supplemental Nutrition Assistance Program (SNAP): poverty levels, [source](https://data.census.gov/cedsci/map?q=Official%20Poverty%20Measure&g=0100000US%241400000&y=2019&tid=ACSST5Y2019.S2201&cid=S2201_C01_001E&vintage=2019&layer=VT_2019_140_00_PY_D1&mode=thematic&loc=38.7098,-94.3102,z8.0000)
- 2018 CDC Environmental Public Health Tracking Network, Crude Cancer Prevalence and Life Expectancy, [source](https://ephtracking.cdc.gov/DataExplorer/?c=11)
- 2017 EPA Toxic Release Inventory (TRI), [source](https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-present)
- Refinery Pollutants and their Effect on Public Health- The Public Health Advocate [source](https://pha.berkeley.edu/2021/04/11/refinery-pollutants-and-their-effect-on-public-health/#:~:text=These%20invisible%20fumes%20creep%20into,difficulty%20breathing%2C%20and%20blood%20disorders)
- CA Prop 65 [source](https://www.p65warnings.ca.gov/fact-sheets/petroleum-products-environmental-exposure-refineries#:~:text=Various%20chemicals%20in%20petroleum%20products,defects%20or%20other%20reproductive%20harm.&text=Acetaldehyde%20may%20increase%20the%20risk,the%20development%20of%20the%20child.)
- Welcome to “Cancer Alley,” Where Toxic Air Is About to Get Worse- Pro Publica  [source](https://www.propublica.org/article/welcome-to-cancer-alley-where-toxic-air-is-about-to-get-worse) 


