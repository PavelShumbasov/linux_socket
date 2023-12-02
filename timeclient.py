import socket
import sys


def run_client():
    server_ip = input("Введите IP адрес сервера: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (server_ip, 1303)

    try:
        client_socket.connect(server_address)
        data = client_socket.recv(1024)
        print(f"Получено от сервера: {data.decode()}")

    except socket.error as e:
        print(f"Ошибка подключения: {e}")
        sys.exit(1)

    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.")
        sys.exit(1)

    finally:
        client_socket.close()


if __name__ == "__main__":
    run_client()
