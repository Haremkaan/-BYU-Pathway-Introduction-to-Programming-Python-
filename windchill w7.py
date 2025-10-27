# W07 Project: Windchill
# Author: [Haremkaan Michael Torkuma]
# Description: Calculates wind chill values for a range of wind speeds
# using functions for conversion and computation.

def celsius_to_fahrenheit(temp_c):
    """Convert Celsius temperature to Fahrenheit."""
    return (temp_c * 9 / 5) + 32

def wind_chill(temp_f, wind_speed):
    """Compute wind chill based on temperature (°F) and wind speed (mph)."""
    w = 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))
    return w

def main():
    temp = float(input("Enter the temperature: "))
    unit = input("Is this in Fahrenheit or Celsius (F/C)? ").strip().lower()

    if unit == "c":
        temp_f = celsius_to_fahrenheit(temp)
    else:
        temp_f = temp

    print(f"\nTemperature in Fahrenheit: {temp_f:.2f}°F")

    print("\nWind Speed (mph) | Wind Chill (°F)")
    print("-----------------|----------------")
    for speed in range(5, 65, 5):
        wc = wind_chill(temp_f, speed)
        print(f"{speed:>16} | {wc:>14.2f}")

if __name__ == "__main__":
    main()
