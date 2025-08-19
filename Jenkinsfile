node {
    String containerTag = 'myapp-hivebox'

    stage('Build') {
        checkout scm
        linting()
        sh "docker build -t ${containerTag} ."
    }
    stage('Test') {
        sh "docker run --rm ${containerTag} pytest"
    }
    stage('Deploy') {
        withCredentials([
            usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')
            ]) {
            sh "echo ${PASS} | docker login --username ${USER} --password-stdin"
            sh "docker tag ${containerTag} ${USER}/my-repo:1.0.0"
            }
    }
}

void linting() {
    sh 'ruff format'
    sh 'ruff check --fix'
    sh 'docker run --rm -i hadolint/hadolint < Dockerfile'
}
