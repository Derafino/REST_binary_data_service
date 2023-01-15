# REST_binary_data_service
This is a simple REST service written in Python using Flask that allows you to store binary data in a cloud storage AWS S3. The service supports PUT and GET operations for storing and retrieving data using a key-value system.
## Installing
1. Clone the repository
```
git clone https://github.com/Derafino/REST_binary_data_service
```
2. Create a virtual environment
```
python3 -m venv env
```
3. Activate the virtual environment
```
env\Scripts\activate
```
4. Install requirements
```
pip install -r requirements.txt
```
5. Set your credentials in the credentials.py
```
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'
bucket_name = 'your-bucket-name'
```
6. Run the service
```
flask run
```

The service will be running on http://127.0.0.1:5000.
