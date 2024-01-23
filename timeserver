import socket
import datetime


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1303))
    server_socket.listen(1)

    print("Сервер запущен. Ожидание подключения...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Подключено клиентом: {client_address}")

            current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            client_socket.send(current_time.encode())

            client_socket.close()
            print(f"Соединение с {client_address} закрыто")

    except KeyboardInterrupt:
        print("Сервер остановлен.")


if __name__ == "__main__":
    run_server()
