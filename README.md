## AWS Intro Code Kata
---------------------

This kata is intended to familiarize you with three basic AWS services: S3, SQS, and RDS.

You will full-in the AWS interactions/functionality of two Python scripts: 

 * producer.py
 * consumer.py

The *producer.py* script should read all the .log files in an S3 bucket, locate exceptions within the file, and write basic information from each exception to an SQS queue. The information should be: timestamp, exception type, class/file.

The *consumer.py* script should read messages from the SQS queue, and then load them into an RDS database for analysis.

### AWS Setup

Take note of the region you're in when following the steps below.

 1. Manually create an S3 bucket, and upload the log files in `/resources` to it.
 2. Create an RDS database, and modify a member security group so that it's accessible from your IP address.
 3. Create an SQS queue

### Setup for OSX Users

 1. Install pip `sudo easy_install pip`
 2. Install Boto, the AWS SDK for Python: `sudo pip install boto`
 3. Install MySQL for Python: `sudo pip install PyMySQL`
 4. Download the files from https://github.com/cialowicz/AWS-Intro-Code-Kata

