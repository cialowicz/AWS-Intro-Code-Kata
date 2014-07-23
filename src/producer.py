import sys, os
import json
from boto.s3.connection import S3Connection
from boto.sqs.message import Message
import boto.sqs

# Should read all the .log files in an S3 bucket,
# parse each log file to locate code exceptions,
# and then write basic exception information to an SQS queue.

# AWS Keys
AWS_key    = ''
AWS_secret = ''

# AWS Variables
bucketName = 'aws-intro-code-kata'
queueName  = '' # @todo choose a unique queue name
region     = 'us-west-1'

def processBucketLogFiles():
	# @todo: write your code here!
	# get log files from S3 bucket, and pass contents to processLogContent()

def sendMessageToQueue(sqsMessage):
	# @todo: write your code here!
	# send message to SQS

# Processes log file content
def processLogContent(filename, logContent):
	for line in logContent.split('\n'):
		# line should start with a timestamp: 2014
		if not line.startswith("20"):
			continue
		# line should have an exception in it
		if "Exception" not in line:
			continue
		
		parsedLine = line.split(" ")
		
		exceptionDate    = parsedLine[0]
		exceptionTime    = parsedLine[1].split(",")[0] # no milliseconds
		exceptionType    = parsedLine[2]
		exceptionTask    = parsedLine[3].strip("[]")
		exceptionClass   = parsedLine[4].strip("[]")
		exceptionMessage = " ".join(parsedLine[5::])

		message = {"file": filename,
		           "date": exceptionDate,
		           "time": exceptionTime,
		           "type": exceptionType,
		           "task": exceptionTask,
		           "class": exceptionClass,
		           "message": exceptionMessage}
		
		sqsMessage = Message()
		sqsMessage.set_body(json.dumps(message))
		sendMessageToQueue(sqsMessage)

if __name__ == "__main__":
	processBucketLogFiles()
