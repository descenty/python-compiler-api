import pika
import json
from tester import run_tests


def callback(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    print(" [x] Received %r" % data['id'])
    result = run_tests(data['code'], data['test_code'], data['function_name'])
    ch.basic_publish(exchange='', routing_key=properties.reply_to, properties=pika.BasicProperties(
        correlation_id=properties.correlation_id), body=json.dumps({"id": data['id'], "result": result}))


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tests')
channel.basic_consume(queue='tests',
                      auto_ack=True,
                      on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
