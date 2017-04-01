
 DROP SEQUENCE public.group_id_seq;
 drop table public.groups;

CREATE SEQUENCE public.group_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.group_id_seq
  OWNER TO postgres;


CREATE TABLE public."groups"
(
  id bigint NOT NULL DEFAULT nextval('group_id_seq'::regclass),
  group_id character varying  NOT NULL UNIQUE,
  group_name character varying  NOT NULL,
  creation_date timestamp,
  creator_email character varying NOT NULL,
  primary key(group_id)
);