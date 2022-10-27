import requests
import datetime as dt

TOKEN = "3124343523413020232312efgddrgd"
USERNAME = "saeed"
graph_id = "graph24"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
## Create a user
# pixela_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
#
# }
# response = requests.post(PIXELA_ENDPOINT, json=pixela_parameters)
# print(response.json())
# TODO: NOTE -> params = for query in url, json = to send in body, headers = to send in request headers


# Create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_json = {
    "id": graph_id,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
# secure way to send token is headers
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_json, headers=headers)
if response.status_code == 200:
    print(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}.html")

# Post value to the graph
post_value_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"

selected_date = dt.datetime.now()

headers = {
    "X-USER-TOKEN": TOKEN
}
kilometer = input("How many kilometers did you cycle today? ")
json = {
    "date": selected_date.strftime("%Y%m%d"),
    "quantity": kilometer,
}
response = requests.post(url=post_value_endpoint, json=json, headers=headers)
print(response.text)
# Update value to the graph

selected_date = dt.datetime.now()
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{selected_date.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN,
}
update_json = {
    "quantity": "123.321",
}
response = requests.put(url=update_endpoint, headers=headers, json=update_json)
print(response.text)

selected_date = dt.datetime.now()
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{selected_date.strftime('%Y%m%d')}"
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.delete(delete_endpoint, headers=headers)
print(response.text)
