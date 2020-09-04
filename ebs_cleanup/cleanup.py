import boto3
import botocore.exceptions


def clean_up():
    client = boto3.client('ec2')
    # status == available are the EBS volumes that are not attached to any instance
    volumes = client.describe_volumes(
        Filters=[
            {
                'Name':'status',
                'Values':['available']
            }
        ]
    )
    deleted_volumes = []
    for v in volumes['Volumes']:
        try:
            response = client.delete_volume(VolumeId=v.get('VolumeId'), DryRun=False)
            deleted_volumes.append(v.get('VolumeId'))
        except botocore.exceptions.ClientError as error:
            response = {}
            response['status'] = 500
            response['description'] = error.response
            return response
    
    return {'status':'200', 'description':f"Volumes {','.join(deleted_volumes)} deleted successfully."}