def mysql_config_dev():
    mysql_config : {
    "DB_HOST" : "localhost",
    "DB_PORT" : "3306",
    "DB_NAME" : "root",
    "DB_USER" : "root",
    "DB_PWD" : "123456",
    "DB_CHARSET" : "utf8mb4",

    "DB_MAX_OPEN_CONNS" : "20",  # 连接池最大连接数
    "DB_MAX_IDLE_CONNS" : "10",  # 连接池最大空闲数
    "DB_MAX_LIFETIME_CONNS" : "7200",  # 连接池链接最长生命周期
    }
    return mysql_config


def mysql_config_prod():
    mysql_config : {
    "DB_HOST" : "localhost",
    "DB_PORT" : "3306",
    "DB_NAME" : "root",
    "DB_USER" : "root",
    "DB_PWD" : "123456",
    "DB_CHARSET" : "utf8mb4",

    "DB_MAX_OPEN_CONNS" : "20",  # 连接池最大连接数
    "DB_MAX_IDLE_CONNS" : "10",  # 连接池最大空闲数
    "DB_MAX_LIFETIME_CONNS" : "7200",  # 连接池链接最长生命周期
    }
    return mysql_config