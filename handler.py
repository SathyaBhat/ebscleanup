import json
from ebs_cleanup.cleanup import clean_up

def run(event, context):
    response = clean_up()
    return response