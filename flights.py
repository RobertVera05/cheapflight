#imports for python script
import http.client

#function for checking if url exists
def doesUrlExist(url):
    connection = httplib.HTTPConnection(url)
    connection.request("HEAD", '')
    if connection.getresponse().status == 200:
        print("Website exists")
    else:
        print("Website does not exist")

#main function for flights python script
def __main__():
    url = "https://www.google.com/flights#flt=/m/0f2rq..2018-10-02*./m/0f2rq.2018-10-06;c:USD;e:1;ls:1w;sd:0;t:h"
    doesUrlExist(url)

