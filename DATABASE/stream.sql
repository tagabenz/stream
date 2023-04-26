--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:SKUrDGTB3+szNEIe/LnJVg==$K1xiIr8YurH+PJVL/HjRurEac/rgNDqXlU8swVMCCKw=:EgUlL85uQTlOApkLQ9hVvli5Lt8JkpsFSI/s/AUkBqM=';

--
-- User Configurations
--

--
-- User Config "postgres"
--

ALTER ROLE postgres SET client_encoding TO 'utf8';








--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2 (Debian 15.2-1.pgdg110+1)
-- Dumped by pg_dump version 15.2 (Debian 15.2-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2 (Debian 15.2-1.pgdg110+1)
-- Dumped by pg_dump version 15.2 (Debian 15.2-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "stream_db" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2 (Debian 15.2-1.pgdg110+1)
-- Dumped by pg_dump version 15.2 (Debian 15.2-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: stream_db; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE stream_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE stream_db OWNER TO postgres;

\connect stream_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: app_users_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_users_users (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    gender character varying(1) NOT NULL,
    dob date
);


ALTER TABLE public.app_users_users OWNER TO postgres;

--
-- Name: app_users_users_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_users_users_groups (
    id bigint NOT NULL,
    users_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.app_users_users_groups OWNER TO postgres;

--
-- Name: app_users_users_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_users_users_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_users_users_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: app_users_users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_users_users ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_users_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: app_users_users_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_users_users_user_permissions (
    id bigint NOT NULL,
    users_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.app_users_users_user_permissions OWNER TO postgres;

--
-- Name: app_users_users_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_users_users_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_users_users_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: blog_blogs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blog_blogs (
    id bigint NOT NULL,
    title character varying(255),
    img character varying(100),
    content text,
    time_create timestamp with time zone,
    time_update timestamp with time zone,
    is_published boolean
);


ALTER TABLE public.blog_blogs OWNER TO postgres;

--
-- Name: blog_blogs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.blog_blogs ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.blog_blogs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: menu_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.menu_categories (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(255) NOT NULL,
    img character varying(100)
);


ALTER TABLE public.menu_categories OWNER TO postgres;

--
-- Name: menu_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.menu_categories ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.menu_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: menu_menu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.menu_menu (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    url character varying(200) NOT NULL
);


ALTER TABLE public.menu_menu OWNER TO postgres;

--
-- Name: menu_menu_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.menu_menu ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.menu_menu_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: app_users_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_users_users (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, gender, dob) FROM stdin;
3	pbkdf2_sha256$390000$SggCUupu8N4z32nqeLjzF5$CgbAwtcnwdZVGn7knuBH45Q3yGee4SxYJHAtf+qPZ0Q=	2023-04-11 12:57:30.29499+00	t	admin				t	t	2023-04-11 12:57:19.162621+00		\N
8	pbkdf2_sha256$390000$jHAsmx5NYHoq6zsQQcE1Eq$yATx9RiicQYqZHdHlijlaANyZLPiM8AJbR25uii/WyA=	2023-04-15 01:00:39.846249+00	f	tagabenz	Taga	Benz	tagabenz@gmail.com	f	t	2023-04-14 01:21:05.715782+00	М	1991-07-14
\.


--
-- Data for Name: app_users_users_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_users_users_groups (id, users_id, group_id) FROM stdin;
\.


--
-- Data for Name: app_users_users_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_users_users_user_permissions (id, users_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add blogs	6	add_blogs
22	Can change blogs	6	change_blogs
23	Can delete blogs	6	delete_blogs
24	Can view blogs	6	view_blogs
25	Can add user	7	add_users
26	Can change user	7	change_users
27	Can delete user	7	delete_users
28	Can view user	7	view_users
29	Can add Категории	8	add_categories
30	Can change Категории	8	change_categories
31	Can delete Категории	8	delete_categories
32	Can view Категории	8	view_categories
33	Can add Меню	9	add_menu
34	Can change Меню	9	change_menu
35	Can delete Меню	9	delete_menu
36	Can view Меню	9	view_menu
\.


--
-- Data for Name: blog_blogs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blog_blogs (id, title, img, content, time_create, time_update, is_published) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-04-11 23:49:53.200343+00	1	Категории	1	[{"added": {}}]	9	3
2	2023-04-11 23:50:31.572599+00	2	Блог	1	[{"added": {}}]	9	3
3	2023-04-11 23:50:41.033444+00	3	О нас	1	[{"added": {}}]	9	3
4	2023-04-11 23:51:37.145027+00	1	Категории	3		9	3
5	2023-04-11 23:51:42.714737+00	2	Блог	3		9	3
6	2023-04-11 23:51:42.716941+00	3	О нас	3		9	3
7	2023-04-11 23:53:11.582657+00	4	Категории	1	[{"added": {}}]	9	3
8	2023-04-11 23:53:26.821938+00	5	Блог	1	[{"added": {}}]	9	3
9	2023-04-11 23:53:39.494816+00	6	О нас	1	[{"added": {}}]	9	3
10	2023-04-11 23:54:18.64114+00	1	Игры	1	[{"added": {}}]	8	3
11	2023-04-11 23:54:58.28731+00	2	Общение	1	[{"added": {}}]	8	3
12	2023-04-11 23:55:12.895895+00	3	Кино	1	[{"added": {}}]	8	3
13	2023-04-12 13:08:41.599389+00	5	taga1	3		7	3
14	2023-04-12 13:08:41.60302+00	4	taga	3		7	3
15	2023-04-12 13:10:14.180374+00	6	123	3		7	3
16	2023-04-14 01:08:48.511356+00	7	123	3		7	3
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	blog	blogs
7	app_users	users
8	menu	categories
9	menu	menu
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-04-11 12:47:48.182028+00
2	contenttypes	0002_remove_content_type_name	2023-04-11 12:53:43.835016+00
3	auth	0001_initial	2023-04-11 12:53:43.8797+00
4	auth	0002_alter_permission_name_max_length	2023-04-11 12:53:43.885935+00
5	auth	0003_alter_user_email_max_length	2023-04-11 12:53:43.891444+00
6	auth	0004_alter_user_username_opts	2023-04-11 12:53:43.897534+00
7	auth	0005_alter_user_last_login_null	2023-04-11 12:53:43.905059+00
8	auth	0006_require_contenttypes_0002	2023-04-11 12:53:43.907962+00
9	auth	0007_alter_validators_add_error_messages	2023-04-11 12:53:43.914818+00
10	auth	0008_alter_user_username_max_length	2023-04-11 12:53:43.921234+00
11	auth	0009_alter_user_last_name_max_length	2023-04-11 12:53:43.926809+00
12	auth	0010_alter_group_name_max_length	2023-04-11 12:53:43.936001+00
13	auth	0011_update_proxy_permissions	2023-04-11 12:53:43.941624+00
14	auth	0012_alter_user_first_name_max_length	2023-04-11 12:53:43.947882+00
15	app_users	0001_initial	2023-04-11 12:53:43.996028+00
16	admin	0001_initial	2023-04-11 12:53:44.02469+00
17	admin	0002_logentry_remove_auto_add	2023-04-11 12:53:44.036327+00
18	admin	0003_logentry_add_action_flag_choices	2023-04-11 12:53:44.046314+00
19	blog	0001_initial	2023-04-11 12:53:44.061524+00
20	menu	0001_initial	2023-04-11 12:53:44.091969+00
21	sessions	0001_initial	2023-04-11 12:53:44.115768+00
22	app_users	0002_remove_users_dob	2023-04-11 12:57:00.686099+00
23	app_users	0003_users_dob	2023-04-11 12:58:01.754726+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
i0ssfozrtlkxxnzltha63psaqsscq58f	.eJxVjMsOwiAQRf-FtSHDFBBcuu83kGEYpGrapI-V8d-1SRe6veec-1KJtrWlbZE5DUVdVFCn3y0TP2TcQbnTeJs0T-M6D1nvij7oovupyPN6uH8HjZb2rc8Qg4ANzjNVIxA529yhNwUYLAtGsEBofKxO0JBH49CjD9R11TCp9wfI0Db5:1pn8RE:HEhKys-xsZF_9NrmxGbM332nBpQl1y0iUApDZlJ9AsE	2023-04-28 01:41:20.46102+00
\.


--
-- Data for Name: menu_categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.menu_categories (id, name, slug, img) FROM stdin;
1	Игры	games	svg/game_FdlW37J.png
2	Общение	obshenie	svg/chat_lz4rOYG.png
3	Кино	films	svg/film_70tK7j8.png
\.


--
-- Data for Name: menu_menu; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.menu_menu (id, name, url) FROM stdin;
4	Категории	/categories
5	Блог	/blog
6	О нас	/about
\.


--
-- Name: app_users_users_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_users_users_groups_id_seq', 1, false);


--
-- Name: app_users_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_users_users_id_seq', 8, true);


--
-- Name: app_users_users_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_users_users_user_permissions_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);


--
-- Name: blog_blogs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_blogs_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 16, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 23, true);


--
-- Name: menu_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.menu_categories_id_seq', 3, true);


--
-- Name: menu_menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.menu_menu_id_seq', 6, true);


--
-- Name: app_users_users_groups app_users_users_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_groups
    ADD CONSTRAINT app_users_users_groups_pkey PRIMARY KEY (id);


--
-- Name: app_users_users_groups app_users_users_groups_users_id_group_id_7ef52e76_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_groups
    ADD CONSTRAINT app_users_users_groups_users_id_group_id_7ef52e76_uniq UNIQUE (users_id, group_id);


--
-- Name: app_users_users app_users_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users
    ADD CONSTRAINT app_users_users_pkey PRIMARY KEY (id);


--
-- Name: app_users_users_user_permissions app_users_users_user_per_users_id_permission_id_2806a31c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_user_permissions
    ADD CONSTRAINT app_users_users_user_per_users_id_permission_id_2806a31c_uniq UNIQUE (users_id, permission_id);


--
-- Name: app_users_users_user_permissions app_users_users_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_user_permissions
    ADD CONSTRAINT app_users_users_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: app_users_users app_users_users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users
    ADD CONSTRAINT app_users_users_username_key UNIQUE (username);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: blog_blogs blog_blogs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blog_blogs
    ADD CONSTRAINT blog_blogs_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: menu_categories menu_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.menu_categories
    ADD CONSTRAINT menu_categories_pkey PRIMARY KEY (id);


--
-- Name: menu_categories menu_categories_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.menu_categories
    ADD CONSTRAINT menu_categories_slug_key UNIQUE (slug);


--
-- Name: menu_menu menu_menu_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.menu_menu
    ADD CONSTRAINT menu_menu_pkey PRIMARY KEY (id);


--
-- Name: app_users_users_groups_group_id_17e7c8ff; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_users_users_groups_group_id_17e7c8ff ON public.app_users_users_groups USING btree (group_id);


--
-- Name: app_users_users_groups_users_id_758074bf; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_users_users_groups_users_id_758074bf ON public.app_users_users_groups USING btree (users_id);


--
-- Name: app_users_users_user_permissions_permission_id_dc90ebc6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_users_users_user_permissions_permission_id_dc90ebc6 ON public.app_users_users_user_permissions USING btree (permission_id);


--
-- Name: app_users_users_user_permissions_users_id_7adcc6f1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_users_users_user_permissions_users_id_7adcc6f1 ON public.app_users_users_user_permissions USING btree (users_id);


--
-- Name: app_users_users_username_25e30f6d_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_users_users_username_25e30f6d_like ON public.app_users_users USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: menu_categories_name_4d6e23f6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX menu_categories_name_4d6e23f6 ON public.menu_categories USING btree (name);


--
-- Name: menu_categories_name_4d6e23f6_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX menu_categories_name_4d6e23f6_like ON public.menu_categories USING btree (name varchar_pattern_ops);


--
-- Name: menu_categories_slug_716dd0d1_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX menu_categories_slug_716dd0d1_like ON public.menu_categories USING btree (slug varchar_pattern_ops);


--
-- Name: app_users_users_groups app_users_users_groups_group_id_17e7c8ff_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_groups
    ADD CONSTRAINT app_users_users_groups_group_id_17e7c8ff_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_users_users_groups app_users_users_groups_users_id_758074bf_fk_app_users_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_groups
    ADD CONSTRAINT app_users_users_groups_users_id_758074bf_fk_app_users_users_id FOREIGN KEY (users_id) REFERENCES public.app_users_users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_users_users_user_permissions app_users_users_user_permission_id_dc90ebc6_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_user_permissions
    ADD CONSTRAINT app_users_users_user_permission_id_dc90ebc6_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_users_users_user_permissions app_users_users_user_users_id_7adcc6f1_fk_app_users; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_users_users_user_permissions
    ADD CONSTRAINT app_users_users_user_users_id_7adcc6f1_fk_app_users FOREIGN KEY (users_id) REFERENCES public.app_users_users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_app_users_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_app_users_users_id FOREIGN KEY (user_id) REFERENCES public.app_users_users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

