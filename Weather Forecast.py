# Created By Samyak Bumb
import weather_forecast as wf

location=input("Enter Location Here :")

print('Displaying Weather report for: ' + location)

Weather= wf.forecast(place = location)

print(Weather)