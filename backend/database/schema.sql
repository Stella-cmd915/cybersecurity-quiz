-- Cyber Quiz Database Schema
CREATE DATABASE IF NOT EXISTS cyber_quiz_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE cyber_quiz_db;

-- 1. Sessions Table (Anonymous users)
CREATE TABLE sessions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(255) UNIQUE NOT NULL,
    user_category ENUM('child', 'adult', 'professional') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL,
    INDEX idx_session (session_id)
) ENGINE=InnoDB;

-- 2. Demographics Table
CREATE TABLE demographics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(255) NOT NULL,
    gender VARCHAR(50),
    age_group VARCHAR(50),
    education_level VARCHAR(100),
    location VARCHAR(255),
    school_type VARCHAR(50),
    employment_sector VARCHAR(100),
    internet_frequency VARCHAR(50),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 3. Questions Table
CREATE TABLE questions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category ENUM('child', 'adult', 'professional') NOT NULL,
    theme VARCHAR(100) NOT NULL,
    question_number INT NOT NULL,
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT,
    correct_answer CHAR(1) NOT NULL,
    explanation TEXT,
    difficulty ENUM('easy', 'medium', 'hard') DEFAULT 'medium',
    INDEX idx_category_theme (category, theme)
) ENGINE=InnoDB;

-- 4. Answers Table
CREATE TABLE answers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(255) NOT NULL,
    question_id INT NOT NULL,
    user_answer CHAR(1) NOT NULL,
    is_correct BOOLEAN NOT NULL,
    time_spent INT DEFAULT 0,
    answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,
    INDEX idx_session_answers (session_id)
) ENGINE=InnoDB;

-- 5. Results Table
CREATE TABLE results (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(255) UNIQUE NOT NULL,
    total_questions INT NOT NULL,
    correct_answers INT NOT NULL,
    total_score DECIMAL(5,2) NOT NULL,
    theme_scores JSON,
    performance_level ENUM('beginner', 'intermediate', 'advanced', 'expert') NOT NULL,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 6. Recommendations Table
CREATE TABLE recommendations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(255) NOT NULL,
    theme VARCHAR(100) NOT NULL,
    recommendation_text TEXT NOT NULL,
    priority ENUM('low', 'medium', 'high', 'critical') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 7. Themes Table (for reference)
CREATE TABLE themes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category ENUM('child', 'adult', 'professional') NOT NULL,
    theme_name VARCHAR(100) NOT NULL,
    theme_title_gr TEXT NOT NULL,
    description TEXT,
    icon VARCHAR(50),
    UNIQUE KEY unique_category_theme (category, theme_name)
) ENGINE=InnoDB;

-- Insert Themes
INSERT INTO themes (category, theme_name, theme_title_gr, description, icon) VALUES
-- Child themes
('child', 'passwords', 'Κωδικοί Πρόσβασης', 'Μαθαίνω να φτιάχνω ασφαλείς κωδικούς', '🔐'),
('child', 'phishing', 'Phishing & Ύποπτα Μηνύματα', 'Αναγνωρίζω επικίνδυνα μηνύματα', '🎣'),
('child', 'social_media', 'Social Media & Παιχνίδια', 'Ασφαλής συμπεριφορά online', '📱'),
('child', 'privacy', 'Προστασία Προσωπικών Δεδομένων', 'Τι είναι τα προσωπικά μου δεδομένα', '🛡️'),
('child', 'safe_browsing', 'Ασφαλής Περιήγηση', 'Πώς περιηγούμαι με ασφάλεια', '🌐'),
('child', 'online_behavior', 'Online Συμπεριφορά & AI', 'Ευγενική συμπεριφορά στο διαδίκτυο', '🤝'),
('child', 'influencers', 'Επιρροή από YouTubers & TikTokers', 'Κριτική σκέψη στα social media', '⭐'),

-- Adult themes
('adult', 'passwords_auth', 'Κωδικοί & Authentication', 'Διαχείριση κωδικών & 2FA', '🔑'),
('adult', 'phishing_scam', 'Phishing & Scam Detection', 'Αναγνώριση απατών online', '⚠️'),
('adult', 'social_privacy', 'Social Media Privacy', 'Ρυθμίσεις απορρήτου', '🔒'),
('adult', 'online_banking', 'Online Banking & E-commerce', 'Ασφαλείς συναλλαγές', '💳'),
('adult', 'network_security', 'Device & Network Security', 'VPN, Updates, Antivirus', '🛡️'),
('adult', 'digital_literacy', 'Ψηφιακός Γραμματισμός', 'Αναγνώριση fake news', '📰'),

-- Professional themes
('professional', 'advanced_auth', 'Advanced Authentication', 'MFA, SSO, Password Policies', '🔐'),
('professional', 'social_engineering', 'Phishing & Social Engineering', 'Spear phishing, εταιρικές απειλές', '🎯'),
('professional', 'cloud_network', 'Cloud & Network Security', 'VPN, Firewall, Zero Trust', '☁️'),
('professional', 'gdpr_compliance', 'GDPR & Data Compliance', 'Προστασία δεδομένων, DPIA', '📋'),
('professional', 'incident_response', 'Incident Response & Management', 'Security incidents, SIEM', '🚨'),
('professional', 'advanced_practices', 'Advanced Security Practices', 'Least privilege, BYOD, Honeypots', '⚙️');