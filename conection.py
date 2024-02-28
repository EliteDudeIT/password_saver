from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///password_saver', echo=True)
Base = declarative_base()

Session = sessionmaker(db)
session = Session()

class Password(Base):
    __tablename__ = 'password_1'
    id = Column(BigInteger, primary_key=True)
    password = Column(String, nullable=False)

if __name__ == '__main__':
    print('start')
    Base.metadata.create_all(db)
    users = session.query(Password).all()
    for user in users:
        print(user.id, user.password)