import json
import logging
import os
import time

import boto3

queue_url = os.getenv("SQS_URL", "")
logger = logging.getLogger()

def sqs_listener():
    sqs = boto3.client("sqs")
    try:
        logger.info("Aguardando mensagem do sqs")
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20
        )
        if 'Messages' in response:
            logger.info(f"Resposta: {response}")
            message_receipt_handle = ''
            body = ''
            messages = response['Messages']
            for val in messages:
                body = val['Body']
                message_receipt_handle = val['ReceiptHandle']
                logger.info(f"Lendo do sqs: {body}")
                message = json.loads(body)
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message_receipt_handle
                )
        time.sleep(10)
    except Exception as e:
        logging.info('An error occurred while reading from sqs: %s' % str(e))
        time.sleep(10)
