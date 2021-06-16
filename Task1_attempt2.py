import requests
userid = "6wl"     # Imput the user ID to be checked
response = requests.get("https://api.github.com/users/"+userid)       # request to get data from AIP label data "response"

Name = "Gregory Loscombe"         # defining values to match name given in task
ID = "51361635"
Company = "Amplience"
Location = "Manchester"
Public_Repos = 3
public_gists = 2
Followers = 0
Following = 3

assert response.status_code == 200          # assert check to make sure response code is 200 OK. Code stops if comand is not ok
response_body = response.json()

if response_body["name"] != Name:                                           #checking if there is a difference in initial name and response from AIP
    print("name incorrect, name supplied:", response_body["name"])          #if Values don't match valuue ftrom the AIP is printed
else:
    print("names match")

if response_body["id"] != ID:                                               #checking if there is a difference in initial ID and response from AIP
    print("ID incorrect, ID supplied:", response_body["id"])      #if Values don't match valuue ftrom the AIP is printed
else:
    print("ID match")

if response_body["company"] != Company:                                         #checking if there is a difference in initial company and response from AIP
    print("Company incorrect, Company supplied:", response_body["company"])         #if Values don't match valuue ftrom the AIP is printed
else:
    print("company match")

if response_body["public_repos"] != Public_Repos:                                         #checking if there is a difference in initial public repos and response from AIP
    print("Public Repos incorrect, Public Repos supplied:", response_body["public_repos"])         #if Values don't match valuue ftrom the AIP is printed
else:
    print("Public Repos match")

if response_body["location"] != Location:                                              #checking if there is a difference in initial location and response from AIP
         print("Location incorrect, Location supplied:", response_body["location"])         #if Values don't match valuue ftrom the AIP is printed
else:
    print("location match")

if response_body["public_gists"] != public_gists:                                            #checking if there is a difference in initial public_gists and response from AIP
        print("public_gists incorrect, public_gists supplied:", response_body["public_gists"])         #if Values don't match valuue ftrom the AIP is printed
else:
    print("public_gists")

if response_body["followers"] != Followers:                                         #checking if there is a difference in initial followers and response from AIP
    print("followers incorrect, followers supplied:", response_body["followers"])         #if Values don't match valuue ftrom the AIP is printed
else:
    print("followers match")

if response_body["following"] != Following:                                         #checking if there is a difference in initial following and response from AIP
            print("following incorrect, following supplied:", response_body["following"])         #if Values don't match valuue ftrom the AIP is printed
else:
    print("following")