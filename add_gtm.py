import os

files = [
    r"C:\Users\user\Desktop\Karu\landing_preview\index.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\gracias.html",
    r"C:\Users\user\Desktop\Karu\landing_preview\politica-de-privacidad.html"
]

head_code = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TPJH5SQR');</script>
<!-- End Google Tag Manager -->
</head>"""

body_code = """<body class="font-sans text-gray-800 bg-karu-claro antialiased">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TPJH5SQR"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added to avoid duplicates
    if "GTM-TPJH5SQR" not in content:
        content = content.replace("</head>", head_code)
        content = content.replace('<body class="font-sans text-gray-800 bg-karu-claro antialiased">', body_code)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("GTM injected.")
