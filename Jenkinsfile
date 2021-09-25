#!/usr/bin/env groovy
// see https://jenkins.io/doc/book/pipeline/syntax/

pipeline {
    
    agent any
    
    parameters {
        booleanParam(name: "NOT_DEPLOYED", defaultValue: false)
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
                    if (params.NOT_DEPLOYED) {
                        echo "App is not deployed yet, so its deploying now."
                        echo "${params.NOT_DEPLOYED}"
                    } else {
                        echo "this is running becoz app is deployed."
                        echo "${params.NOT_DEPLOYED}"
                    }
                }
            }
        }
    }
}
