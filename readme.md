##Weather Prediction Python Application

This is a python application that takes in weather data for a particular location over a 5 year period. The location chosen for this project is Colorado Springs, respresented by the latitude and longitude. The starting date is 09/30/2024 and the program takes in 5 years of previous data. The data is aggregated functions are applied to the data to give the sum, minimum, maximum, and average for 3 variables. Those variables are temperature, wind, and precipitation. To store the data, a database is creataed using SQLAlchemy and it sets up an in memory SQLLite DB. The table is then created and the data is populated to the table. A method query is made to see the insertion of the data was successful. Once that is done, a unittest is done on 3 tests to show that the API is pulling the correct data. 


##Installation
