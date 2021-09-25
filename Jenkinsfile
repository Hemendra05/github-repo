#!/usr/bin/env groovy
// see https://jenkins.io/doc/book/pipeline/syntax/

pipeline {
    
    agent any
    
    parameters {
        booleanParam(name: "isNotAlreadyDeployed", defaultValue: true)
        string(name: "imageTag", defaultValue: "latest", description: "This tag is for creating the Docker Image.")
    }
    
    stages {

        stage("Build") {
            steps {
                sh "whoami"
                echo "good"
            }
        }
        
        stage("Publish") {
            steps {
                script {
                    if (params.isNotAlreadyDeployed) {
                        echo "App is not deployed yet, so its deploying now."
                    } else {
                        echo "this is running becoz app is deployed."
                    }
                }
            }
        }
    }
}
