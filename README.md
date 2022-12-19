# LAB - Class 28

## Project: Books API Authentication & Production Server 

### Author: Mohammad Khader

### Links and Resources

- [Class Repo](https://github.com/LTUC/amman-python-401d10/tree/main/Class-28)

### Setup

- Clone the Repo
- Run the server
- `http://127.0.0.1:8000/api/v1/books/` To see the books API
- 

#### `.env` requirements (where applicable)


#### How to initialize/run your application (where applicable)

- To run the server
- `python manage.py runserver`

#### How to use your library (where applicable)

#### Tests
##### Testing Using Postman:
1. Send a get request to `http://127.0.0.1:8000/api/v1/books/` to see the data
2. Try sending a post request to `http://127.0.0.1:8000/api/v1/books/` without authentication will fail.
3. Send a post request to `http://127.0.0.1:8000/api/v1/books/` using the basic authentication with the following:
- {"book_name": "The Secret",
"book_genre": "Fantasy",
"book_rating": 8,
"owner": 1}
- Username : admin
- Password mohammad123
- The data will be added to the API
4. To test the tokens send a post request to `http://127.0.0.1:8000/api/token/` with the following body:
`{"username":"admin",`
`"password":"mohammad123"}`
- The response will contain an access token and a refresh token
5. We can use the access token as bearer authentication to post more data to the API.
- The access token will be working for 5 minutes
6. To get a new access token after the first one expired, we send a post request to `http://127.0.0.1:8000/api/token/refresh/` containing the refresh token in the body.
- The response will be a new access token

