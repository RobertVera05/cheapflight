#imports for python script
import http.client
import datetime

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
    initialDate = input('Enter the initial date:')
    currentDate = datetime.date.today()
    print("Current date is :", currentDate)
    if initialDate < currentDate:
        print('Initial date cannot be before todays date')
    endDate = input('Enter the end date:')
    print('Checking for cheapest flights between dates ', initialDate,' and ', endDate, ' to destination ', location)
    url = "https://www.google.com/flights#flt=/m/0f2rq..2018-10-02*./m/0f2rq.2018-10-06;c:USD;e:1;ls:1w;sd:0;t:h"
    doesUrlExist(url)

if __name__ == "__main__":
    main()

