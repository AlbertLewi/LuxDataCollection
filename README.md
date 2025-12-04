# LuxDataCollection
Python code library for a group project that I am currently working on. Code is designed to be modular and easy to use. Provided is a test example using random numbers. 
Code Structure:
- Connects to Arduino through comport
- Collects 10 raw analog data readings from a light sensor
- Uses sensor resistance to calculate lux value
- Appends list of lux values with lux value
- Returns the average of the list after 10 collections
- Appends CSV with lux value and other relevent project data

Calibration:
- Parameters in lux equation were played around with until lux readings roughly matched the readings from a lux detection app on my phone.
- Lux data is generally accurate to the order of magnitude, and is generally off within a range of +/- 5 to 20
