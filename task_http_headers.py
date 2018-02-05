'''
Напишите функцию http_headers_to_json, которая принимает два аргумента:

    путь к файлу с HTTP-заголовками
    путь к файлу с результатами (в формате JSON)

Функция выполняет конвертирование HTTP-заголовков в формат JSON.

Ключами в JSON-объекте становятся имена заголовков,
а значениями - значения заголовков.

Так же в JSON попадает дополнительная информация,
в зависимости от вида заголовка.
'''
import json


def http_headers_to_json(http_path, json_path):

    dict_req = {}
    dict_resp = {}
    dict_append = {}

    with open(http_path) as input_file, \
         open(json_path, 'w') as output_file:

        headers = input_file.read().split('\n')
        first_line = headers.pop(0).split(' ')

        for field in headers:
            if field != '':
                key, value = field.split(': ')
                dict_append[key] = value

        if 'HTTP' in first_line[0]:
            dict_resp['protocol'] = first_line.pop(0)
            dict_resp['status_code'] = first_line.pop(0)
            dict_resp['status_message'] = ' '.join(first_line)
            dict_resp.update(dict_append)
            json.dump(dict_resp, output_file, indent=4)
        else:
            dict_req['method'] = first_line.pop(0)
            dict_req['uri'] = first_line.pop(0)
            dict_req['protocol'] = first_line.pop(0)
            dict_req.update(dict_append)
            json.dump(dict_req, output_file, indent=4)


if __name__ == '__main__':
    http_headers_to_json('headers-1.txt', 'results-1.json')
    http_headers_to_json('headers-2.txt', 'results-2.json')
    http_headers_to_json('headers-3.txt', 'results-3.json')
