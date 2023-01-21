#programa pra dizer com var e constantes se carro foi multado

velocidade = 59
local_carro = 101

RADAR_1 = 60 #limite de velocidade do radar 1
LOCAL_1 = 100 #local onde o radar esta
RADAR_RANGE = 1 #distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro <= (LOCAL_1 + RADAR_RANGE) \
    and local_carro >= (LOCAL_1 - RADAR_RANGE) \
        and velocidade > RADAR_1

if velocidade_carro_passou_radar_1:
    print("atencao: velocidade esta maior que do radar")
if carro_passou_radar_1:
    print(f"Carro multado no km{local_carro} do radar 1!!")