-- Database: test

-- DROP DATABASE test;

CREATE DATABASE test
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Turkish_Turkey.1254'
       LC_CTYPE = 'Turkish_Turkey.1254'
       CONNECTION LIMIT = -1;

COMMENT ON DATABASE test
  IS 'test';
