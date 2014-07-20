import sys, os
import json
from boto.s3.connection import S3Connection
from boto.sqs.message import Message
import boto.sqs

# AWS Keys
AWS_key    = ''
AWS_secret = ''

# AWS Variables
bucketName = 'aws-intro-code-kata'
queueName  = 'aws-intro-code-kata'
region     = 'us-west-1'

# Persistent Connections
sqsConn = boto.sqs.connect_to_region(region, aws_access_key_id=AWS_key, aws_secret_access_key=AWS_secret)

def processBucketLogFiles():
	s3conn = S3Connection(AWS_key, AWS_secret)
	bucket = s3conn.get_bucket(bucketName)
	for key in bucket.list():
		extension = os.path.splitext(key.name)[1]
		if(extension == ".log"):
			print "Processing " + key.name
			logContent = key.get_contents_as_string()
			processLogContent(key.name, logContent)

def sendMessageToQueue(sqsMessage):
	queue = sqsConn.get_queue(queueName)
	queue.write(sqsMessage)

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
