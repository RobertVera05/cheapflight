#imports for python script
import http.client
import datetime
import sys

#function for checking if the initial date entered is invalid
def isValidIinitialDate(initialDate):
    userDate = datetime.date.isoformat(initialDate)
    print('userDate is ', userDate)
    currentDate = datetime.date.today()
    print("Current date is :", currentDate)
    if initialDate < currentDate:
        return False
    else:
        return True

#function for checking if url exists
def doesUrlExist(url):
    connection = httplib.HTTPConnection(url)
    connection.request("HEAD", '')
    if connection.getresponse().status == 200:
        print("Website exists")
    else:
        print("Website does not exist")

#main function
def main():
    location = input('Enter your destination: ')
    initialDate = input('Enter the initial date:(ex. 2018-09-18)')
    returnDate = input('Enter the date you plan on returning:(ex. 2018-09-22)')
    
    #check if the initial date is valid
    isValidDate = isValidIinitialDate(initialDate)
    #if the function returns false then exit out
    if isValidDate == False:
        print('Initial date cannot be before todays date')
        sys.exit()
    
    endDate = input('Enter the end date:')
    print('Checking for cheapest flights between dates ', initialDate,' and ', endDate, ' to destination ', location)
    url = "https://www.google.com/flights#flt=/m/0f2rq..2018-10-02*./m/0f2rq.2018-10-06;c:USD;e:1;ls:1w;sd:0;t:h"
    doesUrlExist(url)

if __name__ == "__main__":
    main()