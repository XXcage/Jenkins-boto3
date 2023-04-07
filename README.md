# Proj3

>**Jenkins:** 

<pre>sudo docker run -itd --name jenkins --restart=always \
-p 8080:8080 -p 50000:50000 \
-v "/home/bckp/Desktop/jenkins:/var/jenkins_home" \
-v "/var/run/docker.sock:/var/run/docker.sock" \
jenkins/jenkins:lts-jdk11  
</pre>

>**Sonarqube**
<pre>sudo docker run -d --name sonarqube --restart=always -p 9000:9000 -p 9092:9092 sonarqube</pre>

  `/var/jenkins_home` contains credentials for aws and dockerhub  
      `/.aws` folder for aws , with credentials and config files as per aws format  
      `/.dockerhub` folder for dockerhub, with dockerhub-credentials.properties file that contains username and password  

There are 2 processes:
** Main pipeline that can be run using shared library function with the following steps:   
* github checkout - consists of cleaning workspace, and cloning repo.   
* docker image build - consists of building image able to run a python code after linting it and posting to sonarqube.   
* docker image push - consists of logging in to dockerhub(after parsing the login details) and publishing image to dockerhub @ rzlinux0/proj3
```
@Library("proj3-sharedlib") _   
runBuildDockerfile()
```
or by SCM in jenkins using git and `Jenkinsfile`   
>Build a dockerfile, lint test the code and rate it using sonarqube and publish the image to dockerhub.
>while using aws config and credentials files, and using dockerhub-credentials file
* Second pipeline that can be run using shared library function:   
```
@Library("proj3-sharedlib") _   
runCronDockerfile()
```   
or by SCM in jenkins using git and `cronJenkinsfile`
>Pull and run a last successful image built by main pipeline.
