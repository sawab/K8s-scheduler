node {
  env.APP_NAME = "scheduler-phoenix"
  env.IMAGE_BASE = "$DOCKER_REGISTRY/wwt/$APP_NAME"
  env.IMAGE = "$IMAGE_BASE:$BUILD_TIMESTAMP.$BUILD_ID"

  deleteDir()
  checkout scm

  stage('Build Docker Image') {
    sh './build.sh'
  }

  stage('Publish Docker Image') {
    if (env.BRANCH_NAME == 'master') {
      withCredentials([usernamePassword(credentialsId: 'artifactory_deployer',
          usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD $DOCKER_REGISTRY'

        // Publish build tag
        sh 'docker push $IMAGE'
        sh 'echo "Published: $IMAGE"'

        // Publish `snapshot` tag
        sh 'docker tag $IMAGE $IMAGE_BASE:latest'
        sh 'docker push $IMAGE_BASE:latest'
        sh 'echo "Published: $IMAGE_BASE:latest"'
      }
    } else {
      sh "echo 'Skipped. Not on master branch.'"
    }
  }

  always {
    deleteDir()
  }
}