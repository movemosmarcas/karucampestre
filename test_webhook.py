import requests

url = "https://script.google.com/macros/s/AKfycbzhdETiYhYUoqlbYVr61SuJCWxQ3wUkf3Tiu66pNgLhDLxsw8sbss-cY_zGUaS-NsRI/exec"
data = {
    "nombre": "Test Agent",
    "correo": "test@agent.com",
    "telefono": "1234567",
    "inversion": "Máximo 600 millones"
}

response = requests.post(url, data=data)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
