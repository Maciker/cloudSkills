import sys
import boto3

try:
    def main():
        create_s3bucket(bucketName)

except Exception as e:
    print(e)


def create_s3bucket(bucketName):
    s3_bucket = boto3.client(
        's3',
    )

    bucket = s3_bucket.create_bucket(
        Bucket=bucketName,
        ACL='private',
    )

    print(bucket)

bucketName = sys.argv[1]

if __name__ == '__main__':
    main()
