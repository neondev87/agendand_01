-- ======================================================
--  SCHEMA COMPLETO PARA AGENDA / EVENTOS / MARCAPASOS
-- ======================================================

-- ==========================
--  TABLA DE USUARIOS
-- ==========================
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(200) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices importantes
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);


-- ==========================
--  TABLA DE EVENTOS (MARCAPASOS)
-- ==========================
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- tipo de evento (UI_update, DB_write, login_success, error, etc)
    event_type VARCHAR(50) NOT NULL,

    -- quién generó el evento (puede ser NULL, ej: sistema)
    user_id INT NULL,

    -- payload del evento (JSON o texto)
    details TEXT,

    -- timestamp automático
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_events_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Índices para velocidad
CREATE INDEX idx_events_user_id ON events(user_id);
CREATE INDEX idx_events_type ON events(event_type);
CREATE INDEX idx_events_created_at ON events(created_at);


-- ==========================
--  TABLA DE EVENT LOG (opcional y recomendada)
-- ==========================
CREATE TABLE IF NOT EXISTS event_log (
    id INT AUTO_INCREMENT PRIMARY KEY,

    source VARCHAR(40) NOT NULL,        -- UI, DB, APP, SYSTEM
    action VARCHAR(100) NOT NULL,       -- login, insert_user, ui_refresh, error, etc
    message TEXT NULL,                  -- detalles
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_event_log_source ON event_log(source);
CREATE INDEX idx_event_log_action ON event_log(action);
