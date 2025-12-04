"""
Script για εισαγωγή ερωτήσεων από το ερωτηματολόγιο στη βάση
"""
from app import app, db
from models import Question

# Ερωτήσεις Παιδιών (8-12 ετών)
child_questions = [
    # Θεματική 1: Κωδικοί Πρόσβασης
    {
        'category': 'child', 'theme': 'passwords', 'question_number': 1,
        'question_text': 'Ποιος είναι ένας καλός κωδικός;',
        'option_a': '123456', 'option_b': 'toonomamou', 'option_c': '$uperK0d1k0$',
        'correct_answer': 'c',
        'explanation': 'Ένας ισχυρός κωδικός έχει αριθμούς, σύμβολα και κεφαλαία γράμματα!',
        'difficulty': 'easy'
    },
    {
        'category': 'child', 'theme': 'passwords', 'question_number': 2,
        'question_text': 'Πρέπει να λες τον κωδικό σου στους φίλους σου;',
        'option_a': 'Ναι, αν είναι καλοί φίλοι', 
        'option_b': 'Όχι, μόνο στους γονείς ή τον δάσκαλο',
        'option_c': 'Σε όποιον μου τον ζητήσει',
        'correct_answer': 'b',
        'explanation': 'Οι κωδικοί είναι προσωπικοί - μόνο εσύ και οι γονείς σου πρέπει να τους ξέρετε!',
        'difficulty': 'easy'
    },
    {
        'category': 'child', 'theme': 'passwords', 'question_number': 3,
        'question_text': 'Είναι καλό να χρησιμοποιείς το όνομά σου για κωδικό;',
        'option_a': 'Ναι, είναι εύκολο να το θυμάμαι',
        'option_b': 'Όχι, είναι εύκολο να το μαντέψουν',
        'option_c': 'Μόνο αν προσθέσω αριθμούς',
        'correct_answer': 'b',
        'explanation': 'Το όνομά σου είναι εύκολο να το βρουν άλλοι - επίλεξε κάτι που μόνο εσύ ξέρεις!',
        'difficulty': 'easy'
    },
    {
        'category': 'child', 'theme': 'passwords', 'question_number': 4,
        'question_text': 'Τι σημαίνει «ισχυρός κωδικός»;',
        'option_a': 'Έχει μόνο γράμματα',
        'option_b': 'Έχει αριθμούς, σύμβολα και κεφαλαία',
        'option_c': 'Είναι μικρός και εύκολος',
        'correct_answer': 'b',
        'explanation': 'Ένας ισχυρός κωδικός συνδυάζει διαφορετικά στοιχεία για μέγιστη ασφάλεια!',
        'difficulty': 'medium'
    },
    
    # Θεματική 2: Phishing & ύποπτα μηνύματα
    {
        'category': 'child', 'theme': 'phishing', 'question_number': 8,
        'question_text': 'Τι είναι phishing;',
        'option_a': 'Μήνυμα για ψάρεμα',
        'option_b': 'Μήνυμα που προσπαθεί να σε ξεγελάσει',
        'option_c': 'Μήνυμα από φίλο',
        'correct_answer': 'b',
        'explanation': 'Το phishing είναι όταν κάποιος προσπαθεί να σε ξεγελάσει για να πάρει τα στοιχεία σου!',
        'difficulty': 'medium'
    },
    {
        'category': 'child', 'theme': 'phishing', 'question_number': 9,
        'question_text': 'Αν λάβεις email που λέει «Κέρδισες δώρο», τι κάνεις;',
        'option_a': 'Κάνω κλικ αμέσως',
        'option_b': 'Το δείχνω σε γονιό ή δάσκαλο',
        'option_c': 'Το αγνοώ και το διαγράφω',
        'correct_answer': 'b',
        'explanation': 'Πάντα δείχνεις τέτοια μηνύματα σε έναν ενήλικα πριν κάνεις κλικ!',
        'difficulty': 'easy'
    },
    
    # Θεματική 3: Social Media & Online Παιχνίδια
    {
        'category': 'child', 'theme': 'social_media', 'question_number': 14,
        'question_text': 'Πρέπει να δέχεσαι αιτήματα φιλίας από αγνώστους;',
        'option_a': 'Ναι',
        'option_b': 'Όχι',
        'option_c': 'Μόνο αν έχουν ωραία φωτογραφία',
        'correct_answer': 'b',
        'explanation': 'Δέξου μόνο άτομα που γνωρίζεις στην πραγματική ζωή!',
        'difficulty': 'easy'
    },
    {
        'category': 'child', 'theme': 'social_media', 'question_number': 16,
        'question_text': 'Είναι καλό να γράφεις το τηλέφωνό σου στα σχόλια;',
        'option_a': 'Ναι, αν το ζητάνε',
        'option_b': 'Όχι, ποτέ',
        'option_c': 'Μόνο στους φίλους μου',
        'correct_answer': 'b',
        'explanation': 'Το τηλέφωνό σου είναι προσωπικό στοιχείο - μην το μοιράζεσαι online!',
        'difficulty': 'easy'
    },
]

# Ερωτήσεις Ενηλίκων
adult_questions = [
    # Θεματική 1: Κωδικοί & Authentication
    {
        'category': 'adult', 'theme': 'passwords_auth', 'question_number': 1,
        'question_text': 'Πόσο συχνά αλλάζετε τους κωδικούς σας;',
        'option_a': 'Ποτέ',
        'option_b': 'Μία φορά το χρόνο',
        'option_c': 'Κάθε 3-6 μήνες',
        'correct_answer': 'c',
        'explanation': 'Η τακτική αλλαγή κωδικών κάθε 3-6 μήνες ενισχύει την ασφάλεια!',
        'difficulty': 'easy'
    },
    {
        'category': 'adult', 'theme': 'passwords_auth', 'question_number': 3,
        'question_text': 'Τι είναι Two Factor Authentication (2FA);',
        'option_a': 'Έλεγχος δύο email',
        'option_b': 'Έλεγχος με κωδικό + άλλο στοιχείο',
        'option_c': 'Δεν ξέρω',
        'correct_answer': 'b',
        'explanation': 'Το 2FA προσθέτει επιπλέον επίπεδο ασφάλειας με δεύτερο παράγοντα επαλήθευσης!',
        'difficulty': 'medium'
    },
    
    # Θεματική 2: Phishing & Scam
    {
        'category': 'adult', 'theme': 'phishing_scam', 'question_number': 6,
        'question_text': 'Τι είναι phishing;',
        'option_a': 'Μήνυμα για ψάρεμα',
        'option_b': 'Μήνυμα που προσπαθεί να κλέψει στοιχεία σας',
        'option_c': 'Ενημερωτικό email',
        'correct_answer': 'b',
        'explanation': 'Το phishing είναι απάτη που στοχεύει στην κλοπή προσωπικών δεδομένων!',
        'difficulty': 'easy'
    },
    {
        'category': 'adult', 'theme': 'phishing_scam', 'question_number': 7,
        'question_text': 'Ποιο είναι σημάδι phishing email;',
        'option_a': 'Ορθογραφικά λάθη και ύποπτος αποστολέας',
        'option_b': 'Μήνυμα από τράπεζά σας',
        'option_c': 'Μήνυμα από φίλο',
        'correct_answer': 'a',
        'explanation': 'Τα phishing emails συχνά έχουν λάθη και ύποπτες διευθύνσεις αποστολέα!',
        'difficulty': 'easy'
    },
    
    # Θεματική 6: Ψηφιακός Γραμματισμός
    {
        'category': 'adult', 'theme': 'digital_literacy', 'question_number': 21,
        'question_text': 'Όταν διαβάζετε μια είδηση online, πώς ελέγχετε αν είναι αληθινή;',
        'option_a': 'Την κοινοποιώ αν συμφωνώ',
        'option_b': 'Ελέγχω την πηγή / κάνω αναζήτηση',
        'option_c': 'Δεν με απασχολεί',
        'correct_answer': 'b',
        'explanation': 'Ο έλεγχος της πηγής και η διασταύρωση πληροφοριών είναι απαραίτητα!',
        'difficulty': 'medium'
    },
]

# Ερωτήσεις Επαγγελματιών
professional_questions = [
    # Θεματική 1: Advanced Authentication
    {
        'category': 'professional', 'theme': 'advanced_auth', 'question_number': 1,
        'question_text': 'Τι είναι MFA;',
        'option_a': 'Multi Factor Authentication',
        'option_b': 'Mail Forwarding Application',
        'option_c': 'Media File Access',
        'correct_answer': 'a',
        'explanation': 'MFA (Multi Factor Authentication) απαιτεί πολλαπλούς παράγοντες επαλήθευσης!',
        'difficulty': 'medium'
    },
    {
        'category': 'professional', 'theme': 'advanced_auth', 'question_number': 2,
        'question_text': 'Τι είναι Single Sign-On (SSO);',
        'option_a': 'Ένας κωδικός για όλα με ασφάλεια',
        'option_b': 'Password manager',
        'option_c': 'VPN',
        'correct_answer': 'a',
        'explanation': 'Το SSO επιτρέπει πρόσβαση σε πολλές εφαρμογές με μία σύνδεση!',
        'difficulty': 'medium'
    },
    
    # Θεματική 4: GDPR & Compliance
    {
        'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 16,
        'question_text': 'Τι είναι GDPR;',
        'option_a': 'Γενικός Κανονισμός Προστασίας Δεδομένων (ΕΕ)',
        'option_b': 'Τεχνολογία encryption',
        'option_c': 'Firewall πρόγραμμα',
        'correct_answer': 'a',
        'explanation': 'Το GDPR είναι ο κανονισμός της ΕΕ για την προστασία προσωπικών δεδομένων!',
        'difficulty': 'easy'
    },
    {
        'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 19,
        'question_text': 'Τι σημαίνει data breach;',
        'option_a': 'Προστασία δεδομένων',
        'option_b': 'Παραβίαση και διαρροή δεδομένων',
        'option_c': 'Backup αρχείων',
        'correct_answer': 'b',
        'explanation': 'Data breach είναι η μη εξουσιοδοτημένη πρόσβαση ή διαρροή δεδομένων!',
        'difficulty': 'easy'
    },
    
    # Θεματική 6: Advanced Practices
    {
        'category': 'professional', 'theme': 'advanced_practices', 'question_number': 26,
        'question_text': 'Τι είναι η αρχή του ελάχιστου δικαιώματος (least privilege);',
        'option_a': 'Δίνεται πρόσβαση μόνο σε ό,τι είναι απαραίτητο για το ρόλο',
        'option_b': 'Ο κάθε χρήστης έχει πλήρη πρόσβαση',
        'option_c': 'Κανείς δεν έχει πρόσβαση',
        'correct_answer': 'a',
        'explanation': 'Least privilege σημαίνει ότι κάθε χρήστης έχει μόνο τα δικαιώματα που χρειάζεται!',
        'difficulty': 'medium'
    },
]

def insert_all_questions():
    """Εισαγωγή όλων των ερωτήσεων στη βάση"""
    with app.app_context():
        # Διαγραφή παλιών ερωτήσεων (προαιρετικό)
        Question.query.delete()
        
        all_questions = child_questions + adult_questions + professional_questions
        
        for q_data in all_questions:
            question = Question(**q_data)
            db.session.add(question)
        
        db.session.commit()
        
        print(f"✅ Επιτυχής εισαγωγή {len(all_questions)} ερωτήσεων!")
        print(f"   - Παιδιά: {len(child_questions)}")
        print(f"   - Ενήλικες: {len(adult_questions)}")
        print(f"   - Επαγγελματίες: {len(professional_questions)}")

if __name__ == '__main__':
    insert_all_questions()