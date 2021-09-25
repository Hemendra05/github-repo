#!/usr/bin/env groovy
// see https://jenkins.io/doc/book/pipeline/syntax/

pipeline {
    
    agent any
    
    parameters {
        booleanParam(name: "RELEASE", defaultValue: true)
    }
    
    stages {

        stage("Build") {
            steps {
                sh "hostname"
            }
        }
        
        stage("Publish") {
            steps {
                script {
                    if (params.RELEASE) {
                        echo "${params.RELEASE}"
                    } else {
                        echo "nothing happen"
                    }
                }
            }
        }
    }
}
