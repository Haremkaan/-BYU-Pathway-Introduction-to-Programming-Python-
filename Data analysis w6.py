# W06 Project: Life Expectancy Data Analysis

# Added Feature:
# 1. User can input a year to see average, min, and max life expectancy for that year.
# 2. User can also input a country name to see its average, minimum, and maximum life expectancy across all years.

filename = "life-expectancy.csv"

with open(filename) as file:
    next(file)  # Skip header line

    # Variables for overall data
    lowest = 9999.0
    highest = 0.0
    lowest_country = ""
    highest_country = ""
    lowest_year = ""
    highest_year = ""

    # Store all data for later analysis
    data = []

    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        data.append((country, year, life_expectancy))

        # Overall lowest and highest
        if life_expectancy < lowest:
            lowest = life_expectancy
            lowest_country = country
            lowest_year = year

        if life_expectancy > highest:
            highest = life_expectancy
            highest_country = country
            highest_year = year

print(f"The overall max life expectancy is: {highest} from {highest_country} in {highest_year}")
print(f"The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}")

# --- Year-specific analysis ---
year_of_interest = input("\nEnter the year of interest: ")

total = 0
count = 0
year_min = 9999.0
year_max = 0.0
min_country = ""
max_country = ""

for country, year, life_expectancy in data:
    if year == year_of_interest:
        total += life_expectancy
        count += 1

        if life_expectancy < year_min:
            year_min = life_expectancy
            min_country = country

        if life_expectancy > year_max:
            year_max = life_expectancy
            max_country = country

if count > 0:
    avg = total / count
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg:.2f}")
    print(f"The max life expectancy was in {max_country} with {year_max}")
    print(f"The min life expectancy was in {min_country} with {year_min}")
else:
    print(f"No data found for the year {year_of_interest}.")

# --- Country-specific analysis (creative feature) ---
country_of_interest = input("\nEnter a country of interest (optional): ").strip().title()

if country_of_interest:
    total = 0
    count = 0
    country_min = 9999.0
    country_max = 0.0
    min_year = ""
    max_year = ""

    for country, year, life_expectancy in data:
        if country == country_of_interest:
            total += life_expectancy
            count += 1

            if life_expectancy < country_min:
                country_min = life_expectancy
                min_year = year

            if life_expectancy > country_max:
                country_max = life_expectancy
                max_year = year

    if count > 0:
        avg = total / count
        print(f"\nFor {country_of_interest}:")
        print(f"The average life expectancy across all years was {avg:.2f}")
        print(f"The max life expectancy was {country_max} in {max_year}")
        print(f"The min life expectancy was {country_min} in {min_year}")
    else:
        print(f"No data found for {country_of_interest}.")
