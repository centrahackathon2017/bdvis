-- Table: public.zones

-- DROP TABLE public.zones;

CREATE TABLE public.zones
(
    ogc_fid text COLLATE pg_catalog."default" NOT NULL,
	total_businesses integer,
	total_apartments integer,
	number_of_crimes integer,
    total_pop integer,
    households integer,
    male integer,
    female integer,
    white integer,
    black integer,
    ameri_es integer,
    asian integer,
    hawn_pi integer,
    other integer,
    multi_race integer,
    hispanic integer,
    age_below_18 integer,
    age_18_40 integer,
    age_40_65 integer,
    age_65 integer,
    age_median integer,
    tran_total integer,
    tran_car integer,
    tran_moto integer,
    tran_bike integer,
    tran_pub integer,
    tran_walk integer,
    tran_other integer,
    tran_home integer,
    student integer,
    less_10k integer,
    "10k_14k" integer,
    "15k_19k" integer,
    "20k_24k" integer,
    "25k_29k" integer,
    "30k_34k" integer,
    "35k_39k" integer,
    "40k_44k" integer,
    "45k_49k" integer,
    "50k_59k" integer,
    "60k_74k" integer,
    "75k_99k" integer,
    "100k_124k" integer,
    "125k_149k" integer,
    "150k_199k" integer,
    "120k_more" integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.zones
    OWNER to postgres;