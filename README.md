# FakeAP

<p align="center">
  <img src="./Img/Logo.png" height="300px" width="350px">
</p>

**FakeAP** es una herramienta de código abierto diseñada para crear puntos de acceso Wi-Fi falsos (AP falsos). Simula redes legítimas para fines **educativos y de investigación en ciberseguridad**, permitiendo evaluar la seguridad de redes inalámbricas.

---

## ⚙️ Requisitos

- Kali Linux o Parrot OS
- Adaptador Wireless compatible con modo monitor
- Python 3.8 o superior

---

## 🛠️ Configuración

1. Verifica que el adaptador esté conectado:

```bash
iwconfig
```

2. Instala la librería necesaria:

```bash
sudo pip install pywifi --break-system-packages
```

3. Clona el repositorio y ejecuta el script:

```bash
git clone https://github.com/bl4ck44/FakeAP.git
cd FakeAP
sudo chmod +x fakeAP.py
sudo python3 fakeAP.py
```

---

## 🧩 Personalización

- **hostapd.conf** → Configura el nombre de la red (SSID) y la contraseña del AP falso.
- **dnsmasq.conf** → Define parámetros de red y permite guardar el tráfico en un archivo `.log`.

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
