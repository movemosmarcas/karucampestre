import requests

url = "https://script.google.com/macros/s/AKfycbxNQFaSZc60fAsYi2MzozRaMQpYEjfPz-52R3T-x5y96-TLTjdephbYRiq68PimvqRH8Q/exec"
data = {
    "nombre": "Test Agent",
    "correo": "test@agent.com",
    "telefono": "1234567",
    "inversion": "Máximo 600 millones"
}

response = requests.post(url, data=data)
print("Status Code:", response.status_code)
print("Response Text:", response.text)

