import sys, os
import json
from boto.sqs.message import Message
import boto.sqs
import pymysql

# Reads exception messages from an SQS queue (messages placed there by producer.py),
# and inserts them into a MySQL database (hopefully RDS if you're doing the full AWS kata)

# AWS Keys
AWS_key    = ''
AWS_secret = ''

# AWS Variables
queueName  = ''
region     = ''
dbHost     = ''
dbUser     = ''
dbPass     = ''
dbName     = ''

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
	if writeExceptionToDB(params):
		queue.delete_message(sqsMessage)

def writeExceptionToDB(params):
	try:
		cursor.execute("""INSERT INTO errors (date, time, type, task, class, message) VALUES (%s, %s, %s, %s, %s, %s)""",
			(params["date"], params["time"], params["type"], params["task"], params["class"], params["message"]))
		dbConn.commit()
		return True
	except:
		dbConn.rollback()
		return False

if __name__ == "__main__":
	processQueueMessages()
	dbConn.close()
