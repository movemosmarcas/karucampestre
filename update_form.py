import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will just write a regex or string replace to add name attributes to the inputs.

# 1. Add names to inputs
content = content.replace('placeholder="Ej. Juan Pérez" required>', 'placeholder="Ej. Juan Pérez" name="nombre" required>')
content = content.replace('placeholder="juan@correo.com" required>', 'placeholder="juan@correo.com" name="correo" required>')
content = content.replace('placeholder="+57 300 000 0000" required>', 'placeholder="+57 300 000 0000" name="telefono" required>')
content = content.replace('class="w-full border-b border-karu-piedra py-3 focus:outline-none focus:border-karu-verde bg-transparent text-karu-verde" required>', 'class="w-full border-b border-karu-piedra py-3 focus:outline-none focus:border-karu-verde bg-transparent text-karu-verde" name="inversion" required>')

# Add JS handler before body ends
js_script = """
    <!-- Google Sheets Form Submission -->
    <script>
        const scriptURL = 'AQUI_PONDREMOS_LA_URL_DEL_SCRIPT';
        const forms = document.querySelectorAll('form');

        forms.forEach(form => {
            form.addEventListener('submit', e => {
                e.preventDefault();
                
                // Change button text to indicate loading
                const btn = form.querySelector('button[type="submit"]');
                const originalText = btn.innerHTML;
                btn.innerHTML = 'Enviando...';
                btn.disabled = true;

                fetch(scriptURL, { method: 'POST', body: new FormData(form)})
                    .then(response => {
                        window.location.href = form.getAttribute('action');
                    })
                    .catch(error => {
                        console.error('Error!', error.message);
                        alert('Hubo un error enviando el formulario. Por favor intenta de nuevo.');
                        btn.innerHTML = originalText;
                        btn.disabled = false;
                    });
            });
        });
    </script>
</body>"""

content = content.replace("</body>", js_script)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated HTML with names and JS")
