<p align="center">
  <a href="" rel="noopener">
</p>

<h3 align="center">Auth REST API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> 
    <br> REST API made in Python implementing Auth Flow from Scratch
    <br> User can signup, signin, signout, check authorization and refresh their token
</p>

## 📝 Table of Contents

-  [About](#about)
-  [Getting Started](#getting_started)
-  [Built Using](#built_using)
-  [Authors](#authors)

## 🧐 About <a name = "about"></a>

Deliverables of this API:

1. Sign up (creation of user) using email and password
2. Sign in - Authentication of user credentials - A token is returned as response preferably JWT
3. Authorization of token - Mechanism of sending token along with a request from client to service - Should check for expiry - Error handling (proper error codes in each failure scenario)
4. Revocation of token - Mechanism of revoking a token from backend
5. Mechanism to refresh a token - Client should be able to renew the token before it expires

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Install Python.
2. Clone this project into your local directory.
3. Make sure to be in the parent directory of the "src" folder
4. Run :

```
pip install -r requirements.txt
```

4. To run the server at port 8000 (default):

```
python -m uvicorn src.main:app --reload
```

5. To check if the server is up, refer Postman collection in the "tests" directory.
6. Refer Postman Collection to check the endpoints.
7. OpenAPI Swagger Documentation is available at:

```
http://localhost:8000/docs
```

## ⛏️ Built Using <a name = "built_using"></a>

-  [Python](https://www.python.org/) - Programming Language
-  [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/) - Server Framework
-  [JSON](https://www.json.org/) - Database (Simulation)

## ✍️ Authors <a name = "authors"></a>

-  [Shivam Shukla](https://github.com/lastropy) - Design and Implementation
