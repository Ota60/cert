from OpenSSL import crypto

def verify_signature(cert_path, sig_path, file_path):
    try:
        # Sertifikayı yükle
        with open(cert_path, "rb") as cert_file:
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file.read())

        # İmzayı yükle
        with open(sig_path, "rb") as sig_file:
            signature = sig_file.read()

        # Dosyayı yükle
        with open(file_path, "rb") as file:
            data = file.read()

        # Açık anahtarla imzayı doğrula
        pub_key = cert.get_pubkey()
        crypto.verify(cert, signature, data, "sha256")
        return "İmza doğrulandı. Dosya güvenilir."
    except crypto.Error as e:
        return f"İmza doğrulanamadı: {e}"
    except Exception as e:
        return f"Hata: {e}"

# Dosya yollarını belirtin
cert_path = "mycert.crt"
sig_path = "fatihiyi.sig"
file_path = "fatihiyi.py"

# Doğrulama işlemi
result = verify_signature(cert_path, sig_path, file_path)
print(result)
