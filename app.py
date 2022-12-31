from flask import Flask, request, redirect, url_for, send_file, render_template
from subprocess import run
import os

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

def process_file(urls):
    # path = os.path.expanduser('~/musics/downloads')
    #path = '/home/gu1ll4um3/github/SpotDL_Web/downloads'
    #path = 'downloads/'
    download_param_album = '{artist}/{album}/{artist} - {title}'
    download_param_playlist = '{playlist}/{artists}/{album} - {title} {artist}'

    os.chdir('downloads')
    #os.system(f'rm -rf *')

    for url in urls:
        if url:
            if "album" in url:
                #os.system(f'python3 -m spotdl {url} --output "{download_param_album}"')
                run(['python3', '-m', 'spotdl', url, '--output', download_param_album])
            elif "playlist" in url:
                os.system(f'python3 -m spotdl {url} --output "{download_param_playlist}"')
            
    
    # os.system(f'zip -r musics.zip ./downloads')
    run(['zip', '-r', 'musics.zip', '.'])

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

        urls = [url1, url2, url3, url4, url5]
        process_file(urls)
        #print(resultProcessFile)
        
        with open('/home/gu1ll4um3/github/SpotDL_Web/logs/erreurs.log', 'r') as f:
            result2 = f.readlines()
    return render_template('download_complete.html', result2=result2)

@app.route('/download', methods=['GET'])
def download():
    # PATH='/home/gu1ll4um3/musics/downloads/musics.zip'
    #os.chdir('downloads')
    PATH='downloads/musics.zip'
    return send_file(PATH,as_attachment=True)

# @app.route('/errors')
# def errors():
#    with open('erreurs.txt', 'r') as f:
#       lines = f.readlines()
#    return render_template('logs.html', lines=lines)

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
