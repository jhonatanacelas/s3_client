import boto3

def list_buckets_by_profile(profile_name):
    """
    List all the buckets owned by a specific profile.
    """
    import boto3
    session = boto3.Session(profile_name=profile_name)
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def list_bucket_items(bucket_name):
    """
    List all the items in a bucket.
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    for item in bucket.objects.all():
        print(item.key)


def download_file(bucket_name, key, local_path):
    """
    Download a file from S3.
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.download_file(key, local_path)


list_bucket_items('bucket-name')

download_file('bucket-name', 'path/to/file', 'local/path/to/file')

