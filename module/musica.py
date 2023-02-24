from musicdl import musicdl
import json
import os
import requests

def music(song):
    config = {'logfilepath': '.musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': 5, 'proxies': {}}
    target_srcs = [
        'kugou', 'kuwo', 'qqmusic', 'qianqian', 'fivesing',
    'netease', 'migu', 'joox', 'yiting','ximalaya','lizhi',
    ]
    client = musicdl.musicdl(config=config)
    search_results = client.search(song, target_srcs)
    
    data = json.loads(json.dumps(search_results).encode('utf8'))
    lista = []
    if data['joox']:
        for songs in data['joox']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
    if data['kugou']:
        for songs in data['kugou']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
    if data['migu']:
        for songs in data['migu']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
    if data['qianqian']:
        for songs in data['qianqian']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
            
    if data['qqmusic']:
        for songs in data['qqmusic']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
            
    if data['yiting']:
        for songs in data['yiting']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
    if data['ximalaya']:
        for songs in data['ximalaya']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
    
    if data['lizhi']:
        for songs in data['lizhi']:
            lista.append(
                {
                    'cancion':songs['songname'],
                    'album':songs['album'],
                    'autor':songs['singers'],
                    'url':songs['download_url'],
                    'fuente':songs['source'],
                    'ext':songs['ext'],
                    'filesize':songs['filesize']
                })
        
    return lista


def downSave(data):
    folder = "./files/music/" + data['autor']
    if not os.path.exists(folder):
        os.makedirs(folder)

    cancion = requests.get(data['url'])
    with open(folder + "/" + data['cancion'] + ".mp3", 'wb') as file:
        file.write(cancion.content)
    return {'status': 1}