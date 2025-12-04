from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Session, Demographics, Question, Answer, Result, Recommendation, Theme
import uuid
from datetime import datetime
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost/cyber_quiz_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)

# ========== UTILITY FUNCTIONS ==========

def calculate_performance_level(score_percentage):
    """Determine performance level based on score"""
    if score_percentage >= 90:
        return 'expert'
    elif score_percentage >= 75:
        return 'advanced'
    elif score_percentage >= 50:
        return 'intermediate'
    else:
        return 'beginner'

def generate_recommendations(session_id, theme_scores, category):
    """Generate personalized recommendations based on weak themes"""
    recommendations_map = {
        'child': {
            'passwords': {
                'low': 'Μάθε να φτιάχνεις δυνατούς κωδικούς με γράμματα, αριθμούς και σύμβολα! 🔐',
                'high': 'Μην πεις ποτέ τον κωδικό σου σε κανέναν εκτός από γονείς! 🔑'
            },
            'phishing': {
                'low': 'Πρόσεχε τα ύποπτα μηνύματα - δείξε τα πάντα σε ενήλικα! ⚠️',
                'high': 'Μην πατάς links από αγνώστους!'
            },
            'social_media': {
                'low': 'Μην δέχεσαι φίλους που δεν γνωρίζεις στα social media! 📱',
                'high': 'Κράτα το προφίλ σου ιδιωτικό!'
            },
            'privacy': {
                'low': 'Τα προσωπικά σου δεδομένα είναι σημαντικά - μην τα μοιράζεσαι! 🛡️',
                'high': 'Ποτέ μην γράφεις τη διεύθυνσή σου online!'
            }
        },
        'adult': {
            'passwords_auth': {
                'low': 'Ενεργοποίησε Two-Factor Authentication (2FA) σε όλους τους λογαριασμούς σου! 🔐',
                'high': 'Χρησιμοποίησε Password Manager για ασφαλείς κωδικούς.'
            },
            'phishing_scam': {
                'low': 'Μάθε να αναγνωρίζεις phishing emails - έλεγξε τον αποστολέα! 🎣',
                'high': 'Ποτέ μην δίνεις προσωπικά στοιχεία μέσω email.'
            },
            'digital_literacy': {
                'low': 'Διασταύρωσε πληροφορίες από έμπιστες πηγές πριν τις κοινοποιήσεις! 📰',
                'high': 'Πρόσεχε τα fake news και τις παραπλανητικές ειδήσεις.'
            }
        },
        'professional': {
            'advanced_auth': {
                'low': 'Εφάρμοσε MFA και SSO στο εργασιακό περιβάλλον! 🔑',
                'high': 'Ενίσχυσε τα password policies με min 12 χαρακτήρες.'
            },
            'gdpr_compliance': {
                'low': 'Μελέτησε το GDPR και τις υποχρεώσεις προστασίας δεδομένων! 📋',
                'high': 'Εφάρμοσε DPIA όπου απαιτείται.'
            },
            'incident_response': {
                'low': 'Δημιούργησε Incident Response Plan για την ομάδα σου! 🚨',
                'high': 'Εκπαίδευσε την ομάδα σε security awareness.'
            }
        }
    }
    
    recommendations = []
    for theme, score in theme_scores.items():
        if score < 70:  # Weak performance
            priority = 'high' if score < 50 else 'medium'
            rec_texts = recommendations_map.get(category, {}).get(theme, {})
            rec_text = rec_texts.get('low' if score < 50 else 'high', 
                                    f'Χρειάζεται βελτίωση στο θέμα: {theme}')
            
            rec = Recommendation(
                session_id=session_id,
                theme=theme,
                recommendation_text=rec_text,
                priority=priority
            )
            db.session.add(rec)
            recommendations.append(rec)
    
    return recommendations

# ========== API ENDPOINTS ==========

@app.route('/api/start-session', methods=['POST'])
def start_session():
    """Initialize a new quiz session"""
    data = request.json
    category = data.get('category')
    
    if category not in ['child', 'adult', 'professional']:
        return jsonify({'error': 'Invalid category'}), 400
    
    session_id = str(uuid.uuid4())
    new_session = Session(session_id=session_id, user_category=category)
    
    db.session.add(new_session)
    db.session.commit()
    
    return jsonify({
        'session_id': session_id,
        'category': category,
        'message': 'Session started successfully'
    }), 201

@app.route('/api/demographics', methods=['POST'])
def save_demographics():
    """Save demographic information"""
    data = request.json
    session_id = data.get('session_id')
    
    demographics = Demographics(
        session_id=session_id,
        gender=data.get('gender'),
        age_group=data.get('age_group'),
        education_level=data.get('education_level'),
        location=data.get('location'),
        school_type=data.get('school_type'),
        employment_sector=data.get('employment_sector'),
        internet_frequency=data.get('internet_frequency')
    )
    
    db.session.add(demographics)
    db.session.commit()
    
    return jsonify({'message': 'Demographics saved'}), 201

@app.route('/api/questions/<category>', methods=['GET'])
def get_questions(category):
    """Fetch all questions for a category"""
    questions = Question.query.filter_by(category=category).all()
    
    return jsonify([{
        'id': q.id,
        'theme': q.theme,
        'question_number': q.question_number,
        'question_text': q.question_text,
        'options': {
            'a': q.option_a,
            'b': q.option_b,
            'c': q.option_c
        },
        'correct_answer': q.correct_answer,
        'explanation': q.explanation,
        'difficulty': q.difficulty
    } for q in questions]), 200

@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submit a single answer"""
    data = request.json
    
    question = Question.query.get(data['question_id'])
    is_correct = (data['user_answer'] == question.correct_answer)
    
    answer = Answer(
        session_id=data['session_id'],
        question_id=data['question_id'],
        user_answer=data['user_answer'],
        is_correct=is_correct,
        time_spent=data.get('time_spent', 0)
    )
    
    db.session.add(answer)
    db.session.commit()
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': question.correct_answer,
        'explanation': question.explanation
    }), 201

@app.route('/api/complete-quiz', methods=['POST'])
def complete_quiz():
    """Calculate final results and generate recommendations"""
    data = request.json
    session_id = data['session_id']
    
    # Get session
    session = Session.query.filter_by(session_id=session_id).first()
    session.completed_at = datetime.utcnow()
    
    # Calculate scores
    answers = Answer.query.filter_by(session_id=session_id).all()
    total_questions = len(answers)
    correct_answers = sum(1 for a in answers if a.is_correct)
    total_score = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    # Calculate theme scores
    theme_scores = {}
    for answer in answers:
        theme = answer.question.theme
        if theme not in theme_scores:
            theme_scores[theme] = {'correct': 0, 'total': 0}
        theme_scores[theme]['total'] += 1
        if answer.is_correct:
            theme_scores[theme]['correct'] += 1
    
    # Convert to percentages
    theme_percentages = {
        theme: round((scores['correct'] / scores['total'] * 100), 2)
        for theme, scores in theme_scores.items()
    }
    
    # Determine performance level
    performance = calculate_performance_level(total_score)
    
    # Save result
    result = Result(
        session_id=session_id,
        total_questions=total_questions,
        correct_answers=correct_answers,
        total_score=total_score,
        theme_scores=theme_percentages,
        performance_level=performance
    )
    
    db.session.add(result)
    
    # Generate recommendations
    recommendations = generate_recommendations(
        session_id, 
        theme_percentages, 
        session.user_category
    )
    
    db.session.commit()
    
    return jsonify({
        'result': result.to_dict(),
        'recommendations': [rec.to_dict() for rec in recommendations]
    }), 201

@app.route('/api/results/<session_id>', methods=['GET'])
def get_results(session_id):
    """Retrieve complete results for a session"""
    result = Result.query.filter_by(session_id=session_id).first()
    
    if not result:
        return jsonify({'error': 'Results not found'}), 404
    
    recommendations = Recommendation.query.filter_by(session_id=session_id).all()
    
    return jsonify({
        'result': result.to_dict(),
        'recommendations': [rec.to_dict() for rec in recommendations]
    }), 200

@app.route('/api/themes/<category>', methods=['GET'])
def get_themes(category):
    """Get all themes for a category"""
    themes = Theme.query.filter_by(category=category).all()
    
    return jsonify([{
        'theme_name': t.theme_name,
        'title': t.theme_title_gr,
        'description': t.description,
        'icon': t.icon
    } for t in themes]), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)