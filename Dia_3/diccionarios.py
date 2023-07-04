datos = {
    'nombre': "Alexis",
    'apellidos': "TH",
    'gender': "male",
    'height': 1.75,
    'fav_sports': [
        "Soccer",
        "Football",
        "Volleyball"
    ],
    "login_data": {
        "email": "alexis@gmail.com",
        'username': 'alexdev2808',
    }
}

apellidos = datos['apellidos']
fav_sport = datos['fav_sports'][0]
username = datos['login_data']['username']

print(f"{apellidos}: Favorite sport => {fav_sport.upper()} and username => {username}")

print(datos.keys())
print(datos.values())
print(datos.items())
