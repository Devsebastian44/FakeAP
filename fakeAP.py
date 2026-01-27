import pywifi
import os
import subprocess

os.system("clear")

print("")

print("\033[32m                                ███████╗ █████╗ ██╗  ██╗███████╗ █████╗ ██████╗     \033[0m")
print("\033[32m                                ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔══██╗    \033[0m")
print("\033[32m                                █████╗  ███████║█████╔╝ █████╗  ███████║██████╔╝    \033[0m")
print("\033[32m                                ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██║██╔═══╝     \033[0m")
print("\033[32m                                ██║     ██║  ██║██║  ██╗███████╗██║  ██║██║         \033[0m")
print("\033[32m                                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝         \033[0m")
print("                                                                                                   ")
print("\033[32m                                           https://github.com/bl4ck44                \033[0m")


if os.geteuid() == 0:
    pass
else:
    print("[+] Ejecute este script como root (usando sudo).\n")
    exit(1)



# Inicializar variables globales
primer_adaptador_nombre = None
adaptador = None

# Detectar adaptadores wireless disponibles
try:
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()
    
    if len(interfaces) == 0:
        print("\033[1m[+] No se encontraron adaptadores inalámbricos disponibles.\033[0m")
    else:
        print("\033[1m\n[+] Adaptadores inalámbricos disponibles:\n\033[0m")
        primer_adaptador_nombre = interfaces[0].name()
        
        for i, iface in enumerate(interfaces, start=1):
            print(f"{i}. Nombre: {iface.name()}")
except Exception as e:
    print(f"\033[1m[+] Error al detectar adaptadores wireless: {e}\033[0m")



# Detectar adaptador de red con conexión a Internet
try:
    resultado = subprocess.check_output(["ip", "route", "show", "default"])
    resultado = resultado.decode("utf-8")
    
    for linea in resultado.split('\n'):
        if "default" in linea and "dev" in linea:
            partes = linea.split()
            try:
                indice = partes.index("dev")
                if indice < len(partes) - 1:
                    adaptador = partes[indice + 1]
                    break
            except ValueError:
                continue
                
except (subprocess.CalledProcessError, Exception) as e:
    print(f"\033[1m[+] Error al detectar adaptador de red: {e}\033[0m")

# Mostrar información del adaptador detectado
if adaptador:
    print(f"\033[1m\n[+] Adaptador de red conectado a Internet: {adaptador}\033[0m")
else:
    print("\033[1m\n[+] No se pudo determinar el adaptador de red conectado a Internet.\033[0m")



while True:                                                   
    print("\n\033[1m[1] Instalar requisitos\033[0m")
    print("\033[1m[2] Configurar archivos\033[0m")
    print("\033[1m[3] Configurar FakeAP\033[0m")
    print("\033[1m[4] Procesar los registros para ordenar por IP\033[0m")
    print("\033[1m[5] Reiniciar la red y el sistema\033[0m")
    print("\033[1m[6] Salir\033[0m")
    opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
    if opcion == "1":
        print("\033[1m\n[+] Instalando\n \033[0m")
        os.system("sudo apt install hostapd dnsmasq aircrack-ng tcpdump tshark xterm wpasupplicant")
        print("\033[1m\n[+] Requisistos instalados\n \033[0m")
    elif opcion == "2":
        # Configurar archivos
        print("\033[1m\n[+] Configurar archivos del FakeAP\033[0m")
        while True:
            print("\n\033[1m--- Configuración de Archivos ---\033[0m")
            print("\033[1m[1] Configurar puerta de enlace (dnsmasq.conf)\033[0m")
            print("\033[1m[2] Cambiar SSID y contraseña (hostapd.conf)\033[0m")
            print("\033[1m[3] Configurar rango de IPs (dnsmasq.conf)\033[0m")
            print("\033[1m[4] Volver al menú principal\033[0m")
            
            subopcion = input("\033[1m[+] Seleccione una opción: \033[0m")
            
            if subopcion == "1":
                # Configurar puerta de enlace
                print("\033[1m\n[+] Configurar puerta de enlace predeterminada\033[0m")
                try:
                    resultado_gateway = subprocess.check_output(["ip", "route", "show", "default"])
                    gateway_actual = resultado_gateway.decode("utf-8").split()[2]
                    print(f"\033[1m[+] Puerta de enlace actual detectada: {gateway_actual}\033[0m")
                    
                    usar_actual = input("\033[1m[+] ¿Desea usar esta puerta de enlace? (s/n): \033[0m")
                    
                    if usar_actual.lower() == 's':
                        gateway = gateway_actual
                    else:
                        gateway = input("\033[1m[+] Ingrese la nueva puerta de enlace (ej: 192.168.1.1): \033[0m")
                    
                    with open('dnsmasq.conf', 'r') as file:
                        contenido = file.read()
                    
                    contenido = contenido.replace('dhcp-option=3,192.168.1.1', f'dhcp-option=3,{gateway}')
                    contenido = contenido.replace('dhcp-option=6,192.168.1.1', f'dhcp-option=6,{gateway}')
                    
                    # Actualizar rango DHCP basado en la puerta de enlace
                    gateway_base = gateway.rsplit('.', 1)[0]  # Obtener 192.168.3 de 192.168.3.1
                    nuevo_rango = f"dhcp-range={gateway_base}.2,{gateway_base}.30,255.255.255.0,12h"
                    
                    # Buscar y reemplazar la línea dhcp-range existente
                    for linea in contenido.split('\n'):
                        if 'dhcp-range=' in linea:
                            contenido = contenido.replace(linea, nuevo_rango)
                            break
                    
                    print(f"\033[1m[+] Rango DHCP actualizado a: {nuevo_rango}\033[0m")
                    
                    with open('dnsmasq.conf', 'w') as file:
                        file.write(contenido)
                    
                    print(f"\033[1m[+] Puerta de enlace actualizada a: {gateway}\033[0m")
                    print(f"\033[1m[+] Rango DHCP actualizado automáticamente a: {nuevo_rango}\033[0m")
                    print("\033[1m[+] Archivo dnsmasq.conf actualizado correctamente\033[0m")
                    
                except FileNotFoundError:
                    print("\033[1m[+] Error: Archivo dnsmasq.conf no encontrado\033[0m")
                except Exception as e:
                    print(f"\033[1m[+] Error al configurar puerta de enlace: {e}\033[0m")
                input("\033[1m[+] Presione Enter para continuar...\033[0m")
                    
            elif subopcion == "2":
                # Cambiar SSID y contraseña
                print("\033[1m\n[+] Configurar SSID y contraseña del AP falso\033[0m")
                try:
                    with open('hostapd.conf', 'r') as file:
                        contenido = file.read()
                    
                    # Leer valores actuales
                    ssid_actual = "Wiifi-nombre"
                    pass_actual = "contraseña"
                    
                    for linea in contenido.split('\n'):
                        if 'ssid=' in linea:
                            ssid_actual = linea.split('=')[1]
                        elif 'wpa_passphrase=' in linea:
                            pass_actual = linea.split('=')[1]
                    
                    print(f"\033[1m[+] SSID actual: {ssid_actual}\033[0m")
                    print(f"\033[1m[+] Contraseña actual: {pass_actual}\033[0m")
                    
                    nuevo_ssid = input("\033[1m[+] Ingrese el nuevo SSID: \033[0m")
                    nueva_pass = input("\033[1m[+] Ingrese la nueva contraseña (mínimo 8 caracteres): \033[0m")
                    
                    if len(nueva_pass) < 8:
                        print("\033[1m[+] Error: La contraseña debe tener al menos 8 caracteres\033[0m")
                        input("\033[1m[+] Presione Enter para continuar...\033[0m")
                        continue
                    
                    if len(nuevo_ssid.strip()) == 0:
                        print("\033[1m[+] Error: El SSID no puede estar vacío\033[0m")
                        input("\033[1m[+] Presione Enter para continuar...\033[0m")
                        continue
                    
                    contenido = contenido.replace(f'ssid={ssid_actual}', f'ssid={nuevo_ssid}')
                    contenido = contenido.replace(f'wpa_passphrase={pass_actual}', f'wpa_passphrase={nueva_pass}')
                    
                    with open('hostapd.conf', 'w') as file:
                        file.write(contenido)
                    
                    print(f"\033[1m[+] SSID actualizado a: {nuevo_ssid}\033[0m")
                    print(f"\033[1m[+] Contraseña actualizada correctamente\033[0m")
                    
                except FileNotFoundError:
                    print("\033[1m[+] Error: Archivo hostapd.conf no encontrado\033[0m")
                except Exception as e:
                    print(f"\033[1m[+] Error al configurar hostapd.conf: {e}\033[0m")
                input("\033[1m[+] Presione Enter para continuar...\033[0m")
                    
            elif subopcion == "3":
                # Configurar rango de IPs
                print("\033[1m\n[+] Configurar rango de IPs DHCP\033[0m")
                try:
                    with open('dnsmasq.conf', 'r') as file:
                        contenido = file.read()
                    
                    rango_actual = "dhcp-range=192.168.3.2,192.168.3.30,255.255.255.0,12h"
                    for linea in contenido.split('\n'):
                        if 'dhcp-range=' in linea:
                            rango_actual = linea
                            break
                    
                    print(f"\033[1m[+] Rango actual: {rango_actual}\033[0m")
                    
                    print("\033[1m[+] Ingrese el nuevo rango de IPs:\033[0m")
                    ip_inicio = input("\033[1m[+] IP inicial (ej: 192.168.3.2): \033[0m")
                    ip_fin = input("\033[1m[+] IP final (ej: 192.168.3.30): \033[0m")
                    Mascara = input("\033[1m[+] Máscara de red (ej: 255.255.255.0): \033[0m")
                    
                    # Validación básica de IPs
                    if not ip_inicio or not ip_fin or not Mascara:
                        print("\033[1m[+] Error: Todos los campos son obligatorios\033[0m")
                        input("\033[1m[+] Presione Enter para continuar...\033[0m")
                        continue
                    
                    nuevo_rango = f"dhcp-range={ip_inicio},{ip_fin},{Mascara},12h"
                    contenido = contenido.replace(rango_actual, nuevo_rango)
                    
                    with open('dnsmasq.conf', 'w') as file:
                        file.write(contenido)
                    
                    print(f"\033[1m[+] Rango DHCP actualizado a: {nuevo_rango}\033[0m")
                    
                except FileNotFoundError:
                    print("\033[1m[+] Error: Archivo dnsmasq.conf no encontrado\033[0m")
                except Exception as e:
                    print(f"\033[1m[+] Error al configurar rango DHCP: {e}\033[0m")
                input("\033[1m[+] Presione Enter para continuar...\033[0m")
                    
            elif subopcion == "4":
                print("\033[1m\n[+] Volviendo al menú principal\033[0m")
                break
            else:
                print("\033[1m[+] Opción inválida\033[0m")
    elif opcion == "3":
        # Configurar FakeAP
        if not primer_adaptador_nombre:
            print("\033[1m[+] Error: No se encontraron adaptadores wireless\033[0m")
            continue
            
        print("\033[1m\n[+] Configurando e iniciando FakeAP\033[0m")
        
        # Verificar que los archivos de configuración existan
        if not os.path.exists('hostapd.conf') or not os.path.exists('dnsmasq.conf'):
            print("\033[1m[+] Error: Archivos de configuración no encontrados\033[0m")
            continue
            
        os.system(f"airmon-ng start {primer_adaptador_nombre}")
        os.system(f"ifconfig {primer_adaptador_nombre} up 192.168.3.1 netmask 255.255.255.0")
        os.system("route add -net 192.168.3.0 netmask 255.255.255.0 gw 192.168.3.1")
        
        if adaptador:
            os.system(f"iptables --table nat --append POSTROUTING --out-interface {adaptador} -j MASQUERADE")
        os.system(f"iptables --append FORWARD --in-interface {primer_adaptador_nombre} -j ACCEPT")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        
        print("\033[1m[+] Iniciando servicios en ventanas separadas...\033[0m")
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'tcpdump -i {primer_adaptador_nombre} -w trafico.pcap; exec bash'])
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'hostapd hostapd.conf -i {primer_adaptador_nombre}; exec bash'])
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'dnsmasq -C dnsmasq.conf -d -i {primer_adaptador_nombre}; exec bash'])
        
    elif opcion == "4":
        # Procesar registros
        if os.path.exists('trafico.pcap'):
            print("\033[1m\n[+] Procesando archivo de captura\033[0m")
            os.system("tshark -r trafico.pcap -T fields -e ip.src -e ip.dst > direcciones_ip.txt")
            os.system("sort direcciones_ip.txt | uniq > direcciones_ip_ordenadas.txt")
            print("\033[1m[+] IPs procesadas y guardadas en direcciones_ip_ordenadas.txt\033[0m")
        else:
            print("\033[1m[+] Error: No se encontró el archivo trafico.pcap\033[0m")
            
    elif opcion == "5":
        # Reiniciar red
        print("\033[1m\n[+] Reiniciando servicios de red\033[0m")
        os.system("systemctl restart NetworkManager.service")
        
        reiniciar = input("\033[1m[+] ¿Desea reiniciar el sistema completo? (s/n): \033[0m")
        if reiniciar.lower() == 's':
            print("\033[1m[+] Reiniciando el sistema en 3 segundos...\033[0m")
            os.system("sleep 3 && reboot")
        else:
            print("\033[1m[+] Servicios de red reiniciados\033[0m")
            
    elif opcion == "6":
        # Salir del programa
        print("\033[1m\n[+] Saliendo del programa\033[0m")
        break
    else:
        print("\033[1m[+] Opción inválida\033[0m")
