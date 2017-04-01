

CREATE SEQUENCE public.group_members_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.group_members_id_seq
  OWNER TO postgres;


CREATE TABLE public."group_members"
(
  id bigint NOT NULL DEFAULT nextval('group_members_id_seq'::regclass),
  group_id character varying  NOT NULL references groups(group_id),
  user_id character varying  NOT NULL references users(user_id),
  membership_date timestamp, 
  primary key(membership_date)
);