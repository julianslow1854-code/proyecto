from sqlalchemy import create_engine
from aqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL - os.getenv("DATABASE_URL")


engine = create_engine("DATABASE_URL")
sessionLocal = sessionmaker(bind = engine)
Base  - declarative_base()