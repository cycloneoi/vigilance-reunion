import requests
from pdf2image import convert_from_path
import os

# Télécharger le PDF de vigilance
pdf_url = "https://rpcache-aa.meteofrance.com/internet2018client/2.0/report?domain=VIGI974&report_type=vigilance&report_subtype=version%20PDF&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImV4cCI6MTc0NDcwNDQ1M30.eyJqdGkiOiJ6dDZCckVacUUiLCJpYXQiOjE3NDQ3MDQ0NTN9.rsfBwMwQJhcBhGHlskT2c50rtp1syCTpeiPvUWQXrT0"
pdf_path = "public/vigilance.pdf"
image_path = "public/vigilance.jpg"  # 👈 changé en .jpg

# Téléchargement du PDF
response = requests.get(pdf_url)
with open(pdf_path, "wb") as f:
    f.write(response.content)

# Convertir la première page du PDF en image JPEG
pages = convert_from_path(pdf_path, first_page=1, last_page=1)
pages[0].save(image_path, 'JPEG')  # 👈 export JPEG

# Supprimer le PDF
os.remove(pdf_path)
