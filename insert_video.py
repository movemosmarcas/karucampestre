import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """    </section>

    <!-- 5. Ubicación Estratégica -->"""

replacement = """    </section>

    <!-- 2.5 Video Destacado -->
    <section class="w-full bg-karu-verde">
        <div class="max-w-7xl mx-auto py-12 px-6">
            <video class="w-full h-auto shadow-2xl rounded-sm" controls playsinline>
                <source src="video_landing.mp4" type="video/mp4">
                Tu navegador no soporta el formato de video.
            </video>
        </div>
    </section>

    <!-- 5. Ubicación Estratégica -->"""

if "<!-- 5. Ubicación Estratégica -->" in content:
    content = content.replace(target, replacement)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Video inserted.")
else:
    print("Target not found. Current text:")
    # Print a snippet around Ubicacion
    import re
    match = re.search(r'.{0,50}Ubicaci.{0,50}', content)
    if match:
        print(match.group(0))
