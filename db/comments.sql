CREATE SEQUENCE public.comments_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.comments_id_seq
  OWNER TO postgres;

  
CREATE TABLE public."comments"
(
  id bigint NOT NULL DEFAULT nextval('comments_id_seq'::regclass),
  owner_email character varying NOT NULL references users(email),
  file_id character varying  NOT NULL references files(file_id),
  comment character varying  NOT NULL,
  comment_date timestamp,
  primary key(id)
);