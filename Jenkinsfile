#!/usr/bin/env groovy
pipeline{
	agent any
	environment {
        PATH = "/home/testhadoop/.pyenv/shims:$PATH"
        runEnv = 'server'
    }
    stages {
        stage('Build') {
            steps{
                echo '='*50 + '开始构建' + '='*50
                echo '---> 更新依赖包'
                sh 'pipenv install --skip-lock'
                echo '---> 扫描用例信息'
                sh 'pipenv run python case_scanner.py'
                echo 'build success!'
             }
        }

    }
	post {
	    failure{
            script{
                emailext attachLog: true,
                body: '''${SCRIPT, template="groovy-html.template"}''',
                mimeType: 'text/html',
                charset:'UTF-8',
                subject: "${currentBuild.fullDisplayName} 构建失败",
                to: 'zaibin_mo@sui.com ou_gong@sui.com ying_zhou2@sui.com'
	        }
	    }
	}
}