from python:3.11
COPY app /app
COPY run.sh /entrypoint.sh
COPY requirements.txt /requirements.txt
COPY instance /instance
COPY authelia-manager.py /authelia-manager.py
RUN pip install -r /requirements.txt && touch /.pip
EXPOSE 5000
ENTRYPOINT /entrypoint.sh
RUN chown -R 1000:1000 /instance