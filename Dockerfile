FROM python:3.8
WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev  libxtst-dev tk-dev 
RUN pip install -r requirements.txt 


CMD ["python","app.py"]