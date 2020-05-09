# Canola Oil Predictions
This project was an entry for a contest held by UCSD's Halıcıoğlu Data Science Institute in February 2020. This entry placed 8th out of over 500 submissions, and used multiple linear regression to predict 2019 canola oil prices and production in Canada, given a provided dataset.

## Data
The provided data included historical price and production from 2000-2018, as well as regional temperature, rain, and soil moisture data from 2000-2019. Each dataset is further subdivided into provinces of Canada. Samples of the price and temperature data are shown below:
![Price Data](price.png?raw=true "Prices")
![Temperature Data](temperature.png?raw=true "Temperature")

## Prediction Method
As can be seen above, the temperature (and other weather data) is cyclical. Clearly, a single regression line would not work for this data, so instead, we create 12 models each corresponding to a month to account for this periodicity.
