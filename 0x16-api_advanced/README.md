Project: 0x16.API advanced 

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to read API documentation to find the endpoints you’re looking for
How to use an API with pagination
How to parse JSON results from an API
How to make a recursive API call
How to sort a dictionary by value

A query string is a part of a uniform resource locator (URL) that assigns values to specified parameters. It commonly includes fields added to a base URL by a web browser or other client application. Query strings serve various purposes, such as:

Passing data to a web application or database.
Choosing the appearance of a page.
Jumping to specific positions in multimedia content.
Here’s how a typical URL containing a query string looks:

https://example.com/over/there?name=ferret

In this example:

The base URL is https://example.com/over/there.
The query string parameter is name=ferret.
The query string consists of a series of field-value pairs separated by an ampersand (&). For instance:

https://example.com/path/to/page?name=ferret&color=purple

In this URL:

name=ferret and color=purple are query parameters.
The question mark (?) separates the base URL from the query string.
Web forms often use query strings to encode form field values when submitted. For each field in the form, the query string contains a pair like field=value.