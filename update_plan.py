import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """                    <div class="flex items-start">
                        <div class="text-4xl font-serif text-karu-arena w-28">40%</div>
                        <div>
                            <h4 class="font-bold uppercase tracking-wider text-karu-verde mb-1">Construcción</h4>
                            <p class="text-sm text-gray-600">Distribuido en 18 cuotas mensuales una vez se decreta el punto de equilibrio.</p>
                        </div>
                    </div>"""

replacement = """                    <div class="flex items-start">
                        <div class="text-4xl font-serif text-karu-arena w-28">10%</div>
                        <div>
                            <h4 class="font-bold uppercase tracking-wider text-karu-verde mb-1">Preventa</h4>
                            <p class="text-sm text-gray-600">Distribuido en 12 cuotas hasta cumplimiento de punto de equilibrio.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="text-4xl font-serif text-karu-arena w-28">30%</div>
                        <div>
                            <h4 class="font-bold uppercase tracking-wider text-karu-verde mb-1">Construcción</h4>
                            <p class="text-sm text-gray-600">Dividido en 12 cuotas mensuales una vez es decretado el punto de equilibrio.</p>
                        </div>
                    </div>"""

content = content.replace(target, replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Plan Comercial")
