import db
import secure

def main():
    conn = db.connect()
    db.create_db(conn)
    db.disconnect(conn)
    sec = secure.encrypt("Hi")
    print(sec)
    msg = secure.decrypt(sec)
    print(msg)

if __name__ == "__main__":
    main()
