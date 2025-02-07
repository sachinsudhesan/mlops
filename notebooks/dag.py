import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/sachinsudhesan/mlops.mlflow')
dagshub.init(repo_owner='sachinsudhesan', repo_name='mlops', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)