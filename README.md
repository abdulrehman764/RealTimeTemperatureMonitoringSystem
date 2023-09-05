# RealTimeTemperatureMonitoringSystem
The primary objective of this project is to develop a system that can effectively monitor and analyze temperature data from various devices located in different geographical areas.

## Overview

This repository contains code files and Lambda functions for a temperature monitoring system. The system involves several components responsible for generating, processing, and alerting based on temperature data from IoT devices. Below is an overview of the main files in this repository:

### 1. Lambda to Generate Data (`Lambda-to-generate-data.py`)

This Python script is responsible for generating synthetic temperature data for IoT devices and sending it to an Amazon Kinesis Data Stream. Here's a brief description of the key functionalities:

- Imports necessary libraries such as `numpy`, `time`, `faker`, `pandas`, `boto3`, and more.
- Generates random device IDs and areas for the IoT devices.
- Defines functions to convert Unix timestamps to human-readable dates and generate random temperatures.
- Sends temperature data to an Amazon Kinesis Data Stream.
- Contains a `main()` function that initiates the data generation process.

#### Usage

This Lambda function is meant to run periodically to simulate data from IoT devices. You need to configure it with your AWS region and specific Kinesis Data Stream name.

### 2. KCL (Kinesis Client Library) Processor (`KCL.py`)

This Python script is designed to process data from an Amazon Kinesis Data Stream and take action based on the data. Key features of this script include:

- Imports required libraries, including the Amazon KCL library.
- Processes records from the Kinesis Data Stream.
- Implements logic to determine if a temperature exceeds a threshold and generates alerts.
- Performs periodic checkpoints to keep track of processed records.
- Handles lease losses and shard endings gracefully.

#### Usage

This script is designed to be run as a Kinesis Client Library application. It automatically reads data from the configured Kinesis Data Stream and processes it.

### 3. Lambda Data Stream to ElasticSearch (`Lambda-DataStream-to-ElasticSearch.py`)

This Python script is a Lambda function responsible for consuming records from a Kinesis Data Stream, decoding and transforming them, and then indexing them into an Amazon Elasticsearch index. Key features include:

- Uses the `requests` library to interact with the Elasticsearch endpoint.
- Decodes and processes records from the Kinesis Data Stream.
- Indexes records in an Elasticsearch index with appropriate document structure.

#### Usage

This Lambda function should be triggered by events from the Kinesis Data Stream. It indexes temperature data into an Elasticsearch index for further analysis.

### 4. Lambda SES Alarm Generator (`Lambda-SES-alarm-generator.py`)

This Python script defines a Lambda function that sends email alerts via Amazon SES (Simple Email Service). It's used to notify recipients when a temperature threshold is exceeded. Key features include:

- Imports the necessary AWS SDK library for SES.
- Sends email alerts with configurable subject and body.
- Provides error handling for email delivery failures.

#### Usage

This Lambda function can be invoked whenever an alarm condition is detected in the temperature data processing pipeline. It sends email alerts to the specified recipients.

## Prerequisites

Before using these Lambda functions and scripts, make sure you have the following prerequisites:

- AWS account with appropriate permissions and configurations.
- Amazon Kinesis Data Stream set up and configured.
- Amazon Elasticsearch cluster for data indexing (if using `Lambda-DataStream-to-ElasticSearch.py`).
- Amazon SES configured for sending email alerts (if using `Lambda-SES-alarm-generator.py`).

## Configuration

Each script or Lambda function may require specific configuration settings, such as AWS region, stream names, and email addresses. Be sure to review and configure the scripts according to your requirements.


**IOT Data Simulator:**
![image](https://github.com/abdulrehman764/RealTimeTemperatureMonitoringSystem/assets/108411380/9379c85e-604a-4f2e-8c9e-0d41fa5e2c2e)


**Architecture and Data Flow Diagram:**
![KinesisArchiteture-1](https://github.com/abdulrehman764/RealTimeTemperatureMonitoringSystem/assets/108411380/8193bf57-43ae-418c-9cba-1031267d0ee2)


**Open Search Dashboard:**
![image](https://github.com/abdulrehman764/RealTimeTemperatureMonitoringSystem/assets/108411380/60782c6f-62bb-47dc-a197-b901de5a9fc5)
