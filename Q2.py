class ClockTime:
    def __init__(self):  # initialising the clock time with hours, minutes and seconds set to None
        self.hours = None
        self.minutes = None
        self.seconds = None

    def setHours(self):
        self.hours = int(input('Set Clock hour(s): '))  # getting user input for hours
        while self.hours > 23:  # if hours is more than 23, print error message and prompt for hour
            print('Hour(s) cannot be more than 23!')
            self.hours = int(input('Set Clock hour(s): '))
        return

    def setMinutes(self):
        self.minutes = int(input('Set Clock minute(s): '))  # getting user input for minutes
        while self.minutes > 59:  # if hours more than 59, print error message and prompt for minute
            print('Minute(s) cannot be more than 59!')
            self.minutes = int(input('Set Clock minute(s): '))
        return

    def setSeconds(self):
        self.seconds = int(input('Set Clock second(s): '))  # getting user input for seconds
        while self.seconds > 59:  # if hours more than 59, print error message and prompt for second
            print('Second(s) cannot be more than 59!')
            self.seconds = int(input('Set Clock second(s): '))
        return

    def setTime(self):  # setTime method that calls setHours, setMinutes and setSeconds methods
        print('Please set clock values in 24-Hour format.')
        self.setHours()
        self.setMinutes()
        self.setSeconds()
        return

    def showTime(self):  # showTime method that prints time that was set
        print('Clock time set is: ' + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
        return


print('Creating new ClockTime object...')
Clock = ClockTime()  # Creating new ClockTime object called Clock
Clock.setTime()  # Setting time
Clock.showTime()  # Showing time
