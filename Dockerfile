FROM python:3
ADD aws_scraper.py /
ADD gcp_scraper.py /
ADD main.py /
ADD pymod /
ADD pymod/* /pymod/
#ADD phantomjs-2.1.1-windows/bin/ /

#https://gist.github.com/julionc/7476620

RUN apt-get update \
&& apt-get install build-essential chrpath libssl-dev libxft-dev \
&& apt-get install libfreetype6 libfreetype6-dev \
&& apt-get install libfontconfig1 libfontconfig1-dev \
&& cd ~ \
&& export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" \
&& wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \
&& tar xvjf $PHANTOM_JS.tar.bz2 \
&& ln -sf $PHANTOM_JS/bin/phantomjs /usr/local/bin

RUN pip install selenium
#RUN pip install boto3
RUN pip install google-api-python-client

CMD [ "python", "./main.py" ]
