with open(r'C:\Users\edgvi\Documents\ventanasbanuls\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    'https://maps.app.goo.gl/9Ww7zbGbAvi6bTe36',
    'https://www.google.com/maps/place/Ventanas+Ba%C3%B1uls,+Carrer+Murillo,+41,+03802+Alcoi,+Alicante/data=!4m2!3m1!1s0xd61865575a2caa7:0xe262f3333a9606ab'
)

with open(r'C:\Users\edgvi\Documents\ventanasbanuls\index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated Ventanas Bañuls Google link to official Google Maps URL')
