<!-- Slide number: 1 -->
# Cloud Storage
Hants Williams, PhD, RN

<!-- Slide number: 2 -->
# Introduction to Cloud Storage
Cloud storage lets you store data online, managed by a cloud provider. Instead of having to keep files on local servers, you can access and manage data over the internet, from anywhere.

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 3 -->
# Introduction to Cloud Storage
Database Storage:
Cloud Storage: Best for unstructured data, like images, videos, or large data files, which don’t follow a strict format. Data is stored as objects (e.g., blobs).
Database Storage: Used for structured data that needs to be organized in tables (like patient records in a database) with specific formats and relationships.

<!-- Slide number: 4 -->

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
https://www.researchgate.net/figure/Unstructured-and-structured-data-generated-by-healthcare-organizations-adapted-from-44_fig3_368565404

<!-- Slide number: 5 -->
# Primary Use Cases
Content Delivery: Efficiently serve digital content (e.g., videos, images) to users across the globe.

![pasted-movie.png](pastedmoviepng.jpg)
https://cloud.google.com/about/locations

<!-- Slide number: 6 -->
# Primary Use Cases

![pasted-movie.png](pastedmoviepng.jpg)
Data Backup and Recovery: Securely store data backups with easy access for disaster recovery. {e.g., stream medical images and videos directly to doctors and patients from storage; protecting against ransomware}
https://cloud.google.com/about/locations

<!-- Slide number: 7 -->
# Primary Use Cases
Archiving: Store large volumes of infrequently accessed data in low-cost storage options. {e.g., saving data for HIPAA required minimums}
Data Analytics: Store raw data that can be processed by cloud-based analytics and AI tools. {store large sets of patient data, like medical imaging or genomics, which can then be processed by cloud-based tools for research and insights}

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 8 -->
# Applications built with cloud storage:
w/ Azure
The same storage system that powers Google Cloud also underpins Google’s most popular products, supporting globally available services with more than billion users across the globe, like YouTube, Drive, Gmail, Photos, workspace suite of products, etc.

![Screenshot 2024-10-07 at 7.56.24 AM.png](Screenshot20241007at75624AMpng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![Screenshot 2024-10-07 at 8.07.01 AM.png](Screenshot20241007at80701AMpng.jpg)
https://cloud.google.com/customers/hmh?hl=en
https://cloud.google.com/customers/johnson-and-johnson

![Screenshot 2024-10-07 at 8.06.17 AM.png](Screenshot20241007at80617AMpng.jpg)
https://cloud.google.com/customers/hca

![Screenshot 2024-10-07 at 8.05.22 AM.png](Screenshot20241007at80522AMpng.jpg)

![Screenshot 2024-10-07 at 8.05.52 AM.png](Screenshot20241007at80552AMpng.jpg)
https://cloud.google.com/customers/nyc-cyber-command
https://cloud.google.com/customers/priceline

![Screenshot 2024-10-07 at 8.04.00 AM.png](Screenshot20241007at80400AMpng.jpg)

<!-- Slide number: 9 -->

![fask_azure_blob_storage.png](fask_azure_blob_storagepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 10 -->

![flask_datascience_pipeline.png](flask_datascience_pipelinepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 11 -->
Types of Cloud Storage Mechanisms

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
AWS

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
GCP
	Managed Disks
	Azure Files
	Azure Blob Storage
AZURE

![Azure Storage - Files.png.jpg](AzureStorageFilespngjpg.jpg)

![VHD data disk.png.jpg](VHDdatadiskpngjpg.jpg)

![Azure Storage - Blob.png.jpg](AzureStorageBlobpngjpg.jpg)

<!-- Slide number: 12 -->
# Block Storage

![pasted-movie.png](pastedmoviepng.jpg)
Data is stored in small blocks, each with a unique identifier. Applications control how the blocks are arranged and accessed, making it highly flexible and fast.
Commonly used for virtual machines and databases

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
	Managed Disks

![VHD data disk.png.jpg](VHDdatadiskpngjpg.jpg)

<!-- Slide number: 13 -->
# File Storage

![pasted-movie.png](pastedmoviepng.jpg)
Data is stored in a hierarchy of folders and files, similar to a local computer’s file system. Each file is organized by name and directory path.
Ideal for shared drives, document storage, and applications where data needs to be easily organized in folders
Example: Storing shared documents, such as medical policies or training videos, that need to be accessed by various staff across departments.

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
	Azure Files

![Azure Storage - Files.png.jpg](AzureStorageFilespngjpg.jpg)

<!-- Slide number: 14 -->
# Object (blob) Storage

![pasted-movie.png](pastedmoviepng.jpg)
Data is stored as objects in a flat structure within “buckets” or “containers.” Each object has metadata and a unique ID, making it ideal for unstructured data. It’s highly scalable and accessible over the internet.
Best for large volumes of unstructured data, such as multimedia files, backups, and big data storage.
Storing large files like MRI scans, X-rays, and genomic data, which can be accessed by specialists across different locations.

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
	Azure Blob Storage

![Azure Storage - Blob.png.jpg](AzureStorageBlobpngjpg.jpg)

<!-- Slide number: 15 -->
# Subtypes of object for GCP

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 16 -->
# Subtypes of object for GCP

![pasted-movie.png](pastedmoviepng.jpg)

![Screenshot 2024-10-07 at 9.40.45 AM.png](Screenshot20241007at94045AMpng.jpg)

<!-- Slide number: 17 -->
# Subtypes of object for Azure

![Screenshot 2024-10-07 at 9.37.16 AM.png](Screenshot20241007at93716AMpng.jpg)

![Screenshot 2024-10-07 at 9.39.53 AM.png](Screenshot20241007at93953AMpng.jpg)
https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
https://azure.microsoft.com/en-us/pricing/details/storage/blobs/

<!-- Slide number: 18 -->
File Storage is best for organized, shared access.

Block Storage is optimized for fast access and control often for VM’s

Object Storage is ideal for scalable, unstructured data access over the internet.

<!-- Slide number: 19 -->
# How to access

![Screenshot 2024-10-07 at 9.31.50 AM.png](Screenshot20241007at93150AMpng.jpg)
Console: It provides a visual interface for you to manage your data in a browser.
Client libraries: The Cloud Storage client libraries allow you to manage your data using one of your preferred languages, including C++, C#, Go, Java, Node.js, PHP, Python, and Ruby.
REST APIs: It manage our data using the JSON or XML API.

![Screenshot 2024-10-07 at 9.31.57 AM.png](Screenshot20241007at93157AMpng.jpg)

![Screenshot 2024-10-07 at 9.32.03 AM.png](Screenshot20241007at93203AMpng.jpg)

<!-- Slide number: 20 -->
# Cloud Console

![pasted-movie.png](pastedmoviepng.jpg)
A web-based interface provided by cloud providers like Azure and GCP. It allows users to interact with cloud storage through a graphical interface.

Users can upload, manage, and organize data in storage systems. It also provides options for monitoring usage, configuring settings, and managing security permissions.

NOT GOOD for automation and working with your code (e.g., is manual process); good for setting things up

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 21 -->
# Client Libraries (SDKs): Software Development Kits

![pasted-movie.png](pastedmoviepng.jpg)
Programming libraries available in multiple languages (e.g., Python, Java, .NET) that allow developers to integrate cloud storage directly into applications.

Client libraries provide functions for tasks like uploading files, reading data, managing permissions, and more. They are ideal for automating storage operations within custom applications.

E.g., a python client library can be used to automatically save and retrieve genomic data from cloud storage, enabling streamlined access for data analysis.

![pasted-movie.png](pastedmoviepng.jpg)
https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview
https://cloud.google.com/python/docs/reference

<!-- Slide number: 22 -->
# Azure Storage with Python SDK
https://learn.microsoft.com/en-us/azure/developer/python/sdk/examples/azure-sdk-example-storage?tabs=cmd

![Screenshot 2024-10-07 at 9.47.24 AM.png](Screenshot20241007at94724AMpng.jpg)

![Screenshot 2024-10-07 at 9.47.51 AM.png](Screenshot20241007at94751AMpng.jpg)

<!-- Slide number: 23 -->
# Azure Storage with Python SDK
https://learn.microsoft.com/en-us/azure/developer/python/sdk/examples/azure-sdk-example-storage?tabs=cmd

![Screenshot 2024-10-07 at 9.47.51 AM.png](Screenshot20241007at94751AMpng.jpg)

<!-- Slide number: 24 -->
# GCP SDK Python - Storage
https://cloud.google.com/python/docs/reference/storage/latest

![Screenshot 2024-10-07 at 9.49.17 AM.png](Screenshot20241007at94917AMpng.jpg)

<!-- Slide number: 25 -->
# GCP SDK Python - Storage

![Screenshot 2024-10-07 at 9.51.13 AM.png](Screenshot20241007at95113AMpng.jpg)
https://github.com/googleapis/python-storage/tree/main/samples

<!-- Slide number: 26 -->
# APIs
APIs provide direct, programmatic access to cloud storage over HTTP. Data is accessible by making HTTP requests, which can be automated and customized.

APIs offer flexibility to build fully customized storage solutions and integrate storage capabilities into various systems, regardless of platform.

Example: A hospital’s telemedicine platform uses REST API calls to store and retrieve patient imaging data from cloud storage, making it accessible for remote consultations.

![Screenshot 2024-10-07 at 9.55.06 AM.png](Screenshot20241007at95506AMpng.jpg)

![Screenshot 2024-10-07 at 9.55.59 AM.png](Screenshot20241007at95559AMpng.jpg)

![Screenshot 2024-10-07 at 9.56.39 AM.png](Screenshot20241007at95639AMpng.jpg)

![Screenshot 2024-10-07 at 9.57.07 AM.png](Screenshot20241007at95707AMpng.jpg)
https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api

<!-- Slide number: 27 -->
# APIs
GET request:

![Screenshot 2024-10-07 at 9.58.16 AM.png](Screenshot20241007at95816AMpng.jpg)
Response:

![Screenshot 2024-10-07 at 9.58.32 AM.png](Screenshot20241007at95832AMpng.jpg)
https://cloud.google.com/storage/docs/json_api

<!-- Slide number: 28 -->
# APIs
DELETE (removing object):

![Screenshot 2024-10-07 at 10.00.50 AM.png](Screenshot20241007at100050AMpng.jpg)
Response:

![Screenshot 2024-10-07 at 10.03.04 AM.png](Screenshot20241007at100304AMpng.jpg)
https://cloud.google.com/storage/docs/json_api/v1/objects/delete

<!-- Slide number: 29 -->
# Comparisons
Cloud Console: Easy, visual interface for basic tasks and quick management.

Client Libraries: Ideal for integration into applications, with support for various programming languages.

REST APIs: Most flexible option for programmatic access, suitable for custom integrations and automation.