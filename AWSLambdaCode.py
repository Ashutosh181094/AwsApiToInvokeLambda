import json

def lambda_handler(event, context):
  message="I love my {}".format(event['Country'])
  print(message)
  return message
