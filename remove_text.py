import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the text
target = ", frente a un samán centenario que ha presenciado generaciones."
# Try standard replace
new_content = content.replace(target, ".")

# Wait, if they used a regular space or maybe no period at the end of the previous sentence?
# "construir, frente a un samán centenario que ha presenciado generaciones."
# Let's replace ", frente a un samán centenario que ha presenciado generaciones." with "."
# If it fails, let's try replacing "construir, frente a un samán centenario que ha presenciado generaciones." with "construir."

if target in content:
    content = content.replace(target, ".")
else:
    # Just to be safe with encoding or formatting
    target2 = "construir, frente a un samán centenario que ha presenciado generaciones"
    content = content.replace(target2, "construir")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Text removed.")
