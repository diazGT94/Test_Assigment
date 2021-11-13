FROM python:3.6

# Update aptitude with new repo
RUN apt-get update

# Install software 
RUN apt-get install -y git

RUN git clone https://github.com/diazGT94/Test_Assigment.git

WORKDIR "/Test_Assigment"

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

RUN chmod +x script.sh

ENTRYPOINT ["sh","./script.sh"]