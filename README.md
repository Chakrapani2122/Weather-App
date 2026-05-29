# 🌦️ Weather App

A beautiful, feature-rich desktop weather application built with Python and Tkinter that provides real-time weather information using the OpenWeatherMap API.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Setup and Configuration](#setup-and-configuration)
- [Usage](#usage)
- [Architecture and Code Overview](#architecture-and-code-overview)
- [Features in Detail](#features-in-detail)
- [Screenshots](#screenshots)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Current Weather Display
- **Real-time Temperature**: Displays current temperature in Celsius with live updates
- **Weather Description**: Shows current weather conditions (Clear, Cloudy, Rainy, etc.)
- **Location Information**: Displays user's current location (State/Country) using IP geolocation
- **Digital Clock**: Real-time clock display in the top-right corner
- **Current Date**: Shows today's date and day of the week

### Detailed Weather Metrics
- **Wind Speed**: Current wind speed in meters/second
- **Humidity**: Current humidity percentage
- **Pressure**: Atmospheric pressure in hectopascals (hPa)
- **UV Index (UVI)**: UV radiation index for sun protection guidance
- **Dew Point**: Dew point temperature in Celsius
- **Visibility**: Visibility distance in meters

### Sunrise and Sunset Information
- **Sunrise Time**: Displays local sunrise time
- **Sunset Time**: Displays local sunset time
- **Visual Icons**: Sun icons for easy identification

### Hourly Forecast
- **10-Hour Forecast**: Displays temperature, time, and weather description for the next 10 hours
- **Color-Coded Display**: Purple background for easy distinction from other sections
- **Live Updates**: Updates every hour with new forecast data

### 3-Day Daily Forecast
- **Extended Forecast**: Shows temperature and weather conditions for the next 3 days
- **Day Names**: Displays the day of the week for each forecast
- **Dark Background**: Contrast-rich display for readability

### Visual Elements
- **Application Icon**: Custom logo at the top-left corner
- **Weather Icons**: Dynamic weather condition icons downloaded from OpenWeatherMap
- **Color-Coded Sections**: Different background colors for different information sections
- **Professional UI Design**: Clean, modern interface with proper spacing and typography

## 📁 Project Structure

```
Weather-App/
├── weather-app.py          # Main application file
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── icon.png                # Downloaded weather icon (generated at runtime)
├── assets/                 # Static assets directory
│   ├── logo.png            # Application logo
│   ├── sunrise.png         # Sunrise icon
│   └── sunset.png          # Sunset icon
├── App1.png                # Screenshot 1
└── App2.png                # Screenshot 2
```

## 🔧 Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux with graphical display
- **Internet Connection**: Required for API calls and IP geolocation
- **API Key**: OpenWeatherMap API key (free tier available)

## 💻 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Chakrapani2122/Weather-App.git
cd Weather-App
```

### Step 2: Install Python
Ensure you have Python 3.8+ installed. Download from [python.org](https://www.python.org/)

### Step 3: Install Required Dependencies
```bash
pip install requests geocoder
```

Or install all dependencies using a requirements file:
```bash
pip install -r requirements.txt
```

## ⚙️ Setup and Configuration

### Obtaining an OpenWeatherMap API Key

1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to your API keys section
4. Copy your API key
5. Update the `weather-app.py` file:

```python
# Line 49 in weather-app.py
api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
```

### API Key Placement
The API key should be replaced in the `get_Weather()` function:

```python
def get_Weather():
    g = geocoder.ip('me')
    cordinates = g.latlng
    global geo_position
    geo_position = cordinates
    api_key = "YOUR_API_KEY_HERE"  # ← Replace this with your API key
    lat = cordinates[0]
    lon = cordinates[1]
    url1 = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    # ... rest of the function
```

## 🚀 Usage

### Running the Application

```bash
python weather-app.py
```

The application will:
1. Detect your location using IP geolocation
2. Fetch current weather data from OpenWeatherMap API
3. Display a beautiful GUI window with weather information
4. Continuously update the clock and weather data

### Window Overview

The application window (1035x665 pixels) is divided into several sections:

- **Top Section (Dark Blue)**: Current temperature, location, time, and weather icon
- **Left Section (Blue)**: Detailed weather metrics (wind, humidity, pressure, UVI, etc.)
- **Middle Section (White)**: Sunrise and sunset information
- **Right Section (Dark)**: 3-day forecast
- **Bottom Section (Purple)**: Hourly forecast for the next 10 hours

## 🏗️ Architecture and Code Overview

### Main Components

#### 1. **Window Setup**
```python
window = Tk()
window.geometry("1035x665")
window.configure(bg="#FFFFFF")
window.title("Weather App")
```
Creates the main window with fixed dimensions and white background.

#### 2. **Canvas for UI Elements**
```python
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=665,
    width=1035,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
```
Uses Tkinter Canvas to draw rectangles and create the background color sections.

#### 3. **API Call Function** (`get_Weather()`)
- Gets user's coordinates using IP geolocation via `geocoder` library
- Makes API call to OpenWeatherMap API with coordinates
- Parses JSON response and stores data globally

#### 4. **Update Functions**
The application uses scheduled update functions that refresh data periodically:
- `update_clock()`: Updates every 100ms
- `update_temperature()`: Updates every 100ms
- `update_weather_desc()`: Updates every 100ms
- `update_wind_speed()`: Updates every 100ms
- `update_humidity()`: Updates every 100ms
- `update_pressure()`: Updates every 100ms
- `update_uvi()`: Updates every 100ms
- `update_dewpoint()`: Updates every 100ms
- `update_visibility()`: Updates every 100ms
- `update_hourly_forecast()`: Updates every 3600000ms (1 hour)
- `update_daily_forecast()`: Updates every 3600000ms (1 hour)

Each update function uses Tkinter's `.after()` method to schedule recursive updates.

#### 5. **UI Layout**
All UI elements are positioned using absolute positioning with `.place()`:
- Labels for text display
- PhotoImage for icon display
- Color-coded rectangles for section backgrounds

### Key Dependencies

- **tkinter**: GUI framework (built-in with Python)
- **requests**: HTTP library for API calls
- **geocoder**: Geolocation library for IP-based location
- **urllib**: For downloading weather icons
- **json**: For parsing API responses
- **datetime**: For date/time formatting

## 📊 Features in Detail

### Weather Data Displayed

#### Current Weather Section
| Parameter | Unit | Description |
|-----------|------|-------------|
| Temperature | °C | Current ambient temperature |
| Weather | - | Current weather condition |
| Wind Speed | m/s | Speed of wind |
| Humidity | % | Percentage of moisture in air |
| Pressure | hPa | Atmospheric pressure |
| UVI | Index | UV radiation intensity |
| Dew Point | °C | Temperature at which dew forms |
| Visibility | m | Distance of clear visibility |
| Sunrise | HH:MM | Time of sunrise |
| Sunset | HH:MM | Time of sunset |

#### Forecast Data
- **Hourly**: 10-hour forecast with time, temperature, and weather description
- **Daily**: 3-day forecast with day name, temperature, and weather condition

### Data Update Intervals
- **Clock, Temperature, Weather**: Every 100ms (real-time)
- **Hourly/Daily Forecast**: Every 1 hour
- **All Other Metrics**: Every 100ms

### Color Scheme
| Section | Background Color | Text Color | Purpose |
|---------|-----------------|-----------|---------|
| Top/Right | #0F0C29 (Dark) | #FFFFFF (White) | Current weather |
| Left | #0575E6 (Blue) | #FFFFFF (White) | Detailed metrics |
| Center | #FFFFFF (White) | #000000 (Black) | Sunrise/Sunset |
| Bottom | #41295A (Purple) | #FFFFFF (White) | Hourly forecast |

## 📸 Screenshots

The project includes two screenshot files:
- **App1.png**: Main application interface showing the complete weather dashboard
- **App2.png**: Alternative view or different weather condition display

To view the screenshots:
1. Open `App1.png` and `App2.png` in the project root directory
2. They showcase the application's UI and how weather information is presented

## 📦 Dependencies

### Core Libraries
- **tkinter** (v8.6+): Graphical User Interface
  - Provides: Tk, Canvas, Entry, Text, Button, PhotoImage, Label
  - Built-in with Python on most systems

- **requests** (v2.25+): HTTP library for making API requests
  ```bash
  pip install requests
  ```

- **geocoder** (v1.38+): Geolocation based on IP address
  ```bash
  pip install geocoder
  ```

### Standard Libraries (included with Python)
- **pathlib**: File path operations
- **math**: Mathematical functions (floor)
- **urllib**: URL handling and downloading
- **time**: Time-related functions
- **json**: JSON parsing
- **datetime**: Date and time handling

### Complete Requirements File
Create a `requirements.txt` file:
```
requests>=2.25.0
geocoder>=1.38.0
```

Install all requirements:
```bash
pip install -r requirements.txt
```

## 🔍 Troubleshooting

### Issue: "Error: Please check your internet connection"
**Cause**: API request failed or no internet connection
**Solution**:
1. Check your internet connection
2. Verify your API key is correct
3. Ensure OpenWeatherMap API is accessible
4. Check that you haven't exceeded your API rate limit

### Issue: "ModuleNotFoundError: No module named 'requests'"
**Solution**:
```bash
pip install requests
```

### Issue: "ModuleNotFoundError: No module named 'geocoder'"
**Solution**:
```bash
pip install geocoder
```

### Issue: Application window doesn't display
**Cause**: No graphical display available
**Solution**:
- If running remotely, set up X11 forwarding
- Ensure you're running on a system with a display server

### Issue: Weather icons not loading
**Cause**: Icon download failed or file permission issue
**Solution**:
1. Check internet connection
2. Ensure write permissions in the application directory
3. Verify the assets folder is readable

### Issue: API returns "Invalid API Key"
**Solution**:
1. Verify you've correctly replaced "YOUR_API_KEY_HERE" in the code
2. Get a new API key from OpenWeatherMap
3. Ensure your API key is still valid and not expired

### Issue: Location showing as None or incorrect
**Cause**: Geocoding service temporarily unavailable
**Solution**:
1. Check internet connection
2. Try running the application again
3. Allow a few seconds for geolocation to complete

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Potential Improvements
- Add city/location search functionality
- Implement weather alerts
- Add weather history tracking
- Support for different units (Fahrenheit, mph)
- Dark mode and light mode themes
- Weather maps and radar
- Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ You can use this software for any purpose
- ✅ You can modify the source code
- ✅ You can distribute the software
- ✅ You can include it in proprietary applications
- ⚠️ You must include the license and copyright notice

## 🙏 Acknowledgments

- **OpenWeatherMap**: Providing comprehensive weather data and API
- **Python Tkinter**: For the GUI framework
- **Geocoder Library**: For IP-based geolocation
- **Community Contributors**: For feedback and improvements

## 📧 Support

For issues, questions, or suggestions:
1. Open an issue on GitHub
2. Check existing issues for similar problems
3. Include details about your operating system and Python version
4. Provide error messages or screenshots when applicable

---

**Created by**: Chakrapani2122  
**Last Updated**: 2024  
**Repository**: [Weather-App on GitHub](https://github.com/Chakrapani2122/Weather-App)