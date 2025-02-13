import streamlit as st
import requests
import geocoder
import json
from datetime import datetime
from math import floor

# Function to get weather data
def get_weather(lat, lon):
    api_key = "your_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to get user's location
def get_location():
    try:
        g = geocoder.ip('me')
        return g.latlng
    except Exception:
        st.warning("Location not available.")
        return None

# Function to display weather data
def display_weather(data):
    current = data["current"]
    st.write(f"**Temperature:** {current.get('temp', 0)} °C")
    st.write(f"**Pressure:** {current.get('pressure', 0)} hPa")
    st.write(f"**Humidity:** {current.get('humidity', 0)}%")
    st.write(f"**Weather:** {current['weather'][0].get('description', 'N/A').title()}")
    st.write(f"**Wind Speed:** {current.get('wind_speed', 0)} meter/sec")
    st.write(f"**UVI:** {current.get('uvi', 0)}")
    st.write(f"**Dew Point:** {current.get('dew_point', 0)} °C")
    st.write(f"**Visibility:** {current.get('visibility', 0)} meter")
    st.write(f"**Sunrise:** {datetime.fromtimestamp(current['sunrise']).strftime('%I:%M %p')}")
    st.write(f"**Sunset:** {datetime.fromtimestamp(current['sunset']).strftime('%I:%M %p')}")

    st.write("### Hourly Forecast")
    for hour in data["hourly"][:10]:
        st.write(f"**Time:** {datetime.fromtimestamp(hour['dt']).strftime('%I:%M %p')}, **Temp:** {floor(hour['temp'])} °C, **Weather:** {hour['weather'][0]['main'].title()}")

    st.write("### Daily Forecast")
    for day in data["daily"][:3]:
        st.write(f"**Day:** {datetime.fromtimestamp(day['dt']).strftime('%A')}, **Temp:** {floor(day['temp']['day'])} °C, **Weather:** {day['weather'][0]['main'].title()}")

# Streamlit app layout
def main():
    st.title("Weather Forecast Application")
    st.write("Get the current weather information and forecast.")

    if st.button("Use My Location"):
        location = get_location()
        if location:
            try:
                data = get_weather(location[0], location[1])
                display_weather(data)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Could not retrieve location.")

if __name__ == "__main__":
    main()
