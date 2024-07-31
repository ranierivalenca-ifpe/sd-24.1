### 1. **Amazon S3 (Simple Storage Service)**

**Description:** Object storage service that offers scalability, data availability, security, and performance.

**Free Tier:** 5 GB of standard storage, 20,000 GET requests, and 2,000 PUT requests per month.

**Pricing Units:** Per GB and per request.

**Previous Knowledge Required:** Basic understanding of cloud storage concepts.

**Demonstration Suggestions:**
- Create an S3 bucket and upload files.
- Set permissions and demonstrate accessing files via a public URL.
- Implement versioning on an S3 bucket and demonstrate how to recover a previous version of a file.
- Set up lifecycle policies to automatically move objects between storage classes.

**Cost Scenarios:**
1. An app stores 1000 user profile images, each 1 MB, and expects 5000 GET requests per day. Calculate costs after 3 months of operation.
2. A backup solution uploads daily backups of 10 GB to S3. Calculate costs after 6 months, considering storage and retrieval costs.
3. A web application hosts static content (HTML, CSS, JS) in S3, serving 1 GB of content daily with 100,000 GET requests. Calculate costs after 1 month, including storage, requests, and data transfer.

----

### 2. **Amazon SNS (Simple Notification Service)**

**Description:** Fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

**Free Tier:** 1 million publishes, 1 million notifications, and 100,000 HTTP/S deliveries.

**Pricing Units:** Per publish, per notification, and per delivery.

**Previous Knowledge Required:** Basic understanding of messaging services.

**Demonstration Suggestions:**
- Create a topic, subscribe to it, and send notifications.
- Demonstrate integration with Lambda to send automated alerts.
- Set up SMS notifications for a specific event.
- Implement an email notification system using SES and SNS.

**Cost Scenarios:**
1. An app sends notifications to 100,000 users about daily updates. Calculate costs after 2 months, considering publish and notification costs.
2. An IoT application sends sensor data updates every minute, totaling 500,000 publishes per day. Calculate costs after 1 month, including data transfer costs.
3. A notification service sends promotional emails to 200,000 subscribers once a week. Calculate costs after 3 months, considering email delivery costs.

----

### 3. **Amazon SES (Simple Email Service)**

**Description:** Cloud-based email sending service for marketing, notification, and transactional emails.

**Free Tier:** 62,000 emails per month when sent from an Amazon EC2 instance, 1,000 emails per month otherwise.

**Pricing Units:** Per email sent.

**Previous Knowledge Required:** Basic understanding of email services.

**Demonstration Suggestions:**
- Set up an email domain and verify email addresses.
- Send a test email using the SES console or SDK.
- Implement email bounce and complaint handling.
- Create a template-based email sending service.

**Cost Scenarios:**
1. An app sends welcome emails to 1,000 new users monthly, growing 20% each month. It also sends password recovery emails to 40% of users monthly. Calculate costs after 6 months.
2. A marketing campaign sends newsletters to 50,000 users every month. Calculate costs after 3 months, considering both free and paid emails.
3. A notification system sends order confirmation emails for 500 daily transactions. Calculate costs after 2 months, including any overage charges.

----

### 4. **Amazon Rekognition**

**Description:** Adds image and video analysis to your applications using deep learning technology.

**Free Tier:** 5,000 images per month for detecting labels.

**Pricing Units:** Per image.

**Previous Knowledge Required:** Basic understanding of image processing concepts.

**Demonstration Suggestions:**
- Upload images and use Rekognition to detect objects and scenes.
- Demonstrate face detection and analysis.
- Implement a custom label detection model.
- Analyze video for facial recognition and object detection.

**Cost Scenarios:**
1. A security system analyzes 1,000 images per day for face recognition. Calculate costs after 3 months, including video analysis.
2. An e-commerce site scans 10,000 product images monthly to identify inappropriate content. Calculate costs after 4 months, considering both free and paid analysis.
3. A social media platform tags objects in 50,000 images uploaded monthly. Calculate costs after 2 months, including storage and retrieval costs.

----

### 5. **Amazon Translate**

**Description:** Neural machine translation service for fast and high-quality language translation.

**Free Tier:** 2 million characters per month for the first 12 months.

**Pricing Units:** Per million characters.

**Previous Knowledge Required:** Basic understanding of language translation.

**Demonstration Suggestions:**
- Translate text between different languages using the console.
- Integrate translation into a web application.
- Translate a document and save the translated text to an S3 bucket.
- Create a multilingual chatbot using Amazon Translate.

**Cost Scenarios:**
1. A global news site translates 1 million characters daily. Calculate costs after 2 months, including both free and paid characters.
2. An international e-commerce platform translates product descriptions totaling 500,000 characters monthly. Calculate costs after 3 months, considering storage and retrieval.
3. A customer support system translates 2 million characters of chat transcripts monthly. Calculate costs after 6 months, including data transfer costs.

----

### 6. **Amazon Comprehend**

**Description:** Natural language processing (NLP) service that finds insights and relationships in text.

**Free Tier:** 50,000 units of text (up to 100 characters each) per month.

**Pricing Units:** Per unit of text.

**Previous Knowledge Required:** Basic understanding of natural language processing.

**Demonstration Suggestions:**
- Analyze text to extract key phrases, entities, sentiment, and language.
- Demonstrate topic modeling and document classification.
- Implement real-time sentiment analysis for social media feeds.
- Create a chatbot with sentiment analysis using Comprehend.

**Cost Scenarios:**
1. A customer feedback system analyzes 200,000 text units monthly. Calculate costs after 3 months, including both free and paid units.
2. A news aggregation site processes 1 million text units to extract key phrases monthly. Calculate costs after 2 months, considering storage and retrieval.
3. A sentiment analysis tool processes 500,000 text units from social media posts monthly. Calculate costs after 4 months, including data transfer costs.

----

### 7. **Amazon Polly**

**Description:** Turns text into lifelike speech, allowing you to create applications that talk.

**Free Tier:** 5 million characters per month for the first 12 months.

**Pricing Units:** Per million characters.

**Previous Knowledge Required:** Basic understanding of text-to-speech technology.

**Demonstration Suggestions:**
- Convert text to speech and play back the audio.
- Integrate speech synthesis into an application.
- Create a multilingual application using Polly's different language voices.
- Implement a real-time speech synthesis service.

**Cost Scenarios:**
1. An audiobook platform converts 20 million characters monthly. Calculate costs after 3 months, including both free and paid characters.
2. An e-learning platform converts 5 million characters monthly into speech for interactive courses. Calculate costs after 6 months, considering storage and retrieval.
3. A news app converts 10 million characters monthly into audio articles. Calculate costs after 2 months, including data transfer costs.

----

### 8. **AWS Lambda**

**Description:** Run code without provisioning or managing servers. Pay only for the compute time you consume.

**Free Tier:** 1 million free requests per month and 400,000 GB-seconds of compute time per month.

**Pricing Units:** Per request and GB-second.

**Previous Knowledge Required:** Basic programming knowledge (e.g., Python, Node.js).

**Demonstration Suggestions:**
- Write and deploy a simple serverless function.
- Trigger the function with an S3 event or HTTP request.
- Integrate Lambda with DynamoDB for real-time data processing.
- Implement a serverless API using API Gateway and Lambda.

**Cost Scenarios:**
1. A web application triggers Lambda functions 2 million times monthly with 1 million GB-seconds of compute time. Calculate costs after 3 months, including both free and paid usage.
2. A data processing pipeline uses Lambda to handle 500,000 requests monthly, consuming 200,000 GB-seconds. Calculate costs after 2 months, considering data transfer.
3. An IoT application triggers Lambda functions 3 million times monthly with 1.5 million GB-seconds of compute time. Calculate costs after 4 months, including storage and retrieval costs.

----

### 9. **Amazon DynamoDB**

**Description:** Key-value and document database that delivers single-digit millisecond performance at any scale.

**Free Tier:** 25 GB of storage, 25 read capacity units, and 25 write capacity units.

**Pricing Units:** Per read/write capacity unit and per GB.

**Previous Knowledge Required:** Basic understanding of database concepts.

**Demonstration Suggestions:**
- Create a DynamoDB table and insert data.
- Query the table and demonstrate indexing.
- Implement a time-series data store with DynamoDB.
- Set up DynamoDB Streams to trigger Lambda functions.

**Cost Scenarios:**
1. A web app with 10,000 daily users performing 1,000 reads and 500 writes per second, storing 100 GB of data. Calculate costs after 2 months, including both free and paid usage.
2. An IoT platform processes 5,000 writes per second and 2,500 reads per second, storing 200 GB. Calculate costs  after 3 months, considering data transfer and retrieval.
3. A mobile app with 50,000 monthly users storing user sessions, requiring 2,000 reads and 1,000 writes per second, storing 150 GB. Calculate costs after 4 months, including indexing costs.

----

### 10. **Amazon SQS (Simple Queue Service)**

**Description:** Fully managed message queuing service to decouple and scale microservices, distributed systems, and serverless applications.

**Free Tier:** 1 million requests.

**Pricing Units:** Per request.

**Previous Knowledge Required:** Basic understanding of messaging and queueing concepts.

**Demonstration Suggestions:**
- Create a queue and send messages.
- Receive and process messages using a Lambda function.
- Implement a delay queue for processing tasks at a later time.
- Set up a dead-letter queue for handling failed messages.

**Cost Scenarios:**
1. A task processing system handles 2 million messages monthly. Calculate costs after 2 months, including both free and paid usage.
2. An order processing system manages 1 million messages monthly, with peak loads of 100,000 messages per day. Calculate costs after 3 months, considering data transfer.
3. A notification system processes 3 million messages monthly. Calculate costs after 4 months, including storage and retrieval costs.

----

### 11. **Amazon RDS (Relational Database Service)**

**Description:** Makes it easy to set up, operate, and scale a relational database in the cloud.

**Free Tier:** 750 hours of db.t2.micro or db.t3.micro instances per month for one year, along with 20 GB of storage.

**Pricing Units:** Per hour and per GB.

**Previous Knowledge Required:** Basic understanding of relational databases and SQL.

**Demonstration Suggestions:**
- Create a database instance and configure it.
- Connect to the database and perform CRUD operations.
- Set up a read replica for scaling read operations.
- Implement automatic backups and point-in-time recovery.

**Cost Scenarios:**
1. An online store runs a db.m5.large instance for 750 hours monthly with 100 GB of storage and a read replica. Calculate costs after 3 months, including both free and paid usage.
2. A SaaS application runs a db.r5.xlarge instance for 500 hours monthly with 200 GB of storage and multi-AZ deployment. Calculate costs after 4 months, considering data transfer.
3. A content management system runs a db.t3.medium instance for 1,000 hours monthly with 150 GB of storage. Calculate costs after 2 months, including backup and retrieval costs.

----

### 12. **Amazon EC2 (Elastic Compute Cloud)**

**Description:** Provides scalable computing capacity in the AWS cloud. Used for launching virtual servers.

**Free Tier:** 750 hours of t2.micro or t3.micro instances per month for one year.

**Pricing Units:** Per hour.

**Previous Knowledge Required:** Understanding of virtual machines, basic networking, and command line interface.

**Demonstration Suggestions:**
- Launch and configure a virtual server.
- Connect to the server via SSH and deploy a simple web application.
- Set up auto-scaling for an EC2 instance to handle varying traffic loads.
- Implement a load balancer to distribute traffic across multiple instances.

**Cost Scenarios:**
1. A web server runs a t3.medium instance for 500 hours monthly with 100 GB of data transfer. Calculate costs after 3 months, including both free and paid usage.
2. A high-traffic website runs a m5.large instance for 750 hours monthly with 200 GB of data transfer and auto-scaling. Calculate costs after 4 months, considering storage and retrieval.
3. A development environment runs a t3.small instance for 1,000 hours monthly with 50 GB of data transfer. Calculate costs after 2 months, including backup and retrieval costs.

----

### 13. **AWS CodeBuild**

**Description:** Fully managed build service that compiles source code, runs tests, and produces software packages.

**Free Tier:** 100 build minutes per month.

**Pricing Units:** Per build minute.

**Previous Knowledge Required:** Understanding of build processes, source control, and continuous integration.

**Demonstration Suggestions:**
- Set up a build project to compile and test a sample application.
- Integrate with CodePipeline for continuous integration.
- Implement a build project that triggers on code commits to a repository.
- Create a multi-stage build process with different environments (dev, test, prod).

**Cost Scenarios:**
1. A development team runs 500 build minutes monthly. Calculate costs after 2 months, including both free and paid usage.
2. An enterprise application runs 2,000 build minutes monthly. Calculate costs after 3 months, considering storage and retrieval.
3. A continuous deployment pipeline uses 1,000 build minutes monthly. Calculate costs after 4 months, including data transfer costs.

----

### 14. **AWS CodePipeline**

**Description:** Continuous integration and continuous delivery service for application and infrastructure updates.

**Free Tier:** 1 active pipeline per month.

**Pricing Units:** Per pipeline.

**Previous Knowledge Required:** Understanding of CI/CD processes, source control, and application deployment.

**Demonstration Suggestions:**
- Create a pipeline to automate the build, test, and deployment of an application.
- Demonstrate integration with GitHub for source control.
- Implement a pipeline with multiple stages for different environments (dev, test, prod).
- Set up automated testing and deployment with CodePipeline.

**Cost Scenarios:**
1. A small project uses 2 active pipelines for CI/CD. Calculate costs after 3 months, including both free and paid usage.
2. A large enterprise application uses 5 active pipelines for different services. Calculate costs after 4 months, considering storage and retrieval.
3. A microservices architecture uses 10 active pipelines. Calculate costs after 2 months, including data transfer costs.

----

### 15. **Amazon CloudFront**

**Description:** Content delivery network (CDN) service that securely delivers data with low latency.

**Free Tier:** 1 TB of data transfer out, 10,000,000 HTTP and HTTPS requests per month for one year.

**Pricing Units:** Per GB and per request.

**Previous Knowledge Required:** Basic understanding of content delivery networks and web performance optimization.

**Demonstration Suggestions:**
- Set up a CloudFront distribution to serve content from an S3 bucket.
- Demonstrate caching and invalidation of content.
- Implement a CloudFront distribution with custom SSL certificates.
- Set up geo-restrictions to control content access based on user location.

**Cost Scenarios:**
1. A media streaming service transfers 5 TB of data with 50,000,000 requests monthly. Calculate costs after 3 months, including both free and paid usage.
2. An e-commerce site transfers 10 TB of data with 100,000,000 requests monthly. Calculate costs after 4 months, considering storage and retrieval.
3. A global web application transfers 20 TB of data with 200,000,000 requests monthly. Calculate costs after 2 months, including data transfer costs.

----

### 16. **AWS Elastic Beanstalk**

**Description:** Easy-to-use service for deploying and scaling web applications and services.

**Free Tier:** 750 hours of use per month.

**Pricing Units:** Per hour.

**Previous Knowledge Required:** Understanding of web application deployment, basic programming, and application configuration.

**Demonstration Suggestions:**
- Deploy a sample web application.
- Show automatic scaling and monitoring of the application.
- Implement a deployment pipeline with Elastic Beanstalk and CodePipeline.
- Set up a multi-tier application with Elastic Beanstalk.

**Cost Scenarios:**
1. A standard web application environment runs for 500 hours monthly with a t3.medium instance. Calculate costs after 3 months, including both free and paid usage.
2. A high-availability environment runs for 750 hours monthly with m5.large instances. Calculate costs after 4 months, considering storage and retrieval.
3. A microservices application runs multiple environments for 1,000 hours monthly. Calculate costs after 2 months, including data transfer costs.

----

### 17. **Amazon ECS (Elastic Container Service)**

**Description:** Fully managed container orchestration service for running, stopping, and managing Docker containers.

**Free Tier:** 750 hours of t2.micro or t3.micro instances per month for one year (underlying EC2 instances).

**Pricing Units:** Per instance hour.

**Previous Knowledge Required:** Understanding of Docker and container orchestration.

**Demonstration Suggestions:**
- Deploy a simple Docker container on an ECS cluster.
- Set up an ECS service with a load balancer to distribute traffic.
- Implement auto-scaling for an ECS service.
- Create a task definition and run multiple tasks on ECS.

**Cost Scenarios:**
1. An application runs 3 Docker containers on a t3.medium instance for 500 hours monthly. Calculate costs after 3 months, including both free and paid usage.
2. A microservices architecture runs 10 Docker containers across 3 m5.large instances for 750 hours monthly. Calculate costs after 4 months, considering storage and retrieval.
3. A batch processing system runs 5 Docker containers on 2 t3.large instances for 1,000 hours monthly. Calculate costs after 2 months, including data transfer costs.

----

### 18. **Amazon EKS (Elastic Kubernetes Service)**

**Description:** Managed Kubernetes service for running Kubernetes clusters on AWS.

**Free Tier:** 750 hours of t2.micro or t3.micro instances per month for one year (underlying EC2 instances).

**Pricing Units:** Per instance hour and per EKS cluster hour.

**Previous Knowledge Required:** Understanding of Kubernetes and container orchestration.

**Demonstration Suggestions:**
- Create an EKS cluster and deploy a Kubernetes application.
- Set up Kubernetes ingress with  an Application Load Balancer.
- Implement Kubernetes auto-scaling using the Horizontal Pod Autoscaler.
- Integrate EKS with AWS Fargate for serverless containers.

**Cost Scenarios:**
1. An application runs on an EKS cluster with 3 t3.medium worker nodes for 500 hours monthly. Calculate costs after 3 months, including both free and paid usage.
2. A microservices architecture runs on an EKS cluster with 5 m5.large worker nodes for 750 hours monthly. Calculate costs after 4 months, considering storage and retrieval.
3. A CI/CD pipeline uses an EKS cluster with 2 t3.large worker nodes for 1,000 hours monthly. Calculate costs after 2 months, including data transfer costs.
