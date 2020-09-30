
Python Client for Cloud AutoML API
==================================


The `Cloud AutoML API`_ is a suite of machine learning products that enables
developers with limited machine learning expertise to train high-quality models
specific to their business needs, by leveraging Google’s state-of-the-art
transfer learning, and Neural Architecture Search technology.

- Client Library Documentation: https://googleapis.dev/python/automl/latest
- Product Documentation:  https://cloud.google.com/automl



Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. Select or create a Cloud Platform project.: https://console.cloud.google.com/project
2. Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/
3. Enable the Cloud AutoML API.: https://cloud.google.com/automl
4. Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html



Installation
-----------
1. Provide authentication credentials to your application code by setting the environment variable `GOOGLE_APPLICATION_CREDENTIALS`
   - example: `export GOOGLE_APPLICATION_CREDENTIALS="[KEY PATH]"` 
2. `make dockerenv`
3. `make create-model` or `GOOGLE_APPLICATION_CREDENTIALS=$HOME/devkey/cadillacvehiclerecognition-poc-1f93eb0150ad.json make create-model`


Note
-----------
Source originated from: https://github.com/googleapis/python-automl
