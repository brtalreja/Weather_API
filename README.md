# Weather API

## Overview

This Python script fetches and displays weather data for a given city using the OpenWeatherMap API. The user inputs the city's name, latitude, longitude, and their own OpenWeatherMap API key to retrieve and display the current temperature, minimum temperature, and maximum temperature for the day.

## Features

- Retrieves weather data using the OpenWeatherMap API.
- Simple command-line interface for user input.
- Displays current temperature, minimum temperature, and maximum temperature for the specified city.
- More features can be added on a need basis.

## Getting Started

### Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

### Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/brtalreja/Weather_API.git
    cd Weather_API
    ```

2. Run the script:

    ```bash
    python Weather_API.py
    ```

3. Follow the prompts to enter the city name, latitude, longitude, and OpenWeatherMap API key.

### Example

1. Run the script:

    ```bash
    python Weather_API.py
    ```

2. Follow the prompts to enter the following details:

    ```
    Please enter the name of the city you want to check the weather for.
    Ibiza
    Please enter the latitude of the city you want to check the weather for.
    39.0200
    Please enter the longitude of the city you want to check the weather for.
    1.4821
    Please enter your weather API ID.
    My_API_ID
    ```

3. The script will fetch the weather data and display the results:

    ```
    In Ibiza, the temperature today is 12.0°C
    In Ibiza, today's lowest temperature is 12.0°C
    In Ibiza, today's highest temperature is 13.0°C
    ```

This example demonstrates how the user can input the city name, latitude, longitude, and API key to obtain the current temperature, minimum temperature, and maximum temperature for the specified city.

## Configuration

Make sure to obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and set it in the script.

```python
weather_api_id = "YOUR_API_KEY_HERE"
```

## References

This project was created following the guidance of the LinkedIn Learning course:

- **Instructor:** Nick Walter
