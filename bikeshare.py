import pandas as pd
import time

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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input('\nWhich city should we explore? \n New York City \n Chicago \n Washington \n Pick one:').lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print('\n Uh oh, looks like we hit a snag, let\'s try that again')
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nLet\'s pick a month first: \n January \n February \n March \n April \n May \n June \n or type 'all' \n Pick one:").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print('Uh oh, let\'s try that again')
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nNext up, pick a day: \n Sunday \n Monday \n Tuesday \n Wednesday \n Thursday \n Friday \n Saturday \n or type 'all' \n Pick one:").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print('Uh oh, let\'s try that again')
        continue
      else:
        break

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
    #loading data with pandas
    df = pd.read_csv(CITY_DATA[city])
    
    #converting to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    #pulling out month and weekday for display
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filtering month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filtering week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        most_common_month = df['month'].mode()[0]
        print('The most common month is', most_common_month, '(i.e. 1 = January)')

    # TO DO: display the most common day of week
    if day == 'all':    
        most_common_day = df['day_of_week'].mode()[0]
        print('The most common day of the week is', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour on a 24 hour clock is', most_common_hour, '(i.e 14 = 2:00pm)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df.groupby(['Start Station', 'End Station']).count()
    print('The most common combination of start and end stations is', start_station,'&',end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('The total travel time in days is', int(total_travel_time/86400))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The average travel time minutes is', int(avg_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nUser types are:\n', user_type)
    
    # TO DO: Display counts of gender
    try:
      gender = df['Gender'].value_counts()
      print('\nGender breakdown:\n', gender)
    except KeyError:
      print('\nGender breakdown: \nNo informtation available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_birth_year = df['Birth Year'].min()
      print('\nThe earliest rider birth year is', int(earliest_birth_year))
    except KeyError:
      print('\nThere was no data available for earliest birth year.')

    try:
      most_recent_birth_year = df['Birth Year'].max()
      print('\nThe most recent rider bith year is', int(most_recent_birth_year))
    except KeyError:
      print('\nThere was no data available for most recent birth year.')

    try:
      most_common_birth_year = df['Birth Year'].value_counts().idxmax()
      print('\nThe most common rider birth year is', int(most_common_birth_year))
    except KeyError:
      print('\nThere was no data available for most common birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def review_data(df):
    '''View data used to populate stats'''
    
    row_index = 0
    view_data = input('\nWould You like to view the data used? Enter yes or no.\n').lower()
    while True:
        if view_data == 'no':
            return
        if view_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        view_data = input('\n Would you like to see five more rows? Enter yes or no \n').lower()

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        review_data(df)

        restart = input('\nWant to go for another ride? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()