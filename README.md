# micro-serv-des
## mp4 to mp3 converter
an example project to practice and show-off some knowledge from micro-service system design \
this app converts mp4 files to mp3\
how?? let me explain\

first, lets have look to how to work with:\

as the first step you have to register.forgot to impliment that part in this version[maybe next version]\
so you request for login\
a jwt token will return if you send the right credentials\
then you send the video and the token\
the app will validates the token ,save the video and say "we call you when its ready" to you\
at the end when the video converted to mp3 the app will send you an email and give you an id to download the video

second, lets have a look at how the app works:\
  the app composed from 5 micro services and rabbitmq as our message broker.\
  it uses nginx-ingress as load balancer\
  we write a service with flask for auth service/
    connects to mysql database. it checks the password and validate tokens.
  then another service as gateway with its the main part of the programm[also uses flask for now].\
  the another two are two consumer service that connects to rabbitmq and each on listen to one channel.
  - the converter waits until a new video upload and convert it to mp3. then save it in mongo db and place a message to audio channel.
  - the notify service listening to audio channel. when a new audio found send an email to user and notifs him.

this app uses 
- jwt authentication
- Docker
- kubernetes
- mysql
- mongodb
- rabbitmq
- flask

services:
1. gateway
3. rabbitmq
4. auth
5. converter
6. notify

## TODO:
- [ ] write curl script helper
- [ ] and thats v0.1
- [ ] change gateway to django 
