import os

# Update index.html
filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <div class="md:text-left text-sm uppercase tracking-wider opacity-80 order-2 md:order-1">
                <p>Un proyecto de TIMONTTI © 2026</p>
            </div>"""

replacement = """            <div class="md:text-left text-sm uppercase tracking-wider opacity-80 order-2 md:order-1 flex flex-col items-center md:items-start">
                <p class="mb-3">Un proyecto de:</p>
                <img src="Timontti-Logo-blanco-300x139.png" alt="Timontti" class="h-10 object-contain mb-3">
                <p class="text-xs">&copy; 2026</p>
            </div>"""

content = content.replace(target, replacement)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)


# Update gracias.html
filepath = r"C:\Users\user\Desktop\Karu\landing_preview\gracias.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target2 = """            <div>
                <p class="uppercase tracking-wider">Un proyecto de TIMONTTI © 2026</p>
            </div>"""

replacement2 = """            <div class="flex flex-col items-center md:items-start">
                <p class="uppercase tracking-wider mb-2">Un proyecto de:</p>
                <img src="Timontti-Logo-blanco-300x139.png" alt="Timontti" class="h-10 object-contain mb-2">
                <p class="text-xs">&copy; 2026</p>
            </div>"""

content = content.replace(target2, replacement2)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Footers updated with Timontti logo.")
