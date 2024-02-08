from sqlalchemy import create_engine, Column, String, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column('id', INTEGER, primary_key=True)
    f_name = Column('f_name', String(50))
    l_name = Column('l_name', String(50))
    username = Column('username', String(50))
    email = Column('email', String(50))
    phone = Column('phone', INTEGER)
    age = Column('age', INTEGER)

    def __init__(self, id, f_name, l_name, username, email, phone, age):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.email = email
        self.phone = phone
        self.age = age

    def __repr__(self):
        return f"User(id={self.id}, f_name={self.f_name}, l_name={self.l_name}, username={self.username}, email={self.email}, phone={self.phone}, age={self.age})"


engine = create_engine("sqlite:///DB.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
user = User(1, 'hu', 'gof', 'h', 'g@gmail.com', 123, 21)
session.add(user)
session.commit()
user1 = User(2, 'husn', 'goff', 'hu', 'go@gmail.com', 1234, 22)
user2 = User(3, 'husni', 'goffo', 'hus', 'goff@gmail.com', 12345, 23)
user3 = User(4, 'husnid', 'goffor', 'husi', 'goffor@gmail.com', 123456, 24)
user4 = User(5, 'husniddin', 'gofforov', 'husii', 'gofforov@gmail.com', 123456, 25)
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.commit()


result = session.query(User).filter(User.f_name=='husn')
for i in result:
    print(i)