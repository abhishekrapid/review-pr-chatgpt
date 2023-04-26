# write a s3 bucket configuration
import boto3
import openai
import os
import pandas

# write a s3 bucket configuration code
s3 = boto3.client("s3")


# write a function create a bucket
def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    return bucket_name


# write a function upload a file
def upload_file(bucket_name, file_name):
    s3.upload_file(file_name, bucket_name, file_name)
    return file_name


# write a function to list all the buckets
def list_buckets():
    response = s3.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    print("Bucket List: %s" % buckets)
    return buckets


# write a function to delete a bucket
def delete_bucket(bucket_name):
    s3.delete_bucket(Bucket=bucket_name)
    return bucket_name


# write a function to delete a file
def delete_file(bucket_name, file_name):
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    return file_name


# write a function to list all the files
def list_files(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    print(response)
    for content in response["Contents"]:
        print(content["Key"])
        return content["Key"]

    return response


# write a function to download a file
def download_file(bucket_name, file_name):
    s3.download_file(bucket_name, file_name, file_name)
    return file_name


# write a function to copy a file
def copy_file(bucket_name, file_name):
    s3.copy_object(Bucket=bucket_name, Key=file_name, CopySource=bucket_name + "/" + file_name)
    return file_name





