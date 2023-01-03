FROM alpine:latest

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# Update packages
RUN apk update

# Install python3 et pip
RUN apk add python3 py3-pip

# install dependencies
RUN pip install -r requirements.txt

# install ffmpeg for SpotDL
RUN spotdl --download-ffmpeg

# install zip
RUN apk update && apk add zip

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./app.py" ]
