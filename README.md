# Forwarder Backend 

Activate the virtual env:
```
conda activate <nameofvenv>
```

For deploying:

```
sam build && sam deploy
```

For testing locally:

```
# Export path for test to find the source code ....
export PYTHONPATH='/Users/prameshbajracharya/lecodage/personalworks/ipolisting'

# Export env vars that lambda will use
export emails_to_send='yccgpzaixr@scpulse.com,gthbpahyukbtns@knowledgemd.com,vyorwfydebrn@knowledgemd.com'

# Call function
python tests/listing.py
```

For testing when live:

> Remember that the function uses `envvars`. So, do check if they are configured on lambda's side before doing anything.

The lambda function will have a function URL that can be called. Use that function url to make any request.

For example:

POST: https://pdzzplykb4o36pyfx7um2o7rpu0qpwwt.lambda-url.ap-south-1.on.aws/
Request Body (JSON):
```
{
    "sender_address": "TxSMS",
    "message": "Hey there, code is XXXXXXX",
    "receiver_address": "+97798XXXXXXXX"
}
```
