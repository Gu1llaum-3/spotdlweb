from flask import Flask, request, redirect, url_for, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        url1 = request.form['url1']
        url2 = request.form['url2']
        url3 = request.form['url3']
        url4 = request.form['url4']
        url5 = request.form['url5']

        # Vérifier si au moins un champ est vide
        if not url1 and not url2 and not url3 and not url4 and not url5:
            return render_template('erreur.html')

        result = process_file(url1, url2, url3, url4, url5)
    return render_template('download_complete.html')

def process_file(url1, url2, url3, url4, url5):
    path = os.path.expanduser('~/musics/downloads')
    download_param_album = '{artist}/{album}/{artist} - {title}'
    download_param_playlist = '{playlist}/{artists}/{album} - {title} {artist}'

    # Télécharger chaque URL s'il n'est pas vide
    if url1:
        if "album" in url1:
            #os.makedirs(f'{path}/download-1', exist_ok=True)
            os.chdir(f'{path}')
            os.system(f'python3 -m spotdl {url1} --output "{download_param_album}"')
        elif "playlist" in url1:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url1} --output "{download_param_playlist}"')

    if url2:
        if "album" in url2:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url2} --output "{download_param_album}"')
        elif "playlist" in url2:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url2} --output "{download_param_playlist}"')

    if url3:
        if "album" in url3:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url3} --output "{download_param_album}"')
        elif "playlist" in url3:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url3} --output "{download_param_playlist}"')

    if url4:
        if "album" in url4:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url4} --output "{download_param_album}"')
        elif "playlist" in url4:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url4} --output "{download_param_playlist}"')

    if url5:
        if "album" in url5:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url5} --output "{download_param_album}"')
        elif "playlist" in url5:
            os.chdir(f"{path}")
            os.system(f'python3 -m spotdl {url5} --output "{download_param_playlist}"')
    
    os.chdir(f'{path}')
    os.system(f'zip -r musics.zip ./')

@app.route('/download', methods=['GET'])
def download():
    PATH='/home/gu1ll4um3/musics/downloads/musics.zip'
    return send_file(PATH,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
