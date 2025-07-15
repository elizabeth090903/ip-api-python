import request

# Reemplaza con tu token personal y roomId
access_token = 'OWFkODU0NWEtMzFlZi00MjYzLWEyZjEtOTI4NmIxMDFkODA3YzYxNjFiZTctZTg5_P0A1_8a4451f0-7d94-4102-99eb-bda7abb53675'
room_id = '8a4451f0-7d94-4102-99eb-bda7abb53675'
mensaje = 'MICHIS NARANJAS'

url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
data = {
    'roomId': room_id,
    'text': mensaje
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Mensaje enviado con éxito.")
else:
    print(f"Error al enviar mensaje: {response.status_code}\n{response.text}")
