#!/usr/bin/env groovy
// see https://jenkins.io/doc/book/pipeline/syntax/

pipeline {
    
    agent any
    
    parameters {
        booleanParam(name: "RELEASE", defaultValue: false)
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
                    if (params.RELEASE) {
                        echo "${params.RELEASE}"
                    } else {
                        echo "${params.RELEASE}"
                    }
                }
            }
        }
    }
}
