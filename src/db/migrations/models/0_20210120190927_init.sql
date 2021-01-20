-- upgrade --
CREATE TABLE IF NOT EXISTS "handbook_persontype" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "person_type" VARCHAR(100) NOT NULL  /* User type */,
    "person_slug" VARCHAR(100) NOT NULL  /* Identifier */,
    "person_desc" TEXT   /* Description */
) /* User type */;
CREATE TABLE IF NOT EXISTS "UserAccounts_user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "user_uuid" CHAR(36) NOT NULL UNIQUE,
    "username" VARCHAR(30) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "is_active" INT NOT NULL  DEFAULT 1,
    "is_superuser" INT NOT NULL  DEFAULT 0,
    "is_verified" INT NOT NULL  DEFAULT 0,
    "first_name" VARCHAR(100) NOT NULL,
    "last_name" VARCHAR(150) NOT NULL,
    "middle_name" VARCHAR(100),
    "phone" VARCHAR(15) NOT NULL,
    "address" TEXT,
    "is_staff" INT NOT NULL  DEFAULT 0,
    "is_legal_person" INT NOT NULL  DEFAULT 0,
    "last_login" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "date_joined" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "avatar" VARCHAR(255),
    "role_id" INT NOT NULL  DEFAULT 4 REFERENCES "handbook_persontype" ("id") ON DELETE CASCADE
) /* User */;
CREATE INDEX IF NOT EXISTS "idx_UserAccount_user_uu_c8d546" ON "UserAccounts_user" ("user_uuid");
CREATE INDEX IF NOT EXISTS "idx_UserAccount_usernam_fb3b81" ON "UserAccounts_user" ("username");
CREATE INDEX IF NOT EXISTS "idx_UserAccount_email_23b168" ON "UserAccounts_user" ("email");
CREATE TABLE IF NOT EXISTS "verification" (
    "link" CHAR(36) NOT NULL  PRIMARY KEY,
    "user_id" INT NOT NULL REFERENCES "UserAccounts_user" ("id") ON DELETE CASCADE
) /* Модель для подтверждения регистрации пользователя  */;
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL
);
