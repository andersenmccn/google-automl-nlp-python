FROM google/cloud-sdk:slim

RUN pip3 install --upgrade pip
RUN pip install google-cloud-automl

ENV GOOGLE_APPLICATION_CREDENTIALS=/key/credentials.json
