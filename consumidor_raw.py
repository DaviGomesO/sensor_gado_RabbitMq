import pika
from pika import PlainCredentials

# Função que retorna 
def minha_callback(ch, method, properties, body):
  print(body)

# Passando os parametros da conexão
connection_parameters = pika.ConnectionParameters(
  host="localhost",
  port=5672,
  credentials=PlainCredentials(
    username='guest', password='guest'
  )
)

# Abrindo o canal de consumidor
channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(
  queue="data_queue",
  durable=True
)
# Fazendo um consumo basico
channel.basic_consume(
  queue="data_queue",
  auto_ack=True,
  on_message_callback=minha_callback
)

print(f'Listen RabbitMQ on Port 5672')
channel.start_consuming()