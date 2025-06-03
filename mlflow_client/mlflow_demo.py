import mlflow

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("Demo-Experiment")

with mlflow.start_run():
    mlflow.log_param("alpha", 0.5)
    mlflow.log_param("l1_ratio", 0.1)
    mlflow.log_metric("rmse", 0.78)
    print("Experiment logged to MLflow!")

