## Description

This project is a demonstration of a Rectangle class in JavaScript. It provides a basic implementation of a rectangle object, allowing users to create rectangles, calculate their area and perimeter.

## Features

- Create rectangles by specifying the length and width.
- Calculate the area of a rectangle.
- Calculate the perimeter of a rectangle.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/project-name.git`
2. Navigate to the project directory: `cd project-name`
3. Install the dependencies: `npm install`

## Usage

To use the Rectangle class in your project, follow these steps:

1. Import the Rectangle class: `const Rectangle = require('./path/to/Rectangle');`
2. Create a new instance of the Rectangle class: `const rectangle = new Rectangle(length, width);`
3. Access the properties and methods of the rectangle object as needed.

Example:

```javascript
const Rectangle = require('./path/to/Rectangle');

const rectangle = new Rectangle(4, 6);
console.log(rectangle.calculateArea());       // Output: 24
console.log(rectangle.calculatePerimeter());  // Output: 20
