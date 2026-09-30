import os

filepath = r"C:\Users\user\Desktop\Karu\landing_preview\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """    <!-- 2.5 Video Destacado -->
    <section class="w-full bg-karu-verde">
        <div class="max-w-7xl mx-auto py-12 px-6">
            <video class="w-full h-auto shadow-2xl rounded-sm" controls playsinline>
                <source src="video_landing.mp4" type="video/mp4">
                Tu navegador no soporta el formato de video.
            </video>
        </div>
    </section>"""

replacement = """    <!-- 2.5 Video Destacado -->
    <section class="w-full bg-karu-verde">
        <div class="max-w-7xl mx-auto py-12 px-6">
            <div class="relative w-full h-auto shadow-2xl rounded-sm group">
                <video id="promoVideo" class="w-full h-auto rounded-sm" controls playsinline>
                    <source src="video_landing.mp4" type="video/mp4">
                    Tu navegador no soporta el formato de video.
                </video>
                
                <!-- Play Button Overlay -->
                <div id="playOverlay" class="absolute inset-0 flex items-center justify-center bg-black/20 cursor-pointer transition-opacity duration-300">
                    <div class="w-20 h-20 md:w-24 md:h-24 bg-karu-arena/90 rounded-full flex items-center justify-center shadow-lg group-hover:scale-110 group-hover:bg-karu-arena transition-all duration-300">
                        <svg class="w-10 h-10 md:w-12 md:h-12 text-white ml-2" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M4 4l12 6-12 6z"></path>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const playOverlay = document.getElementById('playOverlay');
            const promoVideo = document.getElementById('promoVideo');

            if(playOverlay && promoVideo) {
                playOverlay.addEventListener('click', () => {
                    promoVideo.play();
                });

                promoVideo.addEventListener('play', () => {
                    playOverlay.classList.add('opacity-0', 'pointer-events-none');
                });

                promoVideo.addEventListener('pause', () => {
                    playOverlay.classList.remove('opacity-0', 'pointer-events-none');
                });
            }
        });
    </script>"""

if "<!-- 2.5 Video Destacado -->" in content:
    content = content.replace(target, replacement)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Play overlay added.")
else:
    print("Target not found.")
