pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'your-dockerhub-username'
        ORDER_IMAGE    = "${DOCKERHUB_USER}/order-api"
        INV_IMAGE      = "${DOCKERHUB_USER}/inventory-service"
    }

    stages {

        stage('Stage 1 — Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/GurjyotSingh740-gk/autoscale-shop.git'
            }
        }

        stage('Stage 2 — Build Docker Images') {
            steps {
                bat 'docker build -t %ORDER_IMAGE%:latest ./order-api'
                bat 'docker build -t %INV_IMAGE%:latest ./inventory-service'
            }
        }

        stage('Stage 3 — Test') {
            steps {
                bat 'docker run --rm %ORDER_IMAGE%:latest python -c "from app import app; print(app)"'
                bat 'docker run --rm %INV_IMAGE%:latest python -c "from app import app; print(app)"'
            }
        }

        stage('Stage 4 — Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat 'docker push %ORDER_IMAGE%:latest'
                    bat 'docker push %INV_IMAGE%:latest'
                }
            }
        }

        stage('Stage 5 — Update K8s Manifest') {
            steps {
                bat '''
                    powershell -Command "(Get-Content k8s/order-api-deployment.yaml) -replace 'image: .*order-api.*', 'image: %ORDER_IMAGE%:latest' | Set-Content k8s/order-api-deployment.yaml"
                    git config user.email "jenkins@autoscaleshop.com"
                    git config user.name "Jenkins Bot"
                    git add k8s/order-api-deployment.yaml
                    git commit -m "ci: Jenkins updated image tag to latest"
                    git push origin main
                '''
            }
        }
    }

    post {
        success { echo '✅ Pipeline completed successfully!' }
        failure { echo '❌ Pipeline failed. Check logs.' }
    }
}