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

3. Clona el repositorio y ejecuta el script:

```bash
git clone https://github.com/bl4ck44/FakeAP.git
cd FakeAP
sudo chmod +x fakeAP.py
sudo python3 fakeAP.py
```

---

## 📡 Compatibilidad de Adaptadores Wireless

### Adaptadores Recomendados
- **TP-Link TL-WN722N v1/v2** (Chipset Atheros AR9271) ✅
- **Alfa AWUS036H** (Chipset Ralink RT3070) ✅
- **Panda PAU09** (Chipset Ralink RT5572) ✅

### Adaptadores NO Compatibles
- **TP-Link TL-WN722N v3.x** (Chipset RTL8812AU/RTL8821AU) ❌

### Si tienes TL-WN722N v3.x
Puedes intentar instalar drivers específicos:

```bash
# Instala drivers para RTL8812AU
git clone https://github.com/aircrack-ng/rtl8812au.git
cd rtl8812au
sudo make install
sudo modprobe rtl8812au
```

Para verificar tu versión:
```bash
lsusb | grep TP-Link
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
