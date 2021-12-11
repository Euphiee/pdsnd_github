import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Would you like to see data for chicago, new york city, or washington?\n').lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print('Please enter a valid city.')
        except:
            continue

    # get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            month = input('Which month would you like to filter? all, january, february, march, april, may, or june?\n').lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print('Please enter a valid month.')
        except:
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        try:
            day = input('Which day would you like to filter? all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday?\n').lower()
            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print('Please enter a valid day.')
        except:
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular day of week:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', start_station)


    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', end_station)

    # display most frequent combination of start station and end station trip
    df['combination_station'] = df['Start Station']+','+ ' ' + df['End Station']
    comb = df['combination_station'].mode()[0]
    print('Most frequent combination of start station and end station:', comb)
    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('total travel time:', travel_time)



    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time:', round(mean_time,2))


    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nDisplay the breakdown of users\n')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    # there is no gender data in washington, show no data
    print('\nDisplay counts of gender\n')
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print('No gender data')
    


    # Display earliest, most recent, and most common year of birth
    print('\nDisplay earliest, most recent, and most common year of birth\n')
    try:
        earliest = int(df['Birth Year'].min())
        print('earliest year of birth:', earliest)
        recent = int(df['Birth Year'].max())
        print('most recent year of birth:', recent)
        common = int(df['Birth Year'].mode()[0])
        print('most common year of birth:', common)
    except:
        print('No year of birth data')
    

    print("\nThis took %s seconds." % (round((time.time() - start_time),2)))
    print('-'*40)

def raw_data(df):
    """Displays individual raw data."""
    while True:
            try:
                show = input('\nWould you to view indeividual raw data? Enter yes or no.\n').lower()
                if show in ['yes', 'no']:
                    break
                else:
                    print('Please enter a valid input.')
            except:
                continue
        
    lines_start = 0       
    while show == 'yes':
        print(df.iloc[lines_start])
        lines_start += 1
        while True:
            try:
                show = input('\nWould you to view indeividual raw data? Enter yes or no.\n').lower()
                if show in ['yes', 'no']:
                    break
                else:
                    print('Please enter a valid input.')
            except:
                continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        
        
        while True:
            try:
                restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
                if restart in ['yes', 'no']:
                    break
                else:
                    print('Please enter a valid input.')
            except:
                continue

        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
