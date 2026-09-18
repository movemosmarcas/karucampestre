import os

files = [
    r"C:\Users\user\Desktop\Karu\landing_preview\index.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\gracias.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\politica-de-privacidad.html"
]

favicon_tag = '\n    <link rel="icon" type="image/png" href="favicon.png">\n</head>'

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace("</head>", favicon_tag)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Favicon added.")
