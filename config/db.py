from sqlalchemy import create_engine, MetaData


meta = MetaData()

# Chanche the path following the next format to connect the 
#   database with python
# 
# example:
#      'mysql+pymysql://user:password.@IP:PORT/DATABASE
path = ''
# note: the database has to be created before connecting to it

engine = create_engine(path)
conn = engine.connect()
