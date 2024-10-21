from weather import Weather  # Make sure this matches the filename of your Weather class

def main():
    # Create an instance of the Weather class
    weather = Weather(38.8339, -104.8214, 9, 30, 2024)

    # Call methods to get the average temperature, wind speed, and precipitation
    avg_temp = weather.temp_data()
    max_wind = weather.wind_data()
    avg_precip = weather.precip_data()

    # Print the results
    print(f"5-Year Average Temperature: {avg_temp:.2f}°F")
    print(f"5-Year Max Wind Speed: {max_wind:.2f} mph")
    print(f"5-Year Total Precipitation: {avg_precip:.2f} inches")

if __name__ == "__main__":
    main()