from flask import Flask, request, redirect, url_for, send_file, render_template, send_from_directory
from subprocess import run
from datetime import datetime
import os, logging, json

app = Flask(__name__)

#Page d'identification en cours de développement
# with open("identifiants.json") as f:
#   identifiants = json.load(f)

def process_file(urls):
    download_param_album = '{artist}/{album}/{artist} - {title}'
    download_param_playlist = '{playlist}/{artists}/{album} - {title} {artist}'

    # Créer le dossier 'downloads' s'il n'existe pas
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    os.chdir('downloads')
    os.system(f'rm -rf *')

    for url in urls:
        if url:
            if "album" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_album])
            elif "playlist" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_playlist])
    
    run(['zip', '-r', 'musics.zip', '.'])
    os.chdir('../')

@app.route('/', methods=['GET', 'POST'])
def upload_form():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_file():

  if request.method == 'POST':
        url1 = request.form['url1']
        url2 = request.form['url2']
        url3 = request.form['url3']
        url4 = request.form['url4']
        url5 = request.form['url5']

        # Vérifier si au moins un champ est vide
        if not url1 and not url2 and not url3 and not url4 and not url5:
            return render_template('erreur.html')

        urls = [url1, url2, url3, url4, url5]
  
  process_file(urls)
  PATH = "downloads/musics.zip"
  return send_file(PATH, as_attachment=True)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)