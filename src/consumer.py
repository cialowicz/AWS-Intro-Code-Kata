import sys, os
import json
from boto.sqs.message import Message
import boto.sqs
import pymysql

# AWS Keys
AWS_key    = ''
AWS_secret = ''

# AWS Variables
queueName  = '' # @todo: use the same unique queue name as in producer.py
region     = 'us-west-1'
dbHost     = ''
dbUser     = ''
dbPass     = ''
dbName     = 'exceptions'

# Persistent Connections
dbConn = pymysql.connect(host=dbHost, port=3306, user=dbUser, passwd=dbPass, db=dbName)
cursor = dbConn.cursor()

def processQueueMessages():
	# @todo: write your code here!
	# take each SQS queue message, and pass it to processSqsMessage()
	# protip: SQS messages have a visibility timeout (read about this), and must be deleted manually even after being read

def processSqsMessage(sqsMessage, queue):
	params = json.loads(sqsMessage.get_body())
	writeExceptionToDB(params)
	# protip: delete your sqsMessage here from queue, AFTER it has been inserted into the DB, to ensure delivery

def writeExceptionToDB(params):
	# @todo: write your code here!
	# take the params, and insert them into the RDS MySQL DB exceptions table (see schema.sql)

if __name__ == "__main__":
	processQueueMessages()
	dbConn.close()
