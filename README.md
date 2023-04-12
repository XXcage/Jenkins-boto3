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

>**Consul**
<pre>sudo docker run -d --name consul -p 8500:8500 -p 8600:8600/udp consul

There are 2 processes:   
   
<b>* First pipeline that can be run using shared library function with the following steps:   </b>
* github checkout - consists of cleaning workspace, and cloning repo.   
* docker image build - consists of building image able to run a python code after linting it and posting to sonarqube.   
* docker image push - consists of logging in to dockerhub(after retrieving login details from consul) and publishing image to dockerhub <i>@ rzlinux0/proj3</i>
```
@Library("proj3-sharedlib") _   
runBuildDockerfile()
```
or by SCM in jenkins using git and `Jenkinsfile`   
>Build a dockerfile, lint test the code and rate it using sonarqube and publish the image to dockerhub.
>after retrieving aws values and putting them into aws config and credentials files, and retrieving dockerhub credentials

<b>* Second pipeline that can be run using shared library function(and than runs on cron of 5 minutes) with the following steps:   </b>

* dockerhub login - consists of checking what is the latest successful image that was built, and logging in to dockerhub(creds from consul)
* dockerhub pull and run the image.
```
@Library("proj3-sharedlib") _   
runCronDockerfile()
```   
or by SCM in jenkins using git and `cronJenkinsfile`
>Pull and run a last successful image built by First pipeline.

consul-integration branch retrieves credentials from consul KV instead of files
main branch uses folders with files for authentication containing aws and dockerhub credentials.
