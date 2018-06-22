import sys
import boto3
import boto
import boto.s3.connection
import time

def connect_s3()
  global connection
  global bucket
  try:
    start = time.time()
    connection = boto.connect_s3(aws_access_key_id='xyz', aws_secret_access_key = 'secret_access_key')
    bucket = connection.get_bucket(s3_bucket_name)
    end = time.time()
    print("connected to AWS S3 in: "+str(end - start)+" seconds")
  except Exception as e:
    print('[AWS ERROR] - unable to connect to S3')
    print(e)
    sys.exit(1)
    
connect_s3()


    
    
    
