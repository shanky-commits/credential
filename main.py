import requests
from datetime import datetime

USERNAME = "s-mishraaa"
TOKEN = "shashankmishraa"
GRAPH_ID = "test-shashankkk"

pixela_endpoint = "https://pixe.la/v1/users"

# User creation parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Step 1: Create user
response = requests.post(url=pixela_endpoint, json=user_params)
if response.status_code == 200:
    print("User created successfully.")
else:
    print("Error creating user:", response.status_code, response.text)

# Graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Step 2: Create graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
if response.status_code == 200:
    print("Graph created successfully.")
else:
    print("Error creating graph:", response.status_code, response.text)

# Step 3: Add pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
quantity = input("How many kilometers did you cycle today? ")

# Input validation
try:
    quantity = float(quantity)  # Ensure it's a number
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": str(quantity)  # Convert back to string for JSON
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    if response.status_code == 200:
        print("Pixel added successfully.")
    else:
        print("Error adding pixel:", response.status_code, response.text)
except ValueError:
    print("Invalid input! Please enter a number for kilometers.")

# Optional: Update pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}

# Uncomment to update the pixel
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# if response.status_code == 200:
#     print("Pixel updated successfully.")
# else:
#     print("Error updating pixel:", response.status_code, response.text)

# Optional: Delete pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Uncomment to delete the pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# if response.status_code == 200:
#     print("Pixel deleted successfully.")
# else:
#     print("Error deleting pixel:", response.status_code, response.text)
