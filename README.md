# URL Shortener in the Cloud

## What is this application do?
Provides a REST service that takes a long version of an URL and creates a shortened link.
For example: `https://www.gramann-ahrberg.de/filialen/filialen/ -> scth.io/byos1t34K`

## Characteristics
* Any URL can be sent to the REST service which will return a shortened URL.
* The shortened URL has a length of 10 characters.
* A shortened URL cannot be duplicated; e.g. two different links won’t provide the same short name.
* The service follows a Serverless architecture using AWS Lambda.
