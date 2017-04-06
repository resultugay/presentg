navbar = https://getbootstrap.com/components/#navbar-default
Login-Register form = http://bootsnipp.com/snippets/featured/custom-login-registration-amp-forgot-password


-- Sequence: public.user_id_seq

 DROP SEQUENCE public.user_id_seq;
 drop table public.users;

CREATE SEQUENCE public.user_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.user_id_seq
  OWNER TO postgres;


CREATE TABLE public."users"
(
  id bigint NOT NULL DEFAULT nextval('user_id_seq'::regclass),
  username character varying  NOT NULL,
  email character varying NOT NULL UNIQUE,
  name character varying  NOT NULL,
  surname character varying  NOT NULL,
  password character varying  NOT NULL,
  user_id character varying  NOT NULL UNIQUE,
  gender "char"  NOT NULL,
  reg_date timestamp,
  primary key(user_id)
);