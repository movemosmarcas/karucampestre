import os

files = [
    r"C:\Users\user\Desktop\Karu\landing_preview\index.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\gracias.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\politica-de-privacidad.html"
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the email
        new_content = content.replace("gestion.activos@timontti.com", "comercial@timontti.com")
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
