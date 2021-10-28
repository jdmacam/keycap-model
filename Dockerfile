FROM tensorflow/tensorflow
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
CMD jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
