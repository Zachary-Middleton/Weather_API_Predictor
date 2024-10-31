##Weather Prediction Python Application

This is a python application that takes in weather data for a particular location over a 5 year period. The location chosen for this project is Colorado Springs, represented by the latitude and longitude. The starting date is 09/30/2024 and the program takes in 5 years of previous data. The data is aggregated functions are applied to the data to give the sum, minimum, maximum, and average for 3 variables. Those variables are temperature, wind, and precipitation. To store the data, a database is created using SQLAlchemy, and it sets up an in memory SQLLite DB. The table is then created and the data is populated to the table. A method query is made to see the insertion of the data was successful. Once that is done, a unittest is done on 3 tests to show that the API is pulling the correct data. 


##Installation

Clone the repository from GitLab
Install the required packages using pip: pip install - requirements.txt
Run the application: python main.py

##Usage
Since the application takes in the latitude, longitude, day, month, and year. To customize to any location and any lenth of time, update those parameters. Then in the main.py file, update any variable/method that has a hardcoded date.

##Contributing
To add to this project, simply follow the steps below:
- Fork the repository
- Create a new branch for your changes
- Make your changes and commit them to your branch
- Submit a pull request to the original repository
