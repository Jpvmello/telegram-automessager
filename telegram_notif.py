import time
import random
import asyncio
import argparse
import telegram_send

import tracemalloc
tracemalloc.start()

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("arquivo_notif", type=str, help="Caminho para o arquivo contendo a lista de possíveis notificações.")
parser.add_argument("--seg-min", type=int, default=5*60, help="Tempo de notificação mínimo, em segundos.")
parser.add_argument("--seg-max", type=int, default=60*60, help="Tempo de notificação máximo, em segundos.")

args = parser.parse_args()
with open(args.arquivo_notif, "r", encoding="utf-8") as arquivo_notif:
    notificacoes = arquivo_notif.readlines()

print("Iniciado.")

async def enviar_notificacao(mensagem):
    await telegram_send.send(messages = [mensagem])

while True:
    intervalo = random.randint(args.seg_min, args.seg_max) # intervalo aleatório
    time.sleep(intervalo)
    
    mensagem = random.choice(notificacoes)
    asyncio.run(enviar_notificacao(mensagem))
    print("Notificação:", mensagem)