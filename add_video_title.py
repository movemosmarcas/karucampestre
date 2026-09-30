import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """    <!-- 2.5 Video Destacado -->
    <section class="w-full bg-karu-verde">
        <div class="max-w-7xl mx-auto py-12 px-6">
            <div class="relative w-full h-auto shadow-2xl rounded-sm group">"""

replacement = """    <!-- 2.5 Video Destacado -->
    <section class="w-full bg-karu-verde">
        <div class="max-w-7xl mx-auto py-16 px-6">
            <h2 class="text-3xl md:text-5xl font-serif text-white mb-12 text-center">Así se ven nuestros lotes campestres</h2>
            <div class="relative w-full h-auto shadow-2xl rounded-sm group">"""

if target in content:
    content = content.replace(target, replacement)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Title added.")
else:
    print("Target not found.")
