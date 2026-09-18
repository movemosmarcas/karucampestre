import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The inline form block to find
target_inline = """                        <div>
                            <label class="block text-xs uppercase tracking-wider font-bold mb-2">Teléfono</label>
                            <input type="tel" class="w-full border-b border-karu-piedra py-3 focus:outline-none focus:border-karu-verde bg-transparent text-karu-verde" placeholder="+57 300 000 0000" required>
                        </div>"""

replacement_inline = target_inline + """
                        <div>
                            <label class="block text-xs uppercase tracking-wider font-bold mb-2">¿Cuánto deseas invertir en tu lote?</label>
                            <select class="w-full border-b border-karu-piedra py-3 focus:outline-none focus:border-karu-verde bg-transparent text-karu-verde appearance-none" required>
                                <option value="" disabled selected>Selecciona una opción</option>
                                <option value="Máximo 600 millones">Máximo 600 millones</option>
                                <option value="De 600 a 700 millones">De 600 a 700 millones</option>
                                <option value="Más de 700 millones">Más de 700 millones</option>
                            </select>
                        </div>"""

content = content.replace(target_inline, replacement_inline)

# The modal form block to find
target_modal = """                <div>
                    <label class="block text-xs uppercase tracking-wider font-bold mb-2">Teléfono</label>
                    <input type="tel" class="w-full border-b border-karu-piedra py-3 focus:outline-none focus:border-karu-verde bg-transparent text-karu-verde" placeholder="+57 300 000 0000" required>
                </div>"""

replacement_modal = target_modal + """
                <div>
                    <label class="block text-xs uppercase tracking-wider font-bold mb-2">¿Cuánto deseas invertir en tu lote?</label>
                    <select class="w-full border-b border-karu-piedra py-3 focus:outline-none focus:border-karu-verde bg-transparent text-karu-verde appearance-none" required>
                        <option value="" disabled selected>Selecciona una opción</option>
                        <option value="Máximo 600 millones">Máximo 600 millones</option>
                        <option value="De 600 a 700 millones">De 600 a 700 millones</option>
                        <option value="Más de 700 millones">Más de 700 millones</option>
                    </select>
                </div>"""

content = content.replace(target_modal, replacement_modal)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added select dropdowns.")
