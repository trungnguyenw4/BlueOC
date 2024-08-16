# React-Redux Posts App

## Overview

This is a React-Redux application that fetches and displays posts from an API, includes a form to add new posts, and persists new posts across page refreshes using Redux and `redux-persist`.

## Features

- Fetch and display posts from the API endpoint [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts).
- Add new posts using a form.
- Persist new posts to local storage and maintain them across page refreshes.
- Input validation - users can not submit a form with empty header or body.


##Usage

Fetching Posts: The application fetches posts from the API and displays them on the page.

Adding Posts: Use the form to add new posts. The posts will be saved to local storage and will persist across page refreshes.

##Technologies Used
React
Redux
Redux Toolkit
Redux Persist
CSS

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/trungnguyenw4/BlueOC/edit/main/react-redux-application
   cd react-redux-posts

2. Install dependencies:
   ```
   npm install

4. Start the application:
   ```
    npm start
