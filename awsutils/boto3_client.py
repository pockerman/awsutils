import boto3


def get_aws_s3_client(region_name: str,
                      aws_access_key_id:str,
                      aws_secret_access_key: str):
    """Get the AWS S3 client on the specified region

    Parameters
    ----------
    aws_secret_access_key
    aws_access_key_id
    region_name

    Returns
    -------

    """
    return boto3.client('s3',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name)









