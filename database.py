from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://sgub249q21bkggjsc8f7:pscale_pw_X8Jy8xTXh26hfRWcsvtt2JhHTqSo7CkpRGzvsOzd2Gd@aws.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
    'ssl':{
    'ssl_ca': "/etc/ssl/cert.pem"
    
    }
    }
)




