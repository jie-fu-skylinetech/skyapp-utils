FROM python:3
ADD aws_scraper.py /
ADD gcp_scraper.py /
ADD main.py /
ADD pymod /
ADD pymod/* /pymod/
#ADD phantomjs-2.1.1-windows/bin/ /

#https://gist.github.com/julionc/7476620

#RUN apt-get update 
#RUN sudo apt-get install build-essential chrpath libssl-dev libxft-dev 
#RUN sudo apt-get install libfreetype6 libfreetype6-dev 
#RUN sudo apt-get install libfontconfig1 libfontconfig1-dev 
#RUN cd ~ 
ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" 
#RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 
#RUN tar xvjf $PHANTOM_JS.tar.bz2 
ADD $PHANTOM_JS /
RUN ln -sf /$PHANTOM_JS/bin/phantomjs /usr/local/bin
ENV PATH="/$PHANTOM_JS/bin/:${PATH}"

RUN pip install selenium
#RUN pip install boto3
RUN pip install google-cloud
RUN pip install requests

CMD [ "python", "./main.py" ]
