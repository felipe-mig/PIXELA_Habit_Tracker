import requests
from datetime import datetime

USERNAME = "felipe-mig"
TOKEN = "om)o0(X3(8s5ShF)K7i7UIM0d*3&qV*J)"
GRAPH_ID = "graph2"





# CREATING AN ACCOUNT ON PIXELA:

# endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# this will create an account on pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# To run it uncomment this part:

# response = requests.post(url=pixela_endpoint, json=user_params)
# # Print the response in .txt to check if it was succesfull
# print(response.text)








# To check if it is working, on the browser URL bar type: https://pixe.la/v1/users/felipe-mig/graphs/graph2.html and refresh after each request

# CREATING A GRAPH ON YOUR ACCOUNT:

#  https://pixe.la/v1/users/a-know/graphs 
graph_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


# This are the parameters we want to track
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int", # <-- data type (Only int or float are supported.)
    "color": "ajisai" # <-- colours are in japanise: shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) 
}

# encrypting the token and using it as header
headers = {
    "X-USER-TOKEN": TOKEN
}

# https://pixe.la/v1/users/a-know/graphs + graph_config + headers <-- this will be inserted on the browsers URL bar

# To run it uncomment this part:

# response = requests.post(url=graph_enpoint, json=graph_config, headers=headers)
# print(response.text)

# After the request is sent, to check the graph in the browser type this URL with the username and the id as parameters: https://pixe.la/v1/users/felipe-mig/graphs/graph2.html








# ADDING PIXELS TO THE GRAPH:

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# automatization
today = datetime.now()
# print(today.strftime("%y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"), # <-- %y %m %d is for formating the date in the way that the API documentation is requiring (yyyyMMdd format). source: https://www.w3schools.com/python/python_datetime.asp
    
    # change this number based on the performance of your day 
    "quantity": input("How many hours did you spend coding today?\n"), # <-- Specify the quantity to be registered on the specified date. Rules: int ^\-?[0-9]+, float ^\-?[0-9]+\.[0-9]+
}

#  https://pixe.la/v1/users/felipe-mig/graphs/graph2/date:20250219/quantity:3/om)o0(X3(8s5ShF)K7i7UIM0d*3&qV*J) 

# To run it uncomment this part:

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)








# UPDATE

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "10",
}

# To run it uncomment this part:

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)







# DELETE

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# To run it uncomment this part:

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)