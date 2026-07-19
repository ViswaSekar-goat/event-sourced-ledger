INSERT INTO events(
    stream_id,
    version,
    event_type,
    payload,
    created_at
)

VALUES (
    %s,
    %s,
    %s,
    %s,
    %s
)