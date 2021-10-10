# app-engine-python-cronjob
create a cronjob in app engine using python flask

1. THIS IS A CRON JOB WHICH SENDS EMAIL EVERY 5 minutes 
2. pts to be taken care 
      1. remember the app.ymml "app" also points to the app in flask application.
      2. the cron always run the job using an URL and thus we have used "/reminder" and thus the /reminder in flask appln is going to be run 
      3. the http response after the cron runs the job accessed by the URL is between 200-299 if it is successsful
      4. Cron does not automativally retry the job if it fails.

3. the app can be deployed using gcloudsdk command
      1. gcloud app deploy cron.yaml

4. If you just wnat to deploy a flask applicaton refer this medium article
https://medium.com/@dmahugh_70618/deploying-a-flask-app-to-google-app-engine-faa883b5ffab
