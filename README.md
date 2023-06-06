# SpotDLWeb

SpotDLWeb est une interface graphique pour Spotdl et qui à l'aide de Python via Flask.
Il permet de récupérer les métadonnées à l'aide de Spotify puis de télécharger la musique via Youtube Music. La musique peut-être téléchargée directement sur un serveur connecté à Navidrone ou encore Jellyfin ou, télécharger la musique directement en local.

**docker-compose.yaml :**
```yaml
version: '3.3'
services:
  spotdlweb:
    image: gu1llaum3/spotdlweb:latest
    container_name: spotdlweb
    hostname: spotdlweb
    ports:
      - 3000:3000
    volumes:
      - ./path/to/musics:/app/downloads
    restart: unless-stopped
```
