# mp4 to mp3 Converter - A Micro-Services Example

github: [micro-serv-des](https://github.com/AminMasoudi/micro-serv-des)

Welcome to the mp4 to mp3 converter, an example project showcasing micro-service system design concepts.

## What is Micro-Service Design?

Micro-service design is an architectural style that structures an application as a collection of small, independent services. Each service runs in its own process and communicates with lightweight protocols typically over HTTP.

[![Microservices Architecture](https://www.redhat.com/rhdc/managed-files/monolithic-vs-microservices.png)](https://www.redhat.com/en/topics/microservices/what-are-microservices)

In a micro-service architecture, each service is designed to be:

* **Independent**: Each service can be developed, tested, and deployed independently of other services.
* **Decentralized**: Services are not tightly coupled, allowing for greater flexibility and scalability.
* **Resilient**: If one service fails or becomes unavailable, others can continue to function normally.

## Overview

This project demonstrates how to design and implement a scalable, distributed system using multiple micro-services. The app converts MP4 files to MP3 audio files, utilizing various technologies such as Docker, Kubernetes, MySQL, MongoDB, RabbitMQ, and Flask.

## Features

* Convert MP4 videos to MP3 audio files
* Authenticates users with JWT tokens
* Saves video metadata in a MongoDB database
* Sends email notifications upon conversion completion
* Utilizes RabbitMQ as the message broker

## Architecture

The app consists of 6 micro-services:

1. **Gateway**: The main entry point, responsible for routing requests to the respective services.
2. **Auth**: Handles authentication and token validation using JWT.
3. **Converter**: Transforms MP4 videos into MP3 audio files.
4. **Notify**: Sends email notifications upon conversion completion.
5. **rabbitmq**: Handles queue for converter and notify service.

## Technologies

* Docker
* Kubernetes
* MySQL
* MongoDB
* RabbitMQ
* Flask

**TODO**

* [ ] Add Tests
* [ ] Implement the registration feature (planned for v0.2)
* [ ] Migrate the Gateway service to Django (planned for v0.3)
