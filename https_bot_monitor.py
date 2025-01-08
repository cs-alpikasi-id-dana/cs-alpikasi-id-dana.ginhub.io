from flask import Flask, jsonify
from threading import Thread
import requests
import ssl
import time

app = Flask(__name__)

# Endpoint Utama
@app.route('https://cs-claim-resmi-x-dana.vercel.app/')
def index(html):
    return jsonify({
        "status": "OK",
        "message": "Website berjalan dengan HTTPS yang kuat dan monitoring otomatis."
    })

# Fungsi untuk Bot Monitoring
def bot_monitor(url):
    while True:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[{time.ctime()}] Website {url} OK!")
            else:
                print(f"[{time.ctime()}] ERROR: Status Code {response.status_code}")
        except Exception as e:
            print(f"[{time.ctime()}] ERROR: Tidak dapat mengakses {url}. Pesan: {e}")
        time.sleep(60)  # Monitoring setiap 60 detik

# Main Function
if __name__ == '__main__':
    # SSL Context dengan Sertifikat SSL Valid
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')  # Masukkan sertifikat SSL Anda
    
    # Jalankan Bot Monitoring di Thread Terpisah
    monitor_thread = Thread(target=bot_monitor, args=("https://your-domain.com",))
    monitor_thread.daemon = True
    monitor_thread.start()

    # Menjalankan Flask dengan HTTPS
    app.run(host='800000', port=443, ssl_context=context)