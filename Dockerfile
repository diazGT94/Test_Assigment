FROM python:3.6

# Update aptitude with new repo
RUN apt-get update

# Install software 
RUN apt-get install -y git

RUN git clone https://github.com/diazGT94/Test_Assigment.git

WORKDIR "/Test_Assigment"

RUN chmod +x entrypoint.sh

CMD entrypoint.sh