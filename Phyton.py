import random
import time

# Funções para simular leituras de sensores
def read_temperature():
    return random.uniform(25.0, 35.0)  # Simula temperatura entre 25.0 e 35.0 graus Celsius

def read_ph():
    return random.uniform(7.0, 8.5)  # Simula pH entre 7.0 e 8.5

def read_light():
    return random.uniform(300, 800)  # Simula níveis de luz entre 300 e 800 lux

def read_nutrients():
    return random.uniform(0.0, 2.0)  # Simula níveis de nutrientes entre 0.0 e 2.0 (arbitrário)

# Função para ajustar parâmetros (ex: ativar bomba)
def adjust_parameters(param, value):
    if param == "temperature":
        if value > 30.0:
            print("Ajustando temperatura: Ligando o sistema de resfriamento.")
        else:
            print("Temperatura está dentro do intervalo desejado.")
    elif param == "ph":
        if value < 7.5:
            print("Ajustando pH: Adicionando solução alcalina.")
        else:
            print("pH está dentro do intervalo desejado.")
    elif param == "light":
        if value < 400:
            print("Ajustando luz: Aumentando a iluminação.")
        else:
            print("Nível de luz está dentro do intervalo desejado.")
    elif param == "nutrients":
        if value < 1.0:
            print("Ajustando nutrientes: Adicionando nutrientes à água.")
        else:
            print("Nível de nutrientes está dentro do intervalo desejado.")

# Função principal de monitoramento
def monitor_corals():
    while True:
        temperature = read_temperature()
        ph = read_ph()
        light = read_light()
        nutrients = read_nutrients()
        
        print("\nLeituras Atuais:")
        print(f"Temperatura: {temperature:.2f} °C")
        print(f"pH: {ph:.2f}")
        print(f"Luz: {light:.2f} lux")
        print(f"Nutrientes: {nutrients:.2f}")
        
        # Ajuste dos parâmetros com base nas leituras
        adjust_parameters("temperature", temperature)
        adjust_parameters("ph", ph)
        adjust_parameters("light", light)
        adjust_parameters("nutrients", nutrients)
        
        time.sleep(5)  # Espera 5 segundos antes de realizar novas leituras

# Inicia o monitoramento
monitor_corals()
