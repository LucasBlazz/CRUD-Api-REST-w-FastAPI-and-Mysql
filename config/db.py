from sqlalchemy import create_engine, MetaData


meta = MetaData()

engine = create_engine('mysql+pymysql://root:L42904361r.@localhost:3306/storedb')
conn = engine.connect()
