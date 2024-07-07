import queue
import time
import threading
import random

request_queue = queue.Queue()


def generate_request():
    while True:
        # Генеруємо унікальний ідентифікатор заявки
        request_id = random.randint(1, 1000)
        request_queue.put(request_id)
        print(f"Заявка {request_id} додана до черги.")
        # Затримка для імітації нерегулярного надходження заявок
        time.sleep(random.uniform(0.5, 2))


def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Обробка заявки {request_id}.")
            # Затримка для імітації часу обробки заявки
            time.sleep(random.uniform(1, 3))
        else:
            print("Черга порожня. Очікування нових заявок...")
            time.sleep(1)


# Запускаємо функції у окремих потоках
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()
