# FakeAP

<p align="center">
<img src="Logotipo.png" width="278px">
</p>

El repositorio "FakeAP" es una herramienta de código abierto diseñada para facilitar la creación de puntos de acceso Wi-Fi falsos, también conocidos como "AP falsos". Un AP falso es una red Wi-Fi simulada que se asemeja a una red legítima, pero que está controlada por un atacante. Esta herramienta puede ser utilizada con fines educativos y de investigación, así como para probar la seguridad de redes Wi-Fi existentes.

Una vez que un usuario se conecta a la Fake AP, el hacker puede interceptar y registrar toda la información transmitida entre el usuario y la red, lo que puede poner en riesgo la privacidad y la seguridad de los datos del usuario.

### Requisitos

* Kali Linux o Parrot OS

* Adaptador Wireless compatible con modo monitor

<br>

En el archivo **hostapd.conf** puede configurar el nombre de red que se va a crear y la contraseña, en el archivo **dnsmasq.conf** puede configurar para guardar el tráfico de red en un archivo **.log**

```
iwconfig (Primero verificar que este conectado el adaptador)

sudo pip install pywifi --break-system-packages

git clone https://github.com/bl4ck44/FakeAP.git

cd FakeAP

sudo chmod +x fakeAP.py

sudo python3 fakeAP.py
```

### ⚠️ **Aviso**

Este script ha sido desarrollado únicamente con fines **educativos y de investigación en ciberseguridad**.

No me responsabilizo del mal uso que se pueda dar ni de los daños que puedan ocasionarse por su ejecución.

El uso indebido de este material puede ser **ilegal**.