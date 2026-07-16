CREATE TABLE IF NOT EXISTS events
(
    id BIGSERIAL UNIQUE,

    stream_id UUID NOT NULL,

    version INTEGER NOT NULL,

    event_type TEXT NOT NULL,

    payload JSONB NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    PRIMARY KEY (stream_id, version)
);