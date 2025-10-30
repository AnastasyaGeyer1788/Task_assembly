# Учебный проект - Домашняя работа
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 8080

class MyServer(BaseHTTPRequestHandler):


    def do_GET(self):
        """Обрабатывает все GET-запросы и возвращает страницу Контакты"""
        try:
            # Читаем HTML файл contacts.html
            with open('contacts.html', 'r', encoding='utf-8') as file:
                page_content = file.read()

            # Отправляем успешный ответ
            self.send_response(200)
            # Устанавливаем Content-type как text/html
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            # Отправляем HTML содержимое (правильное кодирование)
            self.wfile.write(page_content.encode('utf-8'))

        except FileNotFoundError:
            # Если файл contacts.html не найден
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            error_message = """
            <html>
            <head><title>Ошибка 404</title></head>
            <body>
                <h1>Файл contacts.html не найден</h1>
                <p>Убедитесь, что файл contacts.html находится в той же папке что и app.py</p>
            </body>
            </html>
            """
            self.wfile.write(error_message.encode('utf-8'))

        except Exception as e:
            # Обработка других ошибок
            self.send_response(500)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            error_message = f"""
            <html>
            <head><title>Ошибка 500</title></head>
            <body>
                <h1>Внутренняя ошибка сервера</h1>
                <p>{str(e)}</p>
            </body>
            </html>
            """
            self.wfile.write(error_message.encode('utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), MyServer)
    print(f"Сервер запущен по адресу: http://{host_name}:{server_port}")
    print("Любой GET-запрос возвращает страницу 'Контакты'")
    print("Для остановки сервера нажмите Ctrl+C")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
