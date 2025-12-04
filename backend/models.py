from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), unique=True, nullable=False)
    user_category = db.Column(db.Enum('child', 'adult', 'professional'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    demographics = db.relationship('Demographics', backref='session', lazy=True, cascade='all, delete-orphan')
    answers = db.relationship('Answer', backref='session', lazy=True, cascade='all, delete-orphan')
    result = db.relationship('Result', backref='session', uselist=False, cascade='all, delete-orphan')

class Demographics(db.Model):
    __tablename__ = 'demographics'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), db.ForeignKey('sessions.session_id'))
    gender = db.Column(db.String(50))
    age_group = db.Column(db.String(50))
    education_level = db.Column(db.String(100))
    location = db.Column(db.String(255))
    school_type = db.Column(db.String(50))
    employment_sector = db.Column(db.String(100))
    internet_frequency = db.Column(db.String(50))

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Enum('child', 'adult', 'professional'), nullable=False)
    theme = db.Column(db.String(100), nullable=False)
    question_number = db.Column(db.Integer, nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.Text, nullable=False)
    option_b = db.Column(db.Text, nullable=False)
    option_c = db.Column(db.Text)
    correct_answer = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text)
    difficulty = db.Column(db.Enum('easy', 'medium', 'hard'), default='medium')
    
    answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
    __tablename__ = 'answers'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), db.ForeignKey('sessions.session_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    user_answer = db.Column(db.String(1), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    time_spent = db.Column(db.Integer, default=0)
    answered_at = db.Column(db.DateTime, default=datetime.utcnow)

class Result(db.Model):
    __tablename__ = 'results'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), db.ForeignKey('sessions.session_id'), unique=True)
    total_questions = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False)
    total_score = db.Column(db.Numeric(5, 2), nullable=False)
    theme_scores = db.Column(db.JSON)
    performance_level = db.Column(db.Enum('beginner', 'intermediate', 'advanced', 'expert'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
      
    def to_dict(self):
        return {
            'session_id': self.session_id,
            'total_questions': self.total_questions,
            'correct_answers': self.correct_answers,
            'total_score': float(self.total_score),
            'theme_scores': self.theme_scores,
            'performance_level': self.performance_level,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

class Recommendation(db.Model):
    __tablename__ = 'recommendations'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), db.ForeignKey('sessions.session_id'))
    theme = db.Column(db.String(100), nullable=False)
    recommendation_text = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Enum('low', 'medium', 'high', 'critical'), default='medium')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'theme': self.theme,
            'text': self.recommendation_text,
            'priority': self.priority
        }

class Theme(db.Model):
    __tablename__ = 'themes'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Enum('child', 'adult', 'professional'), nullable=False)
    theme_name = db.Column(db.String(100), nullable=False)
    theme_title_gr = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))