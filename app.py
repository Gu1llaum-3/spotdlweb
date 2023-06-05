from flask import Flask, request, redirect, url_for, send_file, render_template, send_from_directory
from subprocess import run
import os

app = Flask(__name__)


def process_file(urls):
    download_param_album = '{artist}/{album}/{artist} - {title}'
    download_param_playlist = '{playlist}/{artists}/{album} - {title} {artist}'
    download_param_track = '{artist}/{album}/{artist} - {title}'

    os.chdir('downloads')
    os.system(f'rm -rf *')

    for url in urls:
        if url:
            if "album" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_album])
            elif "playlist" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_playlist])
            elif "track" in url:
                run(['python3', '-m', 'spotdl', url, '--output', download_param_track])
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

        urls = [url1, url2, url3]

        # Vérifier si au moins un champ est vide
        if not url1 and not url2 and not url3 :
            return render_template('erreur.html')

        # Créer le dossier 'downloads' s'il n'existe pas
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        process_file(urls)

    # path = "downloads/musics.zip"
    # return send_file(path, as_attachment=True)
    return render_template('finish.html')

@app.route('/zip', methods=['GET', 'POST'])
def zip():
    path = "downloads/musics.zip"
    return send_file(path, as_attachment=True)

@app.errorhandler(404)
def page_not_found(error):  # error est necessaire
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
