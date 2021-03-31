from dotenv import load_dotenv
import os

load_dotenv()

#postgres database_credentials
DATABASE=os.environ['DATABASE']

USER=os.environ['USER']

PASSWORD=os.environ['PASSWORD']

HOST=os.environ['HOST']

PORT=os.environ['PORT']

