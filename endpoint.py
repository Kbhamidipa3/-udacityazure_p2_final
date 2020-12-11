import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://4bbc39d7-1e33-4747-b261-0abecc0bacfc.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "BT87Fzc7mQtnRdyxqRULv6MMkfnIa4Pp"

# Two sets of data to score, so we get two results back
data = {
    "data": [
    {
      "age": 57,
      "job": "technician",
      "marital": "married",
      "education": "high.school",
      "default": "no",
      "housing": "no",
      "loan": "yes",
      "contact": "cellular",
      "month": "jun",
      "day_of_week": "fri",
      "duration": 52,
      "campaign": 4,
      "pdays": 999,
      "previous": 0,
      "poutcome": "nonexistent",
      "emp.var.rate": -1.8,
      "cons.price.idx": 93.444,
      "cons.conf.idx": -41.8,
      "euribor3m": 1.327,
      "nr.employed": 5228.1
    }
  ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
