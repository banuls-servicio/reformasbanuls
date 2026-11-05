with open(r'c:\Users\edgvi\Documents\webleadsagent\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('https://maps.app.goo.gl/9Ww7zbGbAvi6bTe36', 'https://share.google/EFxHTu7dtLrR4XIMK')

with open(r'c:\Users\edgvi\Documents\webleadsagent\index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated Reformas Bañuls Google link to https://share.google/EFxHTu7dtLrR4XIMK')
