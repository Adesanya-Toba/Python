import boto3


class MyS3Client:
    def __init__(self, region_name="us-east-1"):
        self.s3_client = boto3.client("s3", region_name=region_name)

    def list_buckets(self):
        """Returns a list of bucket names."""
        response = self.s3_client.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]  # type: ignore

    def list_objects(self, bucket_name, prefix):
        """Returns a list all objects with specified prefix."""
        response = self.s3_client.list_objects(
            Bucket=bucket_name,
            Prefix=prefix,
        )
        return [object["Key"] for object in response["Contents"]]  # type: ignore
