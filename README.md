## AWS Intro Code Kata
---------------------

This kata is intended to familiarize you with three basic AWS services: S3, SQS, and RDS.

You will full-in the AWS interactions/functionality of two Python scripts: 

 * producer.py
 * consumer.py

The *producer.py* script should read all the .log files in an S3 bucket, locate exceptions within the file, and write basic information from each exception to an SQS queue. The information should be: timestamp, exception type, class/file.

The *consumer.py* script should read messages from the SQS queue, and then load them into an RDS database for analysis.

### Setup for OSX Users

 1. Install pip `sudo easy_install pip`
 2. Install Boto, the AWS SDK for Python: `sudo pip install boto`
 3. Download the files from https://github.com/cialowicz/AWS-Intro-Code-Kata
