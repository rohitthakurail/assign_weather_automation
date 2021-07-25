# assign_weather_automation
Requirement:
Phase 1:
1. Use any UI automation tool to automate https://weather.com/
2. Reach the Search City or Postcode section of the website
3. Use the Search City or Postcode section to search the City or Postcode & select the searched city(example city is Delhi).

Phase 2:
1.Use any API listed here (https://openweathermap.org/current) to get the current weather data for any city. No need to subscribe to any service.
You can use your own API ID.
2. Automate the above REST API using any Rest client 

Phase 3:
1. Create a comparator that matches the temperature information from the UI in phase1 against the API response(ensure both are using the same temperature unit) in phase 2
2. Build a variance logic(should be configurable) that returns a success if temperature difference is within a specified range, else return a matcher exception

Environment Setup:

Required Packages needs to be install for executing the project.
1. requests (2.26.0)
2. selenium (3.141.0)

Assumption:
1. User is providing the input in JSON format.
2. User providing input through console.
3. App ID of openweathermap is hardcoded (as of now it's mine)
4. First matching city in search result taken as provided city.
5. Temperatur Unit is Celsius.
6. calculating variance % wrt UI Temperature values.
7. Using only chrome browser.

Implementation:
1. Take Input from User as JSON
2. Searched location for provided city on weather.com.
3. Read and stored the UI Temperature for the selected city.
4. Get the Temperature value of provided city from openweathermap API.
5. Getting Difference of the both temperature values.
6. Comparing the actual variance and allowed variance
7. if actual variance is in allowed variance range return True else return False

Note: Required Output will print in Console only. 
