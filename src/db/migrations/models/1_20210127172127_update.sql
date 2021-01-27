-- upgrade --
ALTER TABLE "UserAccounts_user" ALTER COLUMN "user_uuid" DROP DEFAULT;
CREATE TABLE IF NOT EXISTS "handbook_commonhardness" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "ch_type" VARCHAR(100) NOT NULL,
    "ch_slug" VARCHAR(100) NOT NULL,
    "ch_desc" TEXT
);
COMMENT ON COLUMN "handbook_commonhardness"."ch_type" IS 'Hardness';
COMMENT ON COLUMN "handbook_commonhardness"."ch_slug" IS 'Slug';
COMMENT ON COLUMN "handbook_commonhardness"."ch_desc" IS 'Description';
COMMENT ON TABLE "handbook_commonhardness" IS 'Human readable hardness';;
CREATE TABLE IF NOT EXISTS "handbook_hardnessscales" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "hs_type" VARCHAR(100) NOT NULL,
    "hs_slug" VARCHAR(100) NOT NULL,
    "hs_desc" TEXT,
    "hs_min" INT NOT NULL  DEFAULT 0,
    "hs_max" INT NOT NULL  DEFAULT 100,
    "hs_units" VARCHAR(15) NOT NULL
);
COMMENT ON COLUMN "handbook_hardnessscales"."hs_type" IS 'Hardness scale';
COMMENT ON COLUMN "handbook_hardnessscales"."hs_slug" IS 'Slug';
COMMENT ON COLUMN "handbook_hardnessscales"."hs_desc" IS 'Description';
COMMENT ON COLUMN "handbook_hardnessscales"."hs_min" IS 'Minimal value';
COMMENT ON COLUMN "handbook_hardnessscales"."hs_max" IS 'Maximum value';
COMMENT ON COLUMN "handbook_hardnessscales"."hs_units" IS 'Measurement unit';
COMMENT ON TABLE "handbook_hardnessscales" IS 'Hardness scales of materials';;
-- downgrade --
ALTER TABLE "UserAccounts_user" ALTER COLUMN "user_uuid" DROP DEFAULT;
DROP TABLE IF EXISTS "handbook_commonhardness";
DROP TABLE IF EXISTS "handbook_hardnessscales";
