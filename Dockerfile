FROM python:3
ADD aws_scraper.py /
ADD pymod /
ADD pymod/* /pymod/
ADD phantomjs-2.1.1-windows/bin/ /

RUN pip install selenium
RUN pip install boto3

CMD [ "python", "./aws_scraper.py" ]