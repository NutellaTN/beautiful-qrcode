import segno

qrcode = segno.make("https://www.wikipedia.org/",error="h")
qrcode.to_artistic(background= "wiki_logo.png",target="qrcodewithlogo.png", scale=5)
