import sys
import boto3
import boto
import boto.s3.connection
from boto.s3.key import Key
import time

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
    
#iterate through a given ARN in bucket    
for key in bucket.list(prefix='path/to/s3/location/', delimiter = '/'):
  array.append(key.name)

array.pop(0)  #get rid of the ARN
print(array)  #prints filenames
print(len(array))  #print number of files in ARN

#another way to list bucket contents
for key in bucket.list():
  print("{name}\t{size}\t{modified}")
  print(key.name +"\t"+ str(key.size) +"\t"+ str(key.last_modified))
  
#read file & count number of times a word occurs
for key in bucket.list('path/to/s3/location/'):
  file_contents = str(key.get_contents_as_string())
  sum += (file_contents.count('searchWord'))
print(sum)

#get file from S3 bucket
destFileName = "s3File"
k = Key(bucket,"path/to/file/filename")
k.get_contents_to_filename(destFileName)

#put file into S3 bucket
file = open("file_name")
k = Key(bucket)
k.key = "path/on/s3/to/upload"
result = k.set_contents_from_file(file)
#use this if folder is AES encrypted - k.set_contents_from_file(file, {"x-amz-server-side-encryption": "AES256"}, True)

