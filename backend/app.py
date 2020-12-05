from flask import Flask, request, Response
from flask_cors import CORS
import mariadb 
import random 
import json
import dbcreds
import secrets
import datetime

def generateToken():
    random_alphanumeric = secrets.token_urlsafe(20)
    return random_alphanumeric
def createDateTime():
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d")
    return currentdate

app = Flask(__name__)
CORS(app)

@app.route('/api/users', methods = ["GET","POST", "PATCH", "DELETE"])
def usersendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        users = None
        userId = request.args.get("userId")
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if userId != "" and userId != None:
                cursor.execute("SELECT u.username,u.email,u.bio,u.birthdate,u.userId FROM users u WHERE userId=?",[userId,])
            else:
                cursor.execute("SELECT users.username,users.email,users.bio,users.birthdate,users.userId FROM users")
            users = cursor.fetchall()
            print(users)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(users != None):
                allusers = []
                for user in users:
                    users_info = {
                    "userId": user[4],
                    "email": user[1],
                    "username": user[0],
                    "bio": user[2],
                    "birthdate": user[3]
                }
                    allusers.append(users_info)
                
                return Response(json.dumps(allusers, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
#endpoint complete and checked 

    elif request.method == "POST":
        conn = None
        cursor = None
        users_email = request.json.get("email")
        users_username = request.json.get("username")
        users_password = request.json.get("password")
        users_bio = request.json.get("bio")
        users_birthdate = request.json.get("birthdate")
        loginToken = generateToken()
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users(username,email,bio,birthdate,password) VALUES(?,?,?,?,?)",[users_username,users_email,users_bio,users_birthdate,users_password])
            conn.commit()
            rows = cursor.rowcount
            if (rows == 1):
                global user_Id 
                user_Id = cursor.lastrowid
                cursor.execute("INSERT INTO user_session(loginToken,user_Id) VALUES(?,?)",[loginToken,user_Id])
                conn.commit()
                rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                newUser = {
                    "userId": user_Id,
                    "email": users_email,
                    "username": users_username,
                    "bio": users_bio,
                    "birthdate": users_birthdate,
                    "loginToken": loginToken
                }
                return Response(json.dumps(newUser, default = str), mimetype = "application/json", status = 201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
#endpoint complete and checked 

    elif request.method == "PATCH":
        conn = None
        cursor = None
        users_bio = request.json.get("bio")
        users_username = request.json.get("username")
        users_birthdate = request.json.get("birthdate")
        loginToken = request.json.get("loginToken")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if users_bio != "" and users_bio != None:
                cursor.execute("UPDATE users INNER JOIN user_session ON users.userId = user_session.user_Id SET users.bio=? WHERE user_session.loginToken=?",[users_bio,loginToken,])
            if users_username != "" and users_username != None:
                cursor.execute("UPDATE users INNER JOIN user_session ON users.userId = user_session.user_Id SET users.username=?  WHERE user_session.loginToken=?",[users_username,loginToken,])
            if users_birthdate  != "" and users_bio != None:
                cursor.execute("UPDATE users INNER JOIN user_session ON users.userId = user_session.user_Id SET users.birthdate=? WHERE user_session.loginToken=?",[users_birthdate,loginToken,])
            conn.commit()
            cursor.execute("SELECT u.userId, u.email, u.username, u.bio, u.birthdate FROM users u INNER JOIN user_session us ON u.userId = us.user_Id WHERE us.loginToken=?",[loginToken])
            user = cursor.fetchall()[0]
            print(user)
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                this_user = {
                    "userId": user[0],
                    "email":  user[1],
                    "username":  user[2],
                    "bio":  user[3],
                    "birthdate":  user[4],
                }
                return Response(json.dumps(this_user, default = str), mimetype = "application/json", status = 200)
            else: 
                return Response("Updated Failed", mimetype="text/html", status=404)
#endpoint complete and checked 

    elif request.method == "DELETE":
        conn = None
        cursor = None
        user_password = request.json.get("password")
        loginToken = request.json.get("loginToken")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT user_Id FROM user_session WHERE user_session.loginToken=?",[loginToken])
            cursor.execute("DELETE FROM users WHERE password=?",[user_password])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("DELETE Success", mimetype = "text/html", status = 204)
            else: 
                return Response("DELETE Failed", mimetype="text/html", status=404)
#endpoint complete and checked 

@app.route('/api/login', methods = ["POST","DELETE"])
def user_Loginendpoint():
    if request.method == "POST":
        conn = None
        cursor = None
        users_email = request.json.get("email")
        users_password = request.json.get("password")
        loginToken = generateToken()
        users = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if (users_email != "" and users_email != None) and (users_password != "" and users_password != None):
                cursor.execute("SELECT u.userId,u.email,u.username,u.bio,u.birthdate FROM users u WHERE u.email=? AND u.password=?",[users_email,users_password])
            users = cursor.fetchall()[0]
            print(users)
            rows = cursor.rowcount
            if (rows == 1):
                user_Id = users[0]
                cursor.execute("INSERT INTO user_session(loginToken,user_Id) VALUES(?,?)",[loginToken,user_Id])
                conn.commit()
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                user_Login = {
                    "userId": users[0],
                    "email": users[1],
                    "username": users[2],
                    "bio": users[3],
                    "birthdate": users[4],
                    "loginToken": loginToken
                }
                return Response(json.dumps(user_Login, default = str), mimetype = "application/json", status = 201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
#endpoint complete and checked 

    elif request.method == "DELETE":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user_session WHERE loginToken=?",[loginToken,])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("DELETE Success", mimetype = "text/html", status = 204)
            else: 
                return Response("DELETE Failed", mimetype="text/html", status=404)
#endpoint complete and checked 

@app.route('/api/follows', methods = ["GET","POST", "DELETE"])
def followendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        users = None
        userId = request.args.get("userId")
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if userId != "" and userId != None:
                cursor.execute("SELECT users.userId, users.email, users.username, users.bio, users.birthdate FROM users INNER JOIN users_follows ON users.userId = users_follows.followed_Id WHERE users_follows.users_Id=? ",[userId,])
            users = cursor.fetchall()
            print(users)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(users != None):
                myFollowers = []
                for user in users:
                    user_info = {
                    "userId": user[0],
                    "email": user[1],
                    "username": user[2],
                    "bio": user[3],
                    "birthdate": user[4]
                    }
                    myFollowers.append(user_info)
                return Response(json.dumps(myFollowers, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
#double check this endpoint with ALEX !!!!!

    elif request.method == "POST":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_followId =  request.json.get("followId")
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            userId = cursor.fetchall()[0][0]
            print(userId)
            cursor.execute("INSERT INTO users_follows(users_Id,followed_Id) VALUES(?,?)",[userId,users_followId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("user followed", mimetype="text/html", status=204)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
                

    elif request.method == "DELETE":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_followId =  request.json.get("followId")
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            userId = cursor.fetchall()[0][0]
            cursor.execute("DELETE FROM users_follows WHERE users_Id=? AND followed_Id=?",[userId,users_followId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for this error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("follow deleted!", mimetype="text/html", status=204)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)

@app.route('/api/followers', methods = ["GET"])
def followersendpoint():
     if request.method == "GET":
        conn = None
        cursor = None
        users = None
        userId = request.args.get("userId")
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if userId != "" and userId != None:
                cursor.execute("SELECT users.userId, users.email, users.username, users.bio, users.birthdate FROM users INNER JOIN users_follows ON users.userId = users_follows.users_Id WHERE userId=? ",[userId,])
            users = cursor.fetchall()
            print(users)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(users != None):
                myFollowers = []
                for user in users:
                    user_info = {
                    "userId": user[0],
                    "email": user[1],
                    "username": user[2],
                    "bio": user[3],
                    "birthdate": user[4]
                }
                myFollowers.append(user_info)
                return Response(json.dumps(myFollowers, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)



@app.route('/api/tweets', methods = ["GET","POST", "PATCH", "DELETE"])
def tweetsendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        userId = request.args.get("userId")
        tweets = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if userId != "" and userId != None:
                cursor.execute("SELECT t.Id, u.userId,u.username,t.content,t.createdAt FROM tweets t INNER JOIN users u ON u.userId = t.userId WHERE t.userId=?",[userId,])
            else:
                cursor.execute("SELECT t.Id, u.userId,u.username,t.content,t.createdAt FROM tweets t INNER JOIN users u ON u.userId = t.userId")
            tweets = cursor.fetchall()
            print(tweets)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(tweets != None):
                allTweets = []
                for tweet in tweets:
                    tweet_info = {
                        "tweetId": tweet[0],
                        "userId": tweet[1],
                        "username": tweet[4],
                        "content": tweet[2],
                        "createdAt": tweet[3]
                    }
                    allTweets.append(tweet_info)
                return Response(json.dumps(allTweets, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "POST":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_content = request.json.get("content")
        createdAt= createDateTime()
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT users.userId, users.username FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE loginToken=?",[loginToken])
            user = cursor.fetchone()
            print(user)
            cursor.execute("INSERT INTO tweets(userId,content,createdAt) VALUES(?,?,?)",[user[0],users_content,createdAt])
            rows = cursor.rowcount
            tweetId = cursor.lastrowid
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                tweet_info = {
                    "tweetId": tweetId,
                    "userId": user[0],
                    "username": user[1],
                    "content": users_content,
                    "createdAt": createdAt,
                }
                return Response(json.dumps(tweet_info, default = str), mimetype = "application/json", status = 201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)

    elif request.method == "PATCH":
        conn = None
        cursor = None
        users_content = request.json.get("content")
        users_tweetId = request.json.get("tweetId")
        loginToken = request.json.get("loginToken")
        userId = None

        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            user = cursor.fetchall()
            print(user)
            cursor.execute("SELECT userId FROM tweets WHERE Id=?",[users_tweetId])
            tweet_owner = cursor.fetchall()
            print(tweet_owner)
            if (user[0][0] == tweet_owner[0][0]):
                cursor.execute("UPDATE tweets SET content=? WHERE Id=?",[users_content,users_tweetId])
                conn.commit()
                rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                tweet_updated = {
                    "tweetId": users_tweetId,
                    "content": users_content
                }
                return Response(json.dumps(tweet_updated, default = str), mimetype = "application/json", status = 200)
            else: 
                return Response("Updated Failed", mimetype="text/html", status=404)

    elif request.method == "DELETE":
        conn = None
        cursor = None
        users_tweetId = request.json.get("tweetId")
        loginToken = request.json.get("loginToken")
        user_Id = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT user_Id FROM user_session WHERE user_session.loginToken=?",[loginToken])
            user_Id = cursor.fetchall()[0][0]
            print(user_Id)
            cursor.execute("SELECT userId FROM tweets WHERE Id=?",[users_tweetId])
            tweet_owner = cursor.fetchall()[0][0] 
            print(tweet_owner)
            if (user_Id == tweet_owner):
                cursor.execute("DELETE FROM tweets WHERE Id=?",[users_tweetId])
                conn.commit()
                rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("DELETE Success", mimetype = "text/html", status = 204)
            else: 
                return Response("DELETE Failed", mimetype="text/html", status=404)


@app.route('/api/comments', methods = ["GET","POST", "PATCH", "DELETE"])
def commentsendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        users_tweetId = request.args.get("tweetId")
        comments = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if users_tweetId != "" and users_tweetId != None:
                cursor.execute("SELECT * FROM comment INNER JOIN users ON users.userId = comment.user_Id WHERE tweet_Id=?",[users_tweetId])
            else:
                cursor.execute("SELECT * FROM comments")
            comments = cursor.fetchall()
            print(comments)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(comments != None):
                allComments = []
                for comment in comments:
                    comments_info = {
                        "commentId": comment[2],
                        "tweetId": comment[3],
                        "userId": comment[4],
                        "username": comment[5],
                        "content": comment[0],
                        "createdAt": comment[1]
                    }
                    allComments.append(comments_info)
                return Response(json.dumps(allComments, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "POST":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_tweetId = request.json.get("tweetId")
        users_content = request.json.get("content")
        createdAt= createDateTime()
        user = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT users.userId, users.username FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE loginToken=?",[loginToken])
            user = cursor.fetchall()[0]
            print(user)
            cursor.execute("INSERT INTO comment(content,createdAt,tweet_Id,user_Id) VALUES(?,?,?,?)",[users_content,createdAt,users_tweetId,user[0]])
            conn.commit()
            rows = cursor.rowcount
            commentId = cursor.lastrowid
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                comment_info = {
                    "commentId": commentId,
                    "tweetId": users_tweetId,
                    "userId": user[0],
                    "username": user[1],
                    "content": users_content,
                    "createdAt": createdAt,
                }
                return Response(json.dumps(comment_info, default = str), mimetype = "application/json", status = 201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)

    elif request.method == "PATCH":
        conn = None
        cursor = None
        users_content = request.json.get("content")
        users_commentId= request.json.get("commentId")
        loginToken = request.json.get("loginToken")
        createdAt = createDateTime()
        user = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId, username FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            user = cursor.fetchall()
            print(user)
            cursor.execute("SELECT user_Id, tweet_Id FROM comment WHERE Id=?",[users_commentId])
            comment_owner = cursor.fetchall()
            print(comment_owner)
            if (user[0][0] == comment_owner[0][0]):
                cursor.execute("UPDATE comment SET content=? WHERE Id=?",[users_content,users_commentId])
                conn.commit()
                rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                comment_updated = {
                    "commentId": users_commentId,
                    "tweetId":comment_owner[0][1],
                    "userId": user[0][0],
                    "username":user[0][1] ,
                    "content": users_content,
                    "createdAt": createdAt
                }
                return Response(json.dumps(comment_updated, default = str), mimetype = "application/json", status = 200)
            else: 
                return Response("Updated Failed", mimetype="text/html", status=404)

    elif request.method == "DELETE":
        conn = None
        cursor = None
        users_commentId= request.json.get("commentId")
        loginToken = request.json.get("loginToken")
        user_Id = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT user_Id FROM user_session WHERE user_session.loginToken=?",[loginToken])
            user_Id = cursor.fetchall()[0][0]
            print(user_Id)
            cursor.execute("SELECT user_Id FROM comment WHERE Id=?",[users_commentId])
            comment_owner = cursor.fetchall()[0][0] 
            print(comment_owner)
            if (user_Id == comment_owner):
                cursor.execute("DELETE FROM comment WHERE Id=?",[users_commentId])
                conn.commit()
                rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("DELETE Success", mimetype = "text/html", status = 204)
            else: 
                return Response("DELETE Failed", mimetype="text/html", status=404)


@app.route('/api/tweet-likes', methods = ["GET","POST", "DELETE"])
def tweetLikesEndPoint():
    if request.method == "GET":
        conn = None
        cursor = None
        users_tweetId = request.args.get("tweetId")
        alltweetlikes = None

        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if users_tweetId != "" and users_tweetId != None:
                cursor.execute("SELECT t.tweetlike_Id,u.userId,u.username FROM tweet_like t INNER JOIN users u ON t.user_Id = u.userId WHERE t.tweetlike_Id=? ",[users_tweetId,])
            else:
                cursor.execute("SELECT t.tweetlike_Id,u.userId,u.username FROM tweet_like t INNER JOIN users u ON t.user_Id = u.userId")
            alltweetlikes = cursor.fetchall()
            print(alltweetlikes)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(alltweetlikes!= None):
                gettingtweetlikes = []
                for x in alltweetlikes:
                    tweetLike_info = {
                    "tweetId": x[0],
                    "userId": x[1],
                    "username": x[2]
                    }
                    gettingtweetlikes.append(tweetLike_info)

                return Response(json.dumps(gettingtweetlikes, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "POST":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_tweetId =  request.json.get("tweetId")
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            userId = cursor.fetchall()[0][0]
            print(userId) 
            cursor.execute("INSERT INTO tweet_like(tweetlike_Id,user_Id) VALUES(?,?)",[users_tweetId,userId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("You made a like on a tweet!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
                

    elif request.method == "DELETE":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_tweetId =  request.json.get("tweetId")
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            userId = cursor.fetchall()[0][0]
            print(userId) 
            cursor.execute("DELETE FROM tweet_like WHERE tweetlike_Id=? AND user_Id",[users_tweetId,userId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Tweet like deleted!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


@app.route('/api/comment-likes', methods = ["GET","POST", "DELETE"])
def commentLikesEndPoint():
    if request.method == "GET":
        conn = None
        cursor = None
        users_commentId = request.args.get("commentId")
        thiscommentlike = None
        allcommentlikes = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if users_commentId != "" and users_commentId != None:
                cursor.execute("SELECT c.comment_Id,u.userId,u.username FROM comment_like c INNER JOIN users u ON c.user_Id = u.userId WHERE c.comment_Id=? ",[users_commentId,])
            else:
                cursor.execute("SELECT c.comment_Id,u.userId,u.username FROM comment_like c INNER JOIN users u ON c.user_Id = u.userId")
            allcommentlikes = cursor.fetchall()
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(allcommentlikes != None):
                getcommentlikes = []
                for commentlike in allcommentlikes:
                    commentLike_info = {
                    "commentId": commentlike[0],
                    "userId": commentlike[1],
                    "username": commentlike[2]
                     }
                    getcommentlikes.append(commentLike_info)
    
                return Response(json.dumps(getcommentlikes, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "POST":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_commentId = request.json.get("commentId")
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            userId = cursor.fetchall()[0][0]
            print(userId) 
            cursor.execute("INSERT INTO comment_like(comment_id,user_Id) VALUES(?,?)",[users_commentId ,userId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("You made a like on a comment!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
                

    elif request.method == "DELETE":
        conn = None
        cursor = None
        loginToken = request.json.get("loginToken")
        users_commentId = request.json.get("commentId")
        userId = None
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT userId FROM users INNER JOIN user_session ON users.userId = user_session.user_Id WHERE user_session.loginToken=?",[loginToken])
            userId = cursor.fetchall()[0][0]
            print(userId) 
            cursor.execute("DELETE FROM comment_like WHERE comment_Id=? AND user_Id",[users_commentId,userId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Comment like deleted!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)



       
