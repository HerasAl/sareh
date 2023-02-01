from musicdl import musicdl
import json
import os
import requests

def music(song):
    config = {'logfilepath': 'musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': 20, 'proxies': {}}
    target_srcs = [
        'joox'
    ]
    client = musicdl.musicdl(config=config)
    client = musicdl.musicdl(config=config)
    search_results = client.search(song, target_srcs)
    
    data = json.loads(json.dumps(search_results).encode('utf8'))
    lista = []
    for songs in data['joox']:
        lista.append(
            {
                'cancion':songs['songname'],
                'album':songs['album'],
                'autor':songs['singers'],
                'url':songs['download_url'],
                'fuente':songs['source']
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
    
    