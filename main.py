from flask import Flask, request, Response
import boto3

from credentials import aws_access_key_id, aws_secret_access_key, bucket_name

app = Flask(__name__)

s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)


@app.route("/", methods=['PUT'])
def put_data():
    keys = ''
    for file_key in request.files:
        key = request.files[file_key].filename
        file = request.files[file_key]
        s3.put_object(Bucket=bucket_name, Key=key, Body=file)
        keys += f'{key}\n'
    return 'Saved data:\n' + keys


@app.route("/<key>", methods=['GET'])
def get_data(key):
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    data = obj['Body'].read()
    response = Response(data, content_type='application/octet-stream')
    return response


if __name__ == "__main__":
    app.run()
