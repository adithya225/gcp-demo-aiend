# Build and deploy

Command to build the application. PLease remeber to change the project name and application name
```
gcloud builds submit --tag gcr.io/gcp-demo-aiend/testdemo  --project=gcp-demo-aiend
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/gcp-demo-aiend/testdemo --platform managed  --project=gcp-demo-aiend --allow-unauthenticated
```
