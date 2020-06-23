import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = { 1: 'January', 2: 'February', 3: 'March', 
           4: 'April', 5: 'May', 6: 'June', 9: 'All' }
DAYS = {0: 'Monday', 1: 'Tuesday', 2: 'Wendesday', 
               3: 'Thursday', 4: 'Friday', 5: 'Saturday', 
               6: 'Sunday', 9: 'All'}

def get_city_name():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
    """   
    # get user input for city (chicago, new york city, washington). 
    while True:
        try:
            city = str(input('Would you like to see data for Chicago, New York, or Washington?\n'))
            if city.lower() in CITY_DATA:
                city = city.lower()
                break
            else:
                print('Your input does not seem right. Please try again.\n')
                continue
        except ValueError:
            print('Sorry, I didn\'t understand that. Please input one of the city names from chicago, new york, washington!')
            continue
        else:
            break
    print('\nIt seems you would like to see the data for {} city. If this is not true, please restart the program.\n\n'.format(city.title()))

    return city

def get_filter_on_month_or_day():
    """
    Asks user to whether they want to filter on month or day.

    Returns:
        (bool) limit_on_month - if they want to filter on month
        (bool) limit_on_day - if they want to filter on day of week
    """       
    limit_on_month = False
    limit_on_day = False
    while True:
        try:
            filter_or_not = str(input('Would you like to filter the data by month, day of week, or not at all?\nPlease enter \'month\', \'day\', \'both\', or \'none\'.\n'))
            filter_or_not = filter_or_not.lower()

            if filter_or_not=='month':
                limit_on_month = True
                break
            elif filter_or_not=='day': 
                limit_on_day = True
                break
            elif filter_or_not=='both': 
                limit_on_month = True
                limit_on_day = True
                break
            elif filter_or_not=='none': 
                break
            else:
                print('Your input does not seem right. Please try again.\n')
                continue
        except ValueError:
            print('Sorry, I didn\'t understand that. Please enter month, day, both, or none!')
            continue
        else:
            break    
    print('Your input is {}.\n\n'.format(filter_or_not.title()))

    return limit_on_month, limit_on_day

def get_month():
    """
    Asks user to specify the month to analyze.

    Returns:
        (int) month - the month to filter by, 1 for january, 2 for february, ... , 6 for june
    """    
    while True:
        try:
            month = int(input('Which month - January, February, March, April, May, or June?\nPlease enter 1 for January, 2 for February, ... , 6 for June.\n'))
            if month>=1 and month<=6:
                break
            else:
                print('Your input does not seem right. Please try again.')
                continue
        except ValueError:
            print("Sorry, I didn't understand that. Please enter an integer!")
            continue
        else:
            break

    print('\nYour input is {}. We will make sure your data is filtered.\n\n'.format(MONTHS[month]))

    return month

def get_day():
    """
    Asks user to specify the day of week to analyze.

    Returns:
        (int) day - the day of week to filter by, 0 for monday, 1 for tuesday, ... , 6 for sunday
    """     
    while True:
        try:
            day = int(input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \nPlease enter 0 for Monday, 1 for Tuesday, ... , 6 for Sunday)\n"))
            if day>=0 and day<=6:
                break
            else:
                print("Your input does not seem right. Please check your typo and try again.")
                continue
        except ValueError:
            print("Sorry, I didn't understand that. Please enter an Integer!")
            continue
        else:
            break 
    print('\nYour input is {}. We will make sure your data is filtered.\n\n'.format(DAYS[day]))
    return day

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - the month to filter by, 1 for january, 2 for february, ... , 6 for june, or 9 to apply no month filter
        (int) day - the day of week to filter by, 0 for monday, 1 for tuesday, ... , 6 for sunday, or 9 to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). 
    city = get_city_name()

    # check if user want to filter on month and day
    limit_on_month, limit_on_day = get_filter_on_month_or_day()

    # get user input for month (all, january, february, ... , june)
    if limit_on_month:
        month = get_month()
    else:
        month = 9 # 9 means no filter will be apply

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if limit_on_day:
       day = get_day()
    else:
        day = 9 # 9 means no filter will be apply
  
    print('-'*40 +'\n\n')
    print('Your filter is: city={}  month={}  day_of_week={}. The analysis will be based on the filtered data.\n'.format(city.title(), MONTHS[month],DAYS[day]))

    return city, month, day

def display_raw_data(df):
    """
    After user if they want to view the war data. 
    - If yes, then 5 rows of data will be displayed.
    - If no, it will stop.
    """
    i=0
    while True:
        try:
            display = str(input('Would you like to view individual trip data? Please enter yes or no. 5 rows of data will be diaplayed.\n'))
            if display.lower()=='yes':
                for j in range(i,i+5):
                    print('index={}:\n {}\n'.format(j,df.iloc[j]))
                i += 5
                continue
            elif display.lower() == 'no':
                break
            else:
                print("Sorry, I didn't understand that. Please enter yes or no!")
                continue
        except ValueError:
            print("Sorry, I didn't understand that. Please re-enter!")
            continue
        else:
            break

def check_continue():
    """
    After each step, we want to take a break so user can read the output on the screen. Then we can continue to analyze other statistics.
    """
    while True:
        next = input('\nPress enter to continue analyzing data...\n')
        if next or next == "":
            break

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - the month to filter by, 1 for january, 2 for february, ... , 6 for june
        (int) day - the day of week to filter by, 0 for monday, 1 for tuesday, ... , 6 for sunday
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("Just one moment... Loading the data.\n")
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    print("Data loaded. Now applying filters... This will be done super fast.\n")
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 9:
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 9:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    print("Data loaded and filters applied.\n")
    print('-'*40+'\n\n')
    check_continue()

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('What is the most popular month for traveling?')
    most_common_month = df['month'].mode()[0]
    popular_month_count = df['month'][df['month']==most_common_month].count()
    print('\n{}\t{}\n'.format(MONTHS[most_common_month],popular_month_count))


    # display the most common day of week
    print('What is the most popular day of week for traveling?')
    day_of_week = df['day_of_week'].mode()[0]
    popular_day_count = df['day_of_week'][df['day_of_week']==day_of_week].count()
    print('\n{}\t{}\n'.format(DAYS[day_of_week],popular_day_count))

    # display the most common start hour
    print('What is the most popular hour of the day to start your travels?')
    start_hour = df['start_hour'].mode()[0]
    popular_hour_count = df['start_hour'][df['start_hour']==start_hour].count()
    print('\n{}\t{}\n'.format(start_hour,popular_hour_count))


    print("\nThis took %s seconds.\n" % (time.time() - start_time))

    check_continue()


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('What is the most popular start station?\n{}\n'.format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('What is the most popular end station?\n{}\n'.format(end_station))

    # display most frequent combination of start station and end station trip
    print('What is the most popular trip from start to end?')
    df['trip'] = df['Start Station'] + '\t' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    # print(trip)
    popular_trip_count = df['trip'][df['trip']==popular_trip].count()
    # print(count)
    print('Start Station\tEnd Station\tCount')
    print('{}\t{}\n'.format(popular_trip,popular_trip_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    check_continue()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    count_days = total_travel_time//86400
    count_hours = (total_travel_time%86400)//3600
    count_minutes = (total_travel_time%3600)//60
    count_seconds = total_travel_time % 60
    print('The total travel time is {} days {} hours {} minutes {} seconds.\n'.format(count_days,count_hours,count_minutes,count_seconds))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    count_minutes = (mean_travel_time)//60
    count_seconds = mean_travel_time % 60
    print('The mean travel time is {} minutes {} seconds.\n'.format(count_minutes,count_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    check_continue()


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('What is the breakdown of users?\n{}\n'.format(count_user_type))


    # Analyzing on Gender
    print('What is the breakdown of user gender?')
    if 'Gender' in df.columns:
        # Display counts of gender
        count_gender = df['Gender'].value_counts()
        print('{}\n'.format(count_gender))
    else:
        print("No gender data to share.\nNone\n")

    # analyzing birth year data
    print('What is the oldest, youngest, and most popular birth year respectively?')
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        latest_year_of_birth = df['Birth Year'].max()
        common_year_of_birth = df['Birth Year'].mode()[0]
        print('The oldest year of birth is {}.\nThe youngest year of birth is {}.\nThe most popular year of birth is {}.\n'\
            .format(int(earliest_year_of_birth),int(latest_year_of_birth),int(common_year_of_birth)))
    else:
        print("No birth year data to share.\nNone\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    check_continue()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # check if user want to display raw data
        display_raw_data(df)

        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
