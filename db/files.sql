CREATE SEQUENCE public.files_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.files_id_seq
  OWNER TO postgres;

  
CREATE TABLE public."files"
(
  id bigint NOT NULL DEFAULT nextval('files_id_seq'::regclass),
  group_id character varying  NOT NULL references groups(group_id),
  file_id character varying  NOT NULL UNIQUE,
  owner_email character varying NOT NULL references users(email),
  filename character varying  NOT NULL,
  file bytea,
  upload_date timestamp,
  primary key(group_id,filename)
);