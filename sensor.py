import random
from produtor import RabbitMqPublisher_in, RabbitMqPublisher_out
from time import sleep

sleep(5)

produtor_dentro = RabbitMqPublisher_in()
produtor_fora = RabbitMqPublisher_out()

TOTAL_GADOS = 50
gados_dentro = TOTAL_GADOS
gados_fora = 0

def sensor():
    animal = random.randint(0, 100)
    if (animal % 2 == 0):
      return "in"
    else:
      return "out"

chamada = 1
while True:
  action = sensor()
  message = ""
  sleep(1)
  if action == "in" and gados_fora > 0:
      gados_dentro += 1
      gados_fora -= 1
      message = f'Dentro: {gados_dentro}, tempo de execucao: {chamada}'
      produtor_dentro.send_message(message)
  elif action == "out" and gados_dentro <= TOTAL_GADOS:
      gados_dentro -= 1
      gados_fora += 1
      message = f'Fora: {gados_fora}, tempo de execucao: {chamada}'
      produtor_fora.send_message(message)
  else: 
     message = "Todos os gados ja estao dentro!"
     message_fora = "Nenhum gado esta fora!"
     produtor_dentro.send_message(message)
     produtor_fora.send_message(message_fora)
     message += '\n'+ message_fora
  print(message)
  chamada += 1

print(f'Gados dentro: {gados_dentro}\nGados Fora: {gados_fora}')