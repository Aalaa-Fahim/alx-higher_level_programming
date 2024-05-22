# JavaScript - Web Scraping

This repo provides a brief introduction to web scraping with JavaScript, focusing on manipulating JSON data, utilizing the Fetch API for HTTP requests, and performing file operations with the `fs` module in Node.js.

## Manipulating JSON Data

Manipulating JSON data involves converting JSON strings into JavaScript objects and vice versa. This is useful for processing data received from web services or stored in files.

Example:
```javascript
let jsonString = '{"name":"John", "age":30, "city":"New York"}';
let obj = JSON.parse(jsonString);
console.log(obj.name); // Output: John
```

## Using the Fetch API

The Fetch API is a modern, promise-based mechanism for making asynchronous HTTP requests in JavaScript. It's built into modern browsers and is part of the standard web platform.

Example:
```javascript
fetch('https://api.example.com/data')
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

## Reading and Writing Files with the `fs` Module

Node.js's `fs` module provides an API for interacting with the file system. This includes reading from and writing to files, which is essential for web scraping tasks that involve storing or retrieving data.

Example: Reading a JSON file
```javascript
const fs = require('fs');

fs.readFile('path/to/file.json', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  let jsonData = JSON.parse(data);
  console.log(jsonData);
});
```

Example: Writing to a JSON file
```javascript
const fs = require('fs');
const data = { key: 'value' };

fs.writeFile('path/to/file.json', JSON.stringify(data, null, 2), (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('File saved successfully.');
  }
});
```

## Conclusion

Web scraping with JavaScript involves extracting data from websites and processing it according to your needs. By mastering JSON manipulation, fetching data from APIs, and managing files with Node.js, you can build powerful web scraping tools and applications.
```
