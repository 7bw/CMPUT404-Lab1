import requests

# print the version of the requests library
print(requests.__version__)

# get Google homepage
print(requests.get("http://google.com"))

response = requests.get("https://raw.githubusercontent.com/7bw/CMPUT404-Lab1/master/lab1.py")
print(response.text)
