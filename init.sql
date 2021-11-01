CREATE TABLE reminders (
    guild_id        BIGINT NOT NULL,
    author_id       BIGINT NOT NULL,
    course          VARCHAR NOT NULL,
    homework        VARCHAR NOT NULL,
    due_date        TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE TABLE group_members (
    guild_id        BIGINT NOT NULL,
    group_num       INTEGER NOT NULL,
    member_name     VARCHAR NOT NULL
);

CREATE TABLE project_groups (
    guild_id        BIGINT NOT NULL,
    project_num     INTEGER NOT NULL,
    group_num       INTEGER NOT NULL
);

CREATE TABLE name_mapping (
    guild_id        BIGINT NOT NULL,
    username        VARCHAR NOT NULL,
    real_name       VARCHAR NOT NULL
);

CREATE TABLE pinned_messages (
    guild_id        BIGINT NOT NULL,
    author_id       BIGINT NOT NULL,
    tag             VARCHAR NOT NULL,
    description     VARCHAR NOT NULL,
    link            VARCHAR NOT NULL
);

CREATE TABLE questions (
    guild_id        BIGINT NOT NULL,
    number          BIGINT NOT NULL,
    question        VARCHAR NOT NULL,
    author_id       BIGINT,
    msg_id          BIGINT NOT NULL
);

CREATE TABLE answers (
    guild_id        BIGINT NOT NULL,
    q_number        BIGINT NOT NULL,
    answer          VARCHAR NOT NULL,
    author_id       BIGINT,
    author_role     VARCHAR NOT NULL
)