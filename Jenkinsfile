#!/usr/bin/env groovy
// see https://jenkins.io/doc/book/pipeline/syntax/

pipeline {
    
    agent any
    
    parameters {
        booleanParam(name: "DEPLOYED", defaultValue: false)
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
                    if (params.DEPLOYED) {
                        echo "this is running becoz app is deployed."
                        echo "${params.DEPLOYED}"
                    } else {
                        echo "App is not deployed yet, so its deploying now."
                        echo "${params.DEPLOYED}"
                    }
                }
            }
        }
    }
}
