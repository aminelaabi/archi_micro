

class Config:

    CASCADE = "haarcascade_frontalface_default.xml"
    INDEX_HTML = "static/index.html"


    database_url = "postgresql://example:example@localhost:5432"
        
    securite_schemes = ["bcrypt"]
    deprecated = "auto"

    access_token_expire_minutes = 30
    secret_key = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm = "HS256"

    password_size = 8

    token_url = "user/login"