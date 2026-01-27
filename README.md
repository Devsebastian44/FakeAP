# FakeAP

<p align="center">
  <img src="./Img/Logo.png" height="300px" width="350px">
</p>

**FakeAP** es una herramienta de código abierto diseñada para crear puntos de acceso Wi-Fi falsos (AP falsos). Simula redes legítimas para fines **educativos y de investigación en ciberseguridad**, permitiendo evaluar la seguridad de redes inalámbricas.

---

## ⚙️ Requisitos

- Kali Linux o Parrot OS
- Adaptador Wireless compatible con modo monitor y modo AP
- Python 3.8 o superior

---

## 🛠️ Configuración

1. Verifica que el adaptador esté conectado:

```bash
iwconfig
```

2. Instala las librerías necesarias:

```bash
# Instala dependencias del sistema
sudo apt update
sudo apt install python3-pip python3-dev

# Instala las librerías Python
sudo pip install -r requirements.txt --break-system-packages
```

3. Inicia wpa_supplicant y ejecuta el script:

```bash
# Inicia el servicio wpa_supplicant
sudo systemctl start wpa_supplicant

# Clona el repositorio y ejecuta el script
git clone https://github.com/Devsebastian44/FakeAP.git
cd FakeAP
sudo chmod +x fakeAP.py
sudo python3 fakeAP.py
```

---


## 📂 Estructura del proyecto

```
FakeAP/
│── fakeAP.py           # Script principal para levantar el AP falso
│── hostapd.conf        # Configuración del punto de acceso
│── dnsmasq.conf        # Configuración del servidor DHCP/DNS
```

---

## ⚠️ Aviso legal

Este script ha sido desarrollado únicamente con fines **educativos y de investigación en ciberseguridad**. El uso indebido de este material puede ser **ilegal**. No me responsabilizo del mal uso ni de los daños que puedan ocasionarse por su ejecución.
