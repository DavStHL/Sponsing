import streamlit as st
import os
from datetime import datetime

# Ordner vorbereiten
os.makedirs("uploads", exist_ok=True)
os.makedirs("daten", exist_ok=True)

st.title("🤝 Sponsoring-Anfrage – Handballverein")

st.markdown("Bitte füllen Sie das Formular aus und laden Sie Ihr Logo hoch.")

firma = st.text_input("Firmenname")
ansprechpartner = st.text_input("Ansprechpartner")
email = st.text_input("E-Mail-Adresse")

paket = st.selectbox("Sponsoring-Paket wählen", [
    "Paket A – Logo auf Ärmel (200€)",
    "Paket B – Brust klein (400€)",
    "Paket C – Groß + Social Media (600€)",
    "Paket D – Premium (800€)"
])

anzahl_trikots = st.number_input("Anzahl Trikots", min_value=14, max_value=100, step=1)
hinweise = st.text_area("Weitere Hinweise (optional)")

logo = st.file_uploader("Logo hochladen (PNG, JPG)", type=["png", "jpg", "jpeg"])

if st.button("Absenden"):
    if not (firma and email):
        st.warning("Bitte mindestens Firmenname und E-Mail angeben.")
    else:
        # Speichern
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        dateiname = f"{firma}_{timestamp}".replace(" ", "_")

        with open(f"daten/{dateiname}.txt", "w", encoding="utf-8") as f:
            f.write(f"Firma: {firma}\n")
            f.write(f"Ansprechpartner: {ansprechpartner}\n")
            f.write(f"E-Mail: {email}\n")
            f.write(f"Paket: {paket}\n")
            f.write(f"Trikots: {anzahl_trikots}\n")
            f.write(f"Hinweise: {hinweise}\n")

        if logo:
            with open(f"uploads/{dateiname}.png", "wb") as f:
                f.write(logo.read())

        st.success("✅ Sponsoring-Anfrage übermittelt!")
