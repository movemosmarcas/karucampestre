import requests

url = "https://script.google.com/macros/s/AKfycbwTWSjuEN7GL1yQ4pCsK43C3r3TNdOxLRy2Wnziiggq6wTIlqdOCIPwHAb0WTlMbx_3/exec"
data = {
    "nombre": "Test Agent",
    "correo": "test@agent.com",
    "telefono": "1234567",
    "inversion": "Máximo 600 millones"
}

response = requests.post(url, data=data)
print("Status Code:", response.status_code)
print("Response Text:", response.text)

