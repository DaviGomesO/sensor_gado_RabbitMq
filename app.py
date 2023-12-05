from flask import Flask, render_template
import threading
from consumidor_dentro import RabbitmqConsumer_in
from consumidor_fora import RabbitmqConsumer_out

app = Flask(__name__)

# Listas para armazenar as mensagens recebidas
mensagens_dentro = []
mensagens_fora = []

def minha_callback_dentro(ch, method, properties, body):
  # Adiciona a mensagem na lista de mensagens
  mensagens_dentro.append(body)

def minha_callback_fora(ch, method, properties, body):
  # Adiciona a mensagem na lista de mensagens
  mensagens_fora.append(body)

# Inicializa os consumidores
rabbitmq_consumer_in = RabbitmqConsumer_in(minha_callback_dentro)
rabbitmq_consumer_out = RabbitmqConsumer_out(minha_callback_fora)

# Inicia os consumidores em threads separadas
threading.Thread(target=rabbitmq_consumer_in.start).start()
threading.Thread(target=rabbitmq_consumer_out.start).start()

@app.route('/')
def home():
  # Renderiza um template HTML com as mensagens
  return render_template('index.html', mensagens_dentro=mensagens_dentro[-1], mensagens_fora=mensagens_fora[-1])

if __name__ == '__main__':
  app.run(debug=True)
