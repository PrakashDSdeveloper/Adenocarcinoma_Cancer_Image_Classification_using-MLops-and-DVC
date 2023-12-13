
# Chest Cancer Classification using MLflow and DVC

## Workflows

### 1. Update Configuration Files

- **config.yaml**: Update the configuration file as needed.
- **params.yaml**: Update parameters for the model.
- **entity**: Update relevant information about the project entity.
- **src config**: Update the configuration manager in the source code.
- **components**: Update various components of the project.
- **pipeline**: Update the project pipeline.
- **main.py**: Update the main script file.
- **dvc.yaml**: Update DVC configuration.

### 2. MLflow

#### Documentation

- Access the MLflow tutorial for more details.
- Run `mlflow ui` to start the MLflow user interface.

#### Environment Variables

Run the following commands to export MLflow variables as environment variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/PrakashDSdeveloper/Adenocarcinoma_Cancer_Image_Classification_using-MLops-and-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=PrakashDSdeveloper

export MLFLOW_TRACKING_PASSWORD=1f317b3d56a9ba90f61b3e3af3424f4895a8139f
```


### 3. DVC

- Run `dvc init` to initialize DVC.
- Run `dvc repro` to reproduce the project.
- Run `dvc dag` to visualize the DVC pipeline.

## MLflow & DVC Overview

### MLflow

- Production-grade.
- Trace and log all experiments.
- Logging and tagging for models.

### DVC

- Lightweight for Proof of Concept (POC) and experiments tracking.
- Lightweight experiment tracker.
- Can perform orchestration (creating pipelines).

## AWS CI/CD Deployment with GitHub Actions

1. **Login to AWS Console:**
   - Create an IAM user for deployment with specific access (EC2 and ECR).

2. **Build and Push Docker Image:**
   - Build the Docker image of the source code.
   - Push the Docker image to Elastic Container Registry (ECR).

3. **Launch EC2 Instance:**
   - Create an EC2 instance (virtual machine).

4. **Install Docker on EC2:**
   - Update and upgrade packages (optional).
   - Install Docker on the EC2 machine.

5. **Configure EC2 as Self-Hosted Runner:**
   - Configure the EC2 instance as a self-hosted GitHub Actions runner.

6. **Setup GitHub Secrets:**
   - Add GitHub secrets for AWS access keys and region.

7. **AWS Policy:**
   - Grant necessary AWS policies (AmazonEC2ContainerRegistryFullAccess, AmazonEC2FullAccess).

8. **Create ECR Repository:**
   - Create an ECR repository to store the Docker image.

9. **ECR URI:**
   - Save the ECR URI for reference: `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`.

10. **Launch EC2 and Deploy:**
    - Launch the EC2 instance.
    - Pull the Docker image from ECR on EC2.
    - Launch the Docker image on EC2.

## Optional Docker Installation on EC2

```bash
# Optional: Update and upgrade packages
sudo apt-get update -y
sudo apt-get upgrade

# Required: Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
