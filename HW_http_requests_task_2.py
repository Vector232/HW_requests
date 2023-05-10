import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path) # выделяем ТОЛЬКО имя файла, а не весь путь к нему 
        
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

        # добываем ссылку на загрузку при условии, что она возможна
        # в данном случае кинем файл в основную папку и перезапишем, если уже есть с таким названием
        res = requests.get(f'{url}/upload?path={file_name}&overwrite={True}', headers=headers).json() 
        try:
            with open(file_path, 'rb') as f:
                # если по какой-то причине мы не можем закинуть файл в нужное место, то и ссылки не будет(соответственно и ключа в json файле)
                if res.get('href'): 
                    response = requests.put(res['href'], files={'file':f})
                else:
                    return res
        except:
            return f'No such file or directory: {file_path}'
        return response
        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('path_to_file: ')
    token = input('token: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)