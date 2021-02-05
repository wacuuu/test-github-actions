FROM python:3.6-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY main.py /main.py
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
CMD ["/bin/docker-entrypoint.sh"]