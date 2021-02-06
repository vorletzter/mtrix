FROM python:3

# set the default directory where CMD will execute
RUN mkdir -p /opt/services/app
WORKDIR /opt/services/app/

# install opus for mumblepy
RUN apt-get update
RUN apt-get install libopus0 opus-tools -y

# Copy the requierements into the container
# For now the Source lives inside an volume, after release we put it into the container
COPY ./app/* /opt/services/app/

#RUN pip install gunicorn --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt

# define the default command to run when starting the container
#CMD ["gunicorn", "--chdir", "phub", "--bind", ":8000", "phub.wsgi:application"]
# CMD ["gunicorn", "--bind", ":8000", "predigthub.wsgi:application", "--worker-tmp-dir", "/dev/shm"]
CMD ["python", "mtrix.py"]
