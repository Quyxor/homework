import argparse
import string
import logging
import socket
import sys
import threading
from time import sleep


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] %(asctime).19s [%(filename)s:%(lineno)d] :: %(message)s')
logger = logging.getLogger(__name__)


class Server(object):
    def __init__(self, host='127.0.0.1', port=1234, rotn=1):
        self.__address = (host, port)
        self.__server_socket = None
        self.__connections = {}
        self.__rotn = rotn


    def listen(self):
        self.__server_socket = sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(self.__address)
        sock.listen(10)
        logger.info('Сервер запущен по адресу {}'.format(self.__address))

        thread = threading.Thread(target=self.recv_conn, daemon=True)
        thread.start()


    def recv_conn(self):
        while True:
            conn, addr = self.__server_socket.accept()
            self.register(conn)
            data = conn.recv(1024)
            if not data:
                break
            conn.send(self.make_response(data, self.__rotn))
            sleep(1)

        conn.close()


    def register(self, sock):
        """Регистрирует новое соединение."""
        user = sock.getpeername()
        self.__connections[user] = sock
        msg = 'Новое соединение: {}'.format(user)
        logger.info(msg)


    def make_response(self, data, rotn):
        __result = ''
        __rotn = rotn
        __data = data.decode("utf-8")

        for char in __data:
            alpha = string.ascii_uppercase if char.isupper() else string.ascii_lowercase

            if char.isalpha():
                __result += alpha[(alpha.index(char) + __rotn) % len(alpha)]
            else:
                __result += char

        return __result.encode("utf-8")


class Client(object):
    def __init__(self, host, port):
        self.__address = (host, port)
        self.__client_socket = None


    def connect(self):
        self.__client_socket = sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect(self.__address)
            msg = 'Установлено соединение с {}'.format(self.__address)
            logger.info(msg)
        except socket.error:
            logger.error('Сервер недоступен')

        while True:
            __message = input()

            if __message == '\q':
                break
            else:
                sock.send(__message.encode("utf-8"))
                __data = sock.recv(1024)
                __data = __data.decode("utf-8")
                print(__data)
            sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Клиент для шифрования')

    parser.add_argument('-r', '--rotn',
                        help='Значение сдвига',
                        default=1,
                        type=int)

    arguments = parser.parse_args()
    server = Server('127.0.0.1', 1234, arguments.rotn)
    client = Client('127.0.0.1', 1234)

    try:
        server.listen()
        client.connect()
    except Exception as msg:
        logger.error(msg)
    finally:
        sys.exit(0)
