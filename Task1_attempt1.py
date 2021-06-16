import requests
userid = "6wl"     # Imput the user ID to be checked
response = requests.get("https://api.github.com/users/"+userid)       # request to get data from AIP label data "response"
assert response.status_code == 200                                    # assert check to make sure response code is 200 OK

response_body = response.json()

print("Name:", response_body["name"])
print("ID:", response_body["id"])
print("Company:", response_body["company"])
print("Public Repos:", response_body["public_repos"])
print("Public Gists:", response_body["public_gists"])
print("Followers:", response_body["followers"])
print("Following:", response_body["following"])


#print(response_body)

