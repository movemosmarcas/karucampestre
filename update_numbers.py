import os

files = [
    r"C:\Users\user\Desktop\Karu\landing_preview\index.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\gracias.html"
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the numeric only version for hrefs
    content = content.replace("573332392469", "573128136677")
    
    # Replace the formatted version for display text
    content = content.replace("+57 333 239 2469", "+57 312 813 6677")
    content = content.replace("+57 333 2392469", "+57 312 813 6677") # just in case
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement done.")
