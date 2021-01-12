Ppsql -v ON_ERROR_STOP =1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQLCREATE USER approot PASSWORD 'password'; CREATE DATABASE appdb OWNER approot;
    ALTER USER approot CREATEDB;
EOSQL
