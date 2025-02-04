from models import SessionLocal, User


def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()


def create_user(id: int, birthdate):
    session = SessionLocal()

    try:
        new_user = User(id = id, birthdate = birthdate)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user
    
    except Exception as err:
        session.rollback()
    
    finally:
        session.close()


def get_user_by_id(user_id: int):
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    
    except Exception as e:
        pass

    finally:
        db.close()
