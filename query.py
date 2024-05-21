import requests
import json

apiKey = open("box/basic_key.txt", "r").read()
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey, "API-Version" : "2023-04"}

query1 = open("gql/ducks_status.graphql", "r").read()


data = {'query' : query1}

r = requests.post(url=apiUrl, json=data, headers=headers)

output_info = json.dumps(r.json(), indent=2)
output_file = open("output.json", "w")
output_file.write(output_info)

