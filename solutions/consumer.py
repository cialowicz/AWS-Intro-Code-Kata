import sys, os
import json
from boto.sqs.message import Message
import boto.sqs
import pymysql

# AWS Keys
AWS_key    = ''
AWS_secret = ''

# AWS Variables
queueName  = 'aws-intro-code-kata'
region     = 'us-west-1'
dbHost     = ''
dbUser     = ''
dbPass     = ''
dbName     = 'exceptions'

# Persistent Connections
sqsConn = boto.sqs.connect_to_region(region, aws_access_key_id=AWS_key, aws_secret_access_key=AWS_secret)
dbConn = pymysql.connect(host=dbHost, port=3306, user=dbUser, passwd=dbPass, db=dbName)
cursor = dbConn.cursor()

def processQueueMessages():
	queue = sqsConn.get_queue(queueName)
	messages = queue.get_messages(10)
	while len(messages) > 0:
		[processSqsMessage(message, queue) for message in messages]
		messages = queue.get_messages(10)

def processSqsMessage(sqsMessage, queue):
	params = json.loads(sqsMessage.get_body())
	writeExceptionToDB(params)
	queue.delete_message(sqsMessage)

def writeExceptionToDB(params):
	try:
		cursor.execute("""INSERT INTO exceptions (date, time, type, task, class, message) VALUES (%s, %s, %s, %s, %s, %s)""",
			(params["date"], params["time"], params["type"], params["task"], params["class"], params["message"]))
		dbConn.commit()
	except:
		dbConn.rollback()

if __name__ == "__main__":
	processQueueMessages()
	dbConn.close()
