🚀 CI/CD for Dockerized Python API on Google Cloud Run

This project demonstrates a complete CI/CD pipeline for a Dockerized Python Flask API integrated with a PostgreSQL database, using GitHub Actions for Continuous Integration (CI) and Google Cloud Run for Continuous Deployment (CD).

The pipeline validates the application in a production-like environment before deploying it to a scalable, serverless cloud platform.

📌 Project Overview

The goal of this project is to implement modern DevOps practices, including containerization, automated testing, and cloud-native deployment.
The application is tested using real integration tests and deployed as a serverless service on Google Cloud.

🛠️ Tech Stack

- Python (Flask)

- PostgreSQL

- Docker & Docker Compose

- GitHub Actions (CI)

- Google Cloud Run (CD)

- Google Artifact Registry

- Google Cloud Build

⚙️ CI/CD Workflow
✅ Continuous Integration (CI)

- Dockerized the Flask API using a Dockerfile

- Used Docker Compose to orchestrate:

- Python API container

- PostgreSQL container

- Implemented a GitHub Actions workflow that:

- Triggers on pushes and pull requests

- Builds the Docker image

- Starts the multi-container stack

- Runs integration tests against the /health endpoint

- Fails fast if the application does not start correctly

✅ Continuous Deployment (CD)

- Built production-ready container images

- Stored images in Google Artifact Registry

- Deployed the application to Google Cloud Run

- Configured dynamic port binding for Cloud Run compatibility

- Enabled automatic scaling and public HTTPS access

🔁 Execution Flow
Code Push →
GitHub Actions (CI) →
Docker Build →
Docker Compose (API + PostgreSQL) →
Integration Tests →
Artifact Registry →
Cloud Run Deployment →
Live HTTPS Service

✅ Outcome

-Automated build and test pipeline

- Verified application behavior before deployment

- Serverless deployment with zero infrastructure management

-Production-ready, cloud-native application lifecycle

🧠 Key Learnings

- Designing real CI pipelines using GitHub Actions

- Running integration tests with Docker Compose

- Container-based consistency across environments

- Cloud Run deployment best practices

- Clear separation between CI and CD

🙏 Acknowledgements

I would like to sincerely thank my mentor and organization for their guidance and continuous support throughout this project.
Their mentorship helped me understand practical DevOps workflows and cloud-native deployment strategies.

📎 Future Enhancements

- Add Cloud SQL (PostgreSQL) integration

- Implement automated GitHub Actions → Cloud Run CD

- Introduce Kubernetes (GKE) deployment

- Add monitoring and logging

✅ This project reflects real-world CI/CD practices used in modern cloud-native applications.
