# TVD_Associates
This project aims to calculate the engagement score of association members using various parameters. The engagement score is a metric that measures the level of involvement and participation of members in the association's activities and events.

## Data Preprocessing

The project includes a data preprocessing step to clean and prepare the data for analysis. The key steps involved are:

1. **Reading the Input Data**: The input data is read from an Excel file located at a specified file path.
2. **Data Type Conversion**: Necessary data type conversions are performed, such as converting the 'Date Registered' column to datetime format and calculating the number of days registered.
3. **Feature Engineering**: New features are created from the existing data, such as concatenating name columns, creating a 'Member Type' column with assigned weights, and converting categorical columns to binary values.
4. **Handling Missing Values**: Appropriate techniques are used to handle missing values in the dataset.

## Engagement Score Calculation

The engagement score for each association member is calculated using a weighted scoring formula that considers various factors. The formula used in this project is:

```
score = Discount Code + Museum-Out + Opt Out + Days_Registered + Amount Paid + Member Type + Address Main + Zip
```

The individual components in the formula contribute differently to the overall engagement score.

## Data Analysis

After calculating the engagement scores, the project performs further analysis on the data:

1. **Scaling the Scores**: The scores are scaled using a StandardScaler to have a mean of zero and a standard deviation of 1 for easier analysis.
2. **Score Distribution Visualization**: A Kernel Density Estimation (KDE) plot is used to visualize the distribution of the scores. The plot shows that the scores are slightly skewed to the right and concentrated around 2.
3. **Top 20% Organizations**: The project identifies the top 20% of organizations based on the average engagement score of their members. A bar plot is generated to visualize these top organizations.
4. **Organization Counts**: The project calculates the count of occurrences for each organization name in the dataset.

## Zip Code Visualization

This Python script reads a GeoJSON file containing zip code boundaries and creates an interactive choropleth map to visualize the zip code data. The map is centered on the United States and displays zip codes as colored markers based on a count value associated with each zip code.

## Features

- **Data Processing**: The script filters the input GeoJSON data based on the zip codes present in a provided DataFrame.
- **Choropleth Map**: A choropleth map layer is added to the Folium map, representing each zip code as a colored marker based on the associated count value.
- **Centroid Calculation**: For each zip code, the script calculates the centroid coordinates using the provided geometry information.
- **Marker Customization**: The markers on the map are customized with colors (red or blue) based on the count value, and tooltips are added to display the zip code and count information.
- **Map Export**: The final map is saved as an HTML file (`filtered_choropleth_map.html`) for easy viewing and sharing.

##Contributors:
- Parag Gupta (Team Lead)
- Saksham Gupta
- Linda Jiang
- Kenneth Kenou
