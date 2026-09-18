import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all variations
content = content.replace("Agenda una visita", "Agenda tu asesoría")
content = content.replace("AGENDA UNA VISITA", "AGENDA TU ASESORÍA")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement done cleanly.")
