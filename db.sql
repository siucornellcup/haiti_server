--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: clinic; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA clinic;


ALTER SCHEMA clinic OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: ethinicity; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE ethinicity AS ENUM (
    'White',
    'Black',
    'American Indian',
    'Asian Indian',
    'Chinese',
    'Filipino',
    'Other Asian',
    'Japanese',
    'Korean',
    'Vietnamese',
    'Native Hawaiian',
    'Guamanian',
    'Samoan',
    'Other Pacific Islander',
    'Other'
);


ALTER TYPE public.ethinicity OWNER TO postgres;

--
-- Name: gender; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE gender AS ENUM (
    'Female',
    'Male'
);


ALTER TYPE public.gender OWNER TO postgres;

--
-- Name: pex_condition; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE pex_condition AS ENUM (
    'Diabetic',
    'Asthmatic',
    'Peanut Allergy'
);


ALTER TYPE public.pex_condition OWNER TO postgres;

SET search_path = clinic, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: doctors; Type: TABLE; Schema: clinic; Owner: postgres; Tablespace: 
--

CREATE TABLE doctors (
    doc_id character varying(80) NOT NULL,
    name character varying(80)
);


ALTER TABLE clinic.doctors OWNER TO postgres;

--
-- Name: medical_images; Type: TABLE; Schema: clinic; Owner: postgres; Tablespace: 
--

CREATE TABLE medical_images (
    medical_image_id character varying(80) NOT NULL,
    medical_image bytea
);


ALTER TABLE clinic.medical_images OWNER TO postgres;

--
-- Name: nurses; Type: TABLE; Schema: clinic; Owner: postgres; Tablespace: 
--

CREATE TABLE nurses (
    fingerprint_hash character varying(80) NOT NULL,
    name character varying(80) NOT NULL,
    village character varying(80) NOT NULL,
    dob date NOT NULL,
    gender public.gender NOT NULL,
    id_photo bytea
);


ALTER TABLE clinic.nurses OWNER TO postgres;

--
-- Name: patients; Type: TABLE; Schema: clinic; Owner: postgres; Tablespace: 
--

CREATE TABLE patients (
    name text NOT NULL,
    dob date,
    id_photo bytea,
    village text,
    fingerprint_hash character varying(80),
    ethnicity text,
    gender public.gender,
    pex_condition public.pex_condition[]
);


ALTER TABLE clinic.patients OWNER TO postgres;

--
-- Name: resp_sounds; Type: TABLE; Schema: clinic; Owner: postgres; Tablespace: 
--

CREATE TABLE resp_sounds (
    resp_id character varying(80) NOT NULL,
    resp_sound bytea
);


ALTER TABLE clinic.resp_sounds OWNER TO postgres;

--
-- Name: visits; Type: TABLE; Schema: clinic; Owner: postgres; Tablespace: 
--

CREATE TABLE visits (
    visit_id character varying(80) NOT NULL,
    visit_date date NOT NULL,
    nurse_fingerprint character varying(80) NOT NULL,
    patient_fingerprint character varying(80) NOT NULL,
    doctor_id character varying(80),
    weight numeric,
    height numeric,
    bp_systolic integer,
    bp_diastolic integer,
    pulse_rate integer,
    resp_id character varying(80),
    blood_glucose numeric
);


ALTER TABLE clinic.visits OWNER TO postgres;

--
-- Data for Name: doctors; Type: TABLE DATA; Schema: clinic; Owner: postgres
--

COPY doctors (doc_id, name) FROM stdin;
\.


--
-- Data for Name: medical_images; Type: TABLE DATA; Schema: clinic; Owner: postgres
--

COPY medical_images (medical_image_id, medical_image) FROM stdin;
\.


--
-- Data for Name: nurses; Type: TABLE DATA; Schema: clinic; Owner: postgres
--

COPY nurses (fingerprint_hash, name, village, dob, gender, id_photo) FROM stdin;
\.


--
-- Data for Name: patients; Type: TABLE DATA; Schema: clinic; Owner: postgres
--

COPY patients (name, dob, id_photo, village, fingerprint_hash, ethnicity, gender, pex_condition) FROM stdin;
\.


--
-- Data for Name: resp_sounds; Type: TABLE DATA; Schema: clinic; Owner: postgres
--

COPY resp_sounds (resp_id, resp_sound) FROM stdin;
\.


--
-- Data for Name: visits; Type: TABLE DATA; Schema: clinic; Owner: postgres
--

COPY visits (visit_id, visit_date, nurse_fingerprint, patient_fingerprint, doctor_id, weight, height, bp_systolic, bp_diastolic, pulse_rate, resp_id, blood_glucose) FROM stdin;
\.


--
-- Name: doctors_pkey; Type: CONSTRAINT; Schema: clinic; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (doc_id);


--
-- Name: medical_images_pkey; Type: CONSTRAINT; Schema: clinic; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY medical_images
    ADD CONSTRAINT medical_images_pkey PRIMARY KEY (medical_image_id);


--
-- Name: nurses_pkey; Type: CONSTRAINT; Schema: clinic; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY nurses
    ADD CONSTRAINT nurses_pkey PRIMARY KEY (fingerprint_hash);


--
-- Name: respiratorsounds_pkey; Type: CONSTRAINT; Schema: clinic; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY resp_sounds
    ADD CONSTRAINT respiratorsounds_pkey PRIMARY KEY (resp_id);


--
-- Name: visits_pkey; Type: CONSTRAINT; Schema: clinic; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY visits
    ADD CONSTRAINT visits_pkey PRIMARY KEY (visit_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

