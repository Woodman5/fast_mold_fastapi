-- upgrade --
CREATE TABLE IF NOT EXISTS "UserAccounts_persontype" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "person_type" VARCHAR(100) NOT NULL,
    "person_slug" VARCHAR(100) NOT NULL,
    "person_desc" TEXT
);
COMMENT ON COLUMN "UserAccounts_persontype"."person_type" IS 'User type';
COMMENT ON COLUMN "UserAccounts_persontype"."person_slug" IS 'Identifier';
COMMENT ON COLUMN "UserAccounts_persontype"."person_desc" IS 'Description';
COMMENT ON TABLE "UserAccounts_persontype" IS 'User type';
CREATE TABLE IF NOT EXISTS "UserAccounts_user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user_uuid" UUID NOT NULL UNIQUE,
    "username" VARCHAR(30) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "is_verified" BOOL NOT NULL  DEFAULT False,
    "first_name" VARCHAR(100) NOT NULL,
    "last_name" VARCHAR(150) NOT NULL,
    "middle_name" VARCHAR(100),
    "phone" VARCHAR(15) NOT NULL,
    "address" TEXT,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_legal_person" BOOL NOT NULL  DEFAULT False,
    "last_login" TIMESTAMPTZ,
    "date_joined" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "avatar" VARCHAR(255),
    "role_id" INT NOT NULL  DEFAULT 4 REFERENCES "UserAccounts_persontype" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_UserAccount_user_uu_c8d546" ON "UserAccounts_user" ("user_uuid");
CREATE INDEX IF NOT EXISTS "idx_UserAccount_usernam_fb3b81" ON "UserAccounts_user" ("username");
CREATE INDEX IF NOT EXISTS "idx_UserAccount_email_23b168" ON "UserAccounts_user" ("email");
COMMENT ON TABLE "UserAccounts_user" IS 'User';
CREATE TABLE IF NOT EXISTS "verification" (
    "link" UUID NOT NULL  PRIMARY KEY,
    "user_id" INT NOT NULL REFERENCES "UserAccounts_user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "verification" IS 'Модель для подтверждения регистрации пользователя ';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL
);
