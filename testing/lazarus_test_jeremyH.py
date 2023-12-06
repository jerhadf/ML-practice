# flake8: noqa
# Lazarus API python interview exercise
# 1) Process the document using the Lazarus Forms API Forms endpoint
# This is a cooperative assessment so you can ask questions for help and such.
# Documentation:
# https://docs.lazarusforms.com/docs/lazarus-forms/q-and-a
# Here's a set of credentials:
# orgId: 3bb03098411b45b5b7
# authKey: 6788fe634672436b8772
# File to use:
# https://firebasestorage.googleapis.com/v0/b/lazarus-apis-testing.appspot.com/o/examples%2FSample%20Form.pdf?alt=media&token=5b537052-ea54-4be4-9d36-9620ee994c1c
# Extract the following details:
# Patient First Name
# Patient Last Name
# Physician Address
# Find the hospitalization status
# Information about other medications tried

import base64
import json

import requests

# File & API endpoint to use:
filepath = "https://firebasestorage.googleapis.com/v0/b/lazarus-apis-testing.appspot.com/o/examples%2FSample%20Form.pdf?alt=media&token=5b537052-ea54-4be4-9d36-9620ee994c1c"
endpoint = "https://api.lazarusforms.com/api/rikai"

# download the file and save it locally
response = requests.get(filepath)
with open("Sample_Form.pdf", "wb") as f:
    f.write(response.content)

# read PDF file, encode in base 64, then decode as UTF-8 string
with open("Sample_Form.pdf", "rb") as f:
    file_content = f.read()
file_decoded = base64.b64encode(file_content).decode("UTF-8")

headers_obj = {
    "orgId": "3bb03098411b45b5b7",
    "authKey": "6788fe634672436b8772",
    "Content-Type": "application/json",
}

questions = [
    "What is the patient's first name?",
    "What is the patient's last name?",
    "What is the physician's full address? Include the address, city, state, and zip code.",
    "What is the patient's hospitalization status? Answer as one of Hospitalized, Not Hospitalized, or N/A if no info present.",
    "What are all the other medication names the patient tried? Return as a full list of the name, strength, directions, date of therapy, and reasons for failure for each medication.",
]

data = {"base64": file_decoded, "question": questions}

# send the API request to upload this file and get the answers
doc = requests.request(
    "POST",
    url=endpoint,
    headers=headers_obj,
    data=json.dumps(data),
)

print(doc.json())

with open("results.json", mode="w") as f:
    json.dump(doc.json(), f)

from pydantic import BaseModel

class Medication(BaseModel):
    name: str,
    strength: str,

class PatientInfo(BaseModel):
    # ... items
    other_medications: List[Medication]

