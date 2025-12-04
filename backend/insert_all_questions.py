"""
Complete Questions Import Script
Εισάγει ΟΛΕΣ τις ερωτήσεις από το ερωτηματολόγιο (110 συνολικά)
- Παιδιά: 45 ερωτήσεις
- Ενήλικες: 30 ερωτήσεις  
- Επαγγελματίες: 35 ερωτήσεις
"""
from app import app, db
from models import Question

# ============================================
# ΠΑΙΔΙΑ (8-12 ΕΤΩΝ) - 45 ΕΡΩΤΗΣΕΙΣ
# ============================================

child_questions = [
    # Θεματική 1: Κωδικοί Πρόσβασης (7 ερωτήσεις)
    {'category': 'child', 'theme': 'passwords', 'question_number': 1,
     'question_text': 'Ποιος είναι ένας καλός κωδικός;',
     'option_a': '123456', 'option_b': 'toonomamou', 'option_c': '$uperK0d1k0$',
     'correct_answer': 'c', 'explanation': 'Ένας ισχυρός κωδικός έχει αριθμούς, σύμβολα και κεφαλαία!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'passwords', 'question_number': 2,
     'question_text': 'Πρέπει να λες τον κωδικό σου στους φίλους σου;',
     'option_a': 'Ναι, αν είναι καλοί φίλοι', 'option_b': 'Όχι, μόνο στους γονείς ή τον δάσκαλο', 'option_c': 'Σε όποιον μου τον ζητήσει',
     'correct_answer': 'b', 'explanation': 'Οι κωδικοί είναι προσωπικοί - μόνο εσύ και οι γονείς σου!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'passwords', 'question_number': 3,
     'question_text': 'Είναι καλό να χρησιμοποιείς το όνομά σου για κωδικό;',
     'option_a': 'Ναι, είναι εύκολο να το θυμάμαι', 'option_b': 'Όχι, είναι εύκολο να το μαντέψουν', 'option_c': 'Μόνο αν προσθέσω αριθμούς',
     'correct_answer': 'b', 'explanation': 'Το όνομά σου είναι εύκολο να το βρουν άλλοι!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'passwords', 'question_number': 4,
     'question_text': 'Τι σημαίνει «ισχυρός κωδικός»;',
     'option_a': 'Έχει μόνο γράμματα', 'option_b': 'Έχει αριθμούς, σύμβολα και κεφαλαία', 'option_c': 'Είναι μικρός και εύκολος',
     'correct_answer': 'b', 'explanation': 'Ένας ισχυρός κωδικός συνδυάζει διαφορετικά στοιχεία!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'passwords', 'question_number': 5,
     'question_text': 'Πόσο συχνά πρέπει να αλλάζουμε τους κωδικούς μας;',
     'option_a': 'Ποτέ', 'option_b': 'Κάθε μέρα', 'option_c': 'Ανά μερικούς μήνες',
     'correct_answer': 'c', 'explanation': 'Είναι καλό να αλλάζουμε τους κωδικούς κάθε λίγους μήνες!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'passwords', 'question_number': 6,
     'question_text': 'Αν κάποιος μάθει τον κωδικό σου, τι πρέπει να κάνεις;',
     'option_a': 'Να τον αλλάξεις αμέσως', 'option_b': 'Να τον αφήσεις ίδιο', 'option_c': 'Να ρωτήσεις τον φίλο αν θα τον πει αλλού',
     'correct_answer': 'a', 'explanation': 'Άμεση αλλαγή κωδικού για την ασφάλειά σου!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'passwords', 'question_number': 7,
     'question_text': 'Είναι καλό να χρησιμοποιείς τον ίδιο κωδικό παντού;',
     'option_a': 'Ναι, για να μην τον ξεχνάω', 'option_b': 'Όχι, γιατί είναι επικίνδυνο', 'option_c': 'Μόνο σε παιχνίδια',
     'correct_answer': 'b', 'explanation': 'Διαφορετικοί κωδικοί για κάθε λογαριασμό είναι πιο ασφαλείς!', 'difficulty': 'medium'},

    # Θεματική 2: Phishing (6 ερωτήσεις)
    {'category': 'child', 'theme': 'phishing', 'question_number': 8,
     'question_text': 'Τι είναι phishing;',
     'option_a': 'Μήνυμα για ψάρεμα', 'option_b': 'Μήνυμα που προσπαθεί να σε ξεγελάσει', 'option_c': 'Μήνυμα από φίλο',
     'correct_answer': 'b', 'explanation': 'Το phishing είναι απάτη για να πάρουν τα στοιχεία σου!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'phishing', 'question_number': 9,
     'question_text': 'Αν λάβεις email που λέει «Κέρδισες δώρο», τι κάνεις;',
     'option_a': 'Κάνω κλικ αμέσως', 'option_b': 'Το δείχνω σε γονιό ή δάσκαλο', 'option_c': 'Το αγνοώ και το διαγράφω',
     'correct_answer': 'b', 'explanation': 'Πάντα δείχνε τέτοια μηνύματα σε έναν ενήλικα!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'phishing', 'question_number': 10,
     'question_text': 'Μπορεί ένα phishing μήνυμα να μοιάζει αληθινό;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Δεν ξέρω',
     'correct_answer': 'a', 'explanation': 'Τα phishing μηνύματα προσπαθούν να μοιάσουν αληθινά!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'phishing', 'question_number': 11,
     'question_text': 'Αν ένα μήνυμα ζητά τους κωδικούς σου;',
     'option_a': 'Τους δίνω', 'option_b': 'Δεν τους δίνω ποτέ', 'option_c': 'Μόνο αν γράφει ότι είναι από το σχολείο',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην δίνεις κωδικούς μέσω μηνυμάτων!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'phishing', 'question_number': 12,
     'question_text': 'Ποιο είναι σημάδι phishing;',
     'option_a': 'Ορθογραφικά λάθη και περίεργο email αποστολέα', 'option_b': 'Μήνυμα από συμμαθητή', 'option_c': 'Μήνυμα από τη δασκάλα',
     'correct_answer': 'a', 'explanation': 'Λάθη και ύποπτες διευθύνσεις είναι σημάδια phishing!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'phishing', 'question_number': 13,
     'question_text': 'Αν σου στείλουν μήνυμα με link, τι κάνεις;',
     'option_a': 'Το ανοίγω κατευθείαν', 'option_b': 'Το δείχνω σε ενήλικα', 'option_c': 'Το στέλνω σε φίλους',
     'correct_answer': 'b', 'explanation': 'Πάντα ζήτα βοήθεια από ενήλικα πριν κάνεις κλικ!', 'difficulty': 'easy'},

    # Θεματική 3: Social Media (7 ερωτήσεις)
    {'category': 'child', 'theme': 'social_media', 'question_number': 14,
     'question_text': 'Πρέπει να δέχεσαι αιτήματα φιλίας από αγνώστους;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Μόνο αν έχουν ωραία φωτογραφία',
     'correct_answer': 'b', 'explanation': 'Δέξου μόνο άτομα που γνωρίζεις!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'social_media', 'question_number': 15,
     'question_text': 'Ποιος μπορεί να δει τις φωτογραφίες σου στο προφίλ;',
     'option_a': 'Μόνο εγώ', 'option_b': 'Όλοι αν είναι δημόσιο', 'option_c': 'Μόνο οι φίλοι μου',
     'correct_answer': 'b', 'explanation': 'Αν το προφίλ είναι δημόσιο, όλοι μπορούν να δουν!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'social_media', 'question_number': 16,
     'question_text': 'Είναι καλό να γράφεις το τηλέφωνό σου στα σχόλια;',
     'option_a': 'Ναι, αν το ζητάνε', 'option_b': 'Όχι, ποτέ', 'option_c': 'Μόνο στους φίλους μου',
     'correct_answer': 'b', 'explanation': 'Το τηλέφωνό σου είναι προσωπικό - μην το μοιράζεσαι!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'social_media', 'question_number': 17,
     'question_text': 'Πρέπει να ανεβάζεις φωτογραφίες αγνώστων;',
     'option_a': 'Ναι, αν είναι ωραίες', 'option_b': 'Όχι', 'option_c': 'Μόνο αν τους ρωτήσω',
     'correct_answer': 'c', 'explanation': 'Πάντα ζήτα άδεια πριν ανεβάσεις φωτογραφία κάποιου!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'social_media', 'question_number': 18,
     'question_text': 'Αν κάποιος σου ζητήσει τη διεύθυνσή σου;',
     'option_a': 'Την δίνω', 'option_b': 'Δεν την δίνω ποτέ', 'option_c': 'Την λέω μόνο αν είναι φίλος',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην δίνεις τη διεύθυνσή σου online!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'social_media', 'question_number': 19,
     'question_text': 'Αν ένας φίλος online σου ζητήσει να συναντηθείτε μόνοι σας;',
     'option_a': 'Πηγαίνω', 'option_b': 'Δεν πάω ποτέ χωρίς να το πω στους γονείς μου', 'option_c': 'Πηγαίνω αν είναι κοντά',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην πας σε συνάντηση χωρίς να το πεις στους γονείς!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'social_media', 'question_number': 20,
     'question_text': 'Τι πρέπει να προσέχεις όταν ανεβάζεις φωτογραφία;',
     'option_a': 'Αν φαίνεται το σπίτι σου ή η τοποθεσία σου', 'option_b': 'Αν είναι καθαρή', 'option_c': 'Αν είναι ωραία',
     'correct_answer': 'a', 'explanation': 'Μην αποκαλύπτεις την τοποθεσία σου!', 'difficulty': 'medium'},

    # Θεματική 4: Privacy (5 ερωτήσεις)
    {'category': 'child', 'theme': 'privacy', 'question_number': 21,
     'question_text': 'Ποια είναι προσωπικά δεδομένα;',
     'option_a': 'Το όνομά σου', 'option_b': 'Το αγαπημένο σου χρώμα', 'option_c': 'Το ύψος σου',
     'correct_answer': 'a', 'explanation': 'Το όνομά σου είναι προσωπικό δεδομένο!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'privacy', 'question_number': 22,
     'question_text': 'Γιατί πρέπει να προστατεύεις τα προσωπικά σου δεδομένα;',
     'option_a': 'Γιατί είναι βαρετό', 'option_b': 'Για να μην τα χρησιμοποιήσουν χωρίς άδεια', 'option_c': 'Δεν πειράζει',
     'correct_answer': 'b', 'explanation': 'Τα δεδομένα σου μπορεί να χρησιμοποιηθούν για κακό!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'privacy', 'question_number': 23,
     'question_text': 'Είναι ασφαλές να γράφεις τον αριθμό της κάρτας σου online;',
     'option_a': 'Ναι, αν το site είναι ωραίο', 'option_b': 'Όχι, ποτέ χωρίς γονείς', 'option_c': 'Ναι, αν μου το ζητήσουν',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην βάζεις στοιχεία κάρτας χωρίς γονέα!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'privacy', 'question_number': 24,
     'question_text': 'Πρέπει να γράφεις το σχολείο σου online;',
     'option_a': 'Ναι, είναι ωραίο', 'option_b': 'Όχι, εκτός αν είναι απαραίτητο', 'option_c': 'Μόνο στους φίλους',
     'correct_answer': 'b', 'explanation': 'Μην μοιράζεσαι πληροφορίες για το σχολείο σου!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'privacy', 'question_number': 25,
     'question_text': 'Αν δώσεις πολλά προσωπικά σου στοιχεία online, τι μπορεί να γίνει;',
     'option_a': 'Να τα χρησιμοποιήσουν για κακό', 'option_b': 'Τίποτα', 'option_c': 'Να σου στείλουν δώρα',
     'correct_answer': 'a', 'explanation': 'Τα προσωπικά δεδομένα μπορεί να χρησιμοποιηθούν εναντίον σου!', 'difficulty': 'medium'},

    # Θεματική 5: Safe Browsing (6 ερωτήσεις)
    {'category': 'child', 'theme': 'safe_browsing', 'question_number': 26,
     'question_text': 'Τι σημαίνει το λουκετάκι στη γραμμή διεύθυνσης;',
     'option_a': 'Ότι είναι κλειδωμένη η οθόνη', 'option_b': 'Ότι η ιστοσελίδα είναι ασφαλής', 'option_c': 'Ότι χρειάζεται κωδικός',
     'correct_answer': 'b', 'explanation': 'Το λουκετάκι σημαίνει ασφαλή σύνδεση!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'safe_browsing', 'question_number': 27,
     'question_text': 'Είναι ασφαλές να κατεβάζεις apps από άγνωστα sites;',
     'option_a': 'Ναι, αν είναι δωρεάν', 'option_b': 'Όχι, μπορεί να έχουν ιούς', 'option_c': 'Μόνο αν τα θέλω πολύ',
     'correct_answer': 'b', 'explanation': 'Κατέβαζε apps μόνο από επίσημα καταστήματα!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'safe_browsing', 'question_number': 28,
     'question_text': 'Τι είναι το antivirus;',
     'option_a': 'Παιχνίδι', 'option_b': 'Πρόγραμμα προστασίας από ιούς', 'option_c': 'Κωδικός',
     'correct_answer': 'b', 'explanation': 'Το antivirus προστατεύει από ιούς!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'safe_browsing', 'question_number': 29,
     'question_text': 'Γιατί πρέπει να ενημερώνεις τις εφαρμογές σου;',
     'option_a': 'Για να μην βαριούνται', 'option_b': 'Για να λειτουργούν σωστά και με ασφάλεια', 'option_c': 'Για να αλλάζει το χρώμα',
     'correct_answer': 'b', 'explanation': 'Οι ενημερώσεις διορθώνουν προβλήματα ασφαλείας!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'safe_browsing', 'question_number': 30,
     'question_text': 'Τι πρέπει να κοιτάς πριν κατεβάσεις μια εφαρμογή;',
     'option_a': 'Αν την έχει ο φίλος σου', 'option_b': 'Αν έχει καλές κριτικές και είναι από επίσημο κατάστημα', 'option_c': 'Αν είναι δωρεάν',
     'correct_answer': 'b', 'explanation': 'Έλεγξε τις κριτικές και βεβαιώσου ότι είναι από αξιόπιστη πηγή!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'safe_browsing', 'question_number': 31,
     'question_text': 'Είναι καλό να πατάς διαφημίσεις που υπόσχονται δώρα;',
     'option_a': 'Ναι, μπορεί να κερδίσεις', 'option_b': 'Όχι, μπορεί να είναι παγίδα', 'option_c': 'Μόνο αν φαίνονται αληθινές',
     'correct_answer': 'b', 'explanation': 'Οι περισσότερες τέτοιες διαφημίσεις είναι απάτες!', 'difficulty': 'easy'},

    # Θεματική 6: Online Behavior (4 ερωτήσεις)
    {'category': 'child', 'theme': 'online_behavior', 'question_number': 32,
     'question_text': 'Πρέπει να φερόμαστε ευγενικά online;',
     'option_a': 'Ναι, όπως και στη ζωή', 'option_b': 'Όχι, γιατί δεν με βλέπουν', 'option_c': 'Μόνο αν είναι φίλοι',
     'correct_answer': 'a', 'explanation': 'Η ευγένεια είναι σημαντική παντού!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'online_behavior', 'question_number': 33,
     'question_text': 'Αν δεις κάποιον να κοροϊδεύει άλλους online, τι κάνεις;',
     'option_a': 'Το λες σε ενήλικα', 'option_b': 'Γελάς μαζί του', 'option_c': 'Δεν κάνεις τίποτα',
     'correct_answer': 'a', 'explanation': 'Πρέπει να αναφέρεις το cyberbullying!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'online_behavior', 'question_number': 34,
     'question_text': 'Τι μπορεί να κάνει η Τεχνητή Νοημοσύνη (AI);',
     'option_a': 'Να σε προστατέψει online', 'option_b': 'Να σου γράφει τις εργασίες', 'option_c': 'Και τα δύο',
     'correct_answer': 'c', 'explanation': 'Η AI μπορεί να κάνει πολλά - και καλά και κακά!', 'difficulty': 'hard'},
    
    {'category': 'child', 'theme': 'online_behavior', 'question_number': 35,
     'question_text': 'Μπορεί η AI να κάνει και λάθη;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Δεν ξέρω',
     'correct_answer': 'a', 'explanation': 'Η AI δεν είναι τέλεια - μπορεί να κάνει λάθη!', 'difficulty': 'medium'},

    # Θεματική 7: Influencers (10 ερωτήσεις)
    {'category': 'child', 'theme': 'influencers', 'question_number': 36,
     'question_text': 'Αν ο αγαπημένος σου YouTuber σου πει να αγοράσεις κάτι, τι κάνεις;',
     'option_a': 'Το αγοράζω γιατί μου αρέσει', 'option_b': 'Το λέω στους γονείς μου', 'option_c': 'Το σκέφτομαι πρώτα αν το χρειάζομαι',
     'correct_answer': 'c', 'explanation': 'Σκέψου πάντα αν πραγματικά χρειάζεσαι κάτι πριν το αγοράσεις!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 37,
     'question_text': 'Πιστεύεις ότι οι influencers λένε πάντα την αλήθεια;',
     'option_a': 'Ναι, γιατί τους εμπιστεύομαι', 'option_b': 'Όχι πάντα -- μπορεί να πληρώνονται', 'option_c': 'Δεν ξέρω',
     'correct_answer': 'b', 'explanation': 'Οι influencers συχνά πληρώνονται για να προωθήσουν προϊόντα!', 'difficulty': 'hard'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 38,
     'question_text': 'Αν κάποιος online σε πείσει να κάνεις κάτι που δεν θέλεις;',
     'option_a': 'Το κάνω για να μην τον στενοχωρήσω', 'option_b': 'Το λέω σε έναν ενήλικα', 'option_c': 'Το κρατάω μυστικό',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην κάνεις κάτι που δεν θέλεις - μίλησε σε ενήλικα!', 'difficulty': 'easy'},

    {'category': 'child', 'theme': 'influencers', 'question_number': 39,
     'question_text': 'Όταν βλέπεις διαφημίσεις μέσα στα βίντεο ή στα παιχνίδια, τι κάνεις;',
     'option_a': 'Τις παρακολουθώ', 'option_b': 'Τις αγνοώ', 'option_c': 'Ρωτάω τους γονείς μου',
     'correct_answer': 'c', 'explanation': 'Είναι καλό να ρωτάς τους γονείς για διαφημίσεις!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 40,
     'question_text': 'Σου έχει τύχει να επηρεαστείς από YouTuber/TikToker;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Δεν θυμάμαι',
     'correct_answer': 'a', 'explanation': 'Είναι φυσιολογικό - αλλά πρέπει να σκεφτόμαστε κριτικά!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 41,
     'question_text': 'Πόσο χρόνο περνάς βλέποντας βίντεο κάθε μέρα;',
     'option_a': 'Λιγότερο από 1 ώρα', 'option_b': '1-2 ώρες', 'option_c': 'Πάνω από 2 ώρες',
     'correct_answer': 'a', 'explanation': 'Είναι καλό να περιορίζουμε τον χρόνο μας online!', 'difficulty': 'medium'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 42,
     'question_text': 'Πιστεύεις ότι οι φίλοι σου επηρεάζονται από influencers;',
     'option_a': 'Ναι, πολύ', 'option_b': 'Λίγο', 'option_c': 'Καθόλου',
     'correct_answer': 'a', 'explanation': 'Οι περισσότεροι επηρεαζόμαστε από influencers!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 43,
     'question_text': 'Ξέρεις πότε μια διαφήμιση είναι κρυφή;',
     'option_a': 'Ναι, καταλαβαίνω', 'option_b': 'Όχι', 'option_c': 'Μερικές φορές',
     'correct_answer': 'c', 'explanation': 'Οι κρυφές διαφημίσεις είναι δύσκολο να εντοπιστούν!', 'difficulty': 'hard'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 44,
     'question_text': 'Έχεις προσπαθήσει να κάνεις κάτι επειδή το είδες σε βίντεο;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Ίσως',
     'correct_answer': 'a', 'explanation': 'Αυτό είναι φυσιολογικό - αλλά να είσαι προσεκτικός!', 'difficulty': 'easy'},
    
    {'category': 'child', 'theme': 'influencers', 'question_number': 45,
     'question_text': 'Ποιος σε βοηθά να καταλάβεις τι είναι αλήθεια online;',
     'option_a': 'Οι γονείς μου', 'option_b': 'Οι φίλοι μου', 'option_c': 'Κανένας',
     'correct_answer': 'a', 'explanation': 'Οι γονείς και οι δάσκαλοι μπορούν να σε βοηθήσουν!', 'difficulty': 'easy'},
]

# ============================================
# ΕΝΗΛΙΚΕΣ - 30 ΕΡΩΤΗΣΕΙΣ
# ============================================

adult_questions = [
    # Θεματική 1: Passwords & Auth (5 ερωτήσεις)
    {'category': 'adult', 'theme': 'passwords_auth', 'question_number': 1,
     'question_text': 'Πόσο συχνά αλλάζετε τους κωδικούς σας;',
     'option_a': 'Ποτέ', 'option_b': 'Μία φορά το χρόνο', 'option_c': 'Κάθε 3-6 μήνες',
     'correct_answer': 'c', 'explanation': 'Η τακτική αλλαγή κωδικών ενισχύει την ασφάλεια!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'passwords_auth', 'question_number': 2,
     'question_text': 'Χρησιμοποιείτε τον ίδιο κωδικό για πολλούς λογαριασμούς;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Μερικές φορές',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην επαναχρησιμοποιείτε κωδικούς!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'passwords_auth', 'question_number': 3,
     'question_text': 'Τι είναι Two Factor Authentication (2FA);',
     'option_a': 'Έλεγχος δύο email', 'option_b': 'Έλεγχος με κωδικό + άλλο στοιχείο', 'option_c': 'Δεν ξέρω',
     'correct_answer': 'b', 'explanation': 'Το 2FA προσθέτει επιπλέον επίπεδο ασφάλειας!', 'difficulty': 'medium'},
    
    {'category': 'adult', 'theme': 'passwords_auth', 'question_number': 4,
     'question_text': 'Τι πρέπει να περιέχει ένας ισχυρός κωδικός;',
     'option_a': 'Μόνο αριθμούς', 'option_b': 'Μικρά και κεφαλαία γράμματα, σύμβολα, αριθμούς', 'option_c': 'Μόνο το όνομά σας',
     'correct_answer': 'b', 'explanation': 'Ένας ισχυρός κωδικός συνδυάζει πολλά στοιχεία!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'passwords_auth', 'question_number': 5,
     'question_text': 'Ποια εφαρμογή βοηθά στη διαχείριση κωδικών;',
     'option_a': 'Password manager', 'option_b': 'Antivirus', 'option_c': 'Browser',
     'correct_answer': 'a', 'explanation': 'Οι password managers αποθηκεύουν ασφαλείς κωδικούς!', 'difficulty': 'easy'},
    
    # Θεματική 2: Phishing & Scams (5 ερωτήσεις)
    {'category': 'adult', 'theme': 'phishing_scam', 'question_number': 6,
     'question_text': 'Τι είναι phishing;',
     'option_a': 'Μήνυμα για ψάρεμα', 'option_b': 'Μήνυμα που προσπαθεί να κλέψει στοιχεία', 'option_c': 'Ενημερωτικό email',
     'correct_answer': 'b', 'explanation': 'Το phishing είναι απάτη για κλοπή δεδομένων!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'phishing_scam', 'question_number': 7,
     'question_text': 'Ποιο είναι σημάδι phishing email;',
     'option_a': 'Ορθογραφικά λάθη και ύποπτος αποστολέας', 'option_b': 'Μήνυμα από τράπεζα', 'option_c': 'Μήνυμα από φίλο',
     'correct_answer': 'a', 'explanation': 'Λάθη και ύποπτες διευθύνσεις είναι σημάδια phishing!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'phishing_scam', 'question_number': 8,
     'question_text': 'Αν λάβετε email που ζητά προσωπικά στοιχεία, τι κάνετε;',
     'option_a': 'Τα στέλνω αμέσως', 'option_b': 'Τα αγνοώ ή το ελέγχω από άλλη πηγή', 'option_c': 'Τα γράφω σε απάντηση',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην δίνετε προσωπικά στοιχεία μέσω email!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'phishing_scam', 'question_number': 9,
     'question_text': 'Μπορεί ένα phishing email να φαίνεται επαγγελματικό;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Δεν ξέρω',
     'correct_answer': 'a', 'explanation': 'Τα phishing emails μπορεί να μοιάζουν πολύ αληθινά!', 'difficulty': 'medium'},
    
    {'category': 'adult', 'theme': 'phishing_scam', 'question_number': 10,
     'question_text': 'Αν λάβετε τηλεφώνημα που ζητά στοιχεία λογαριασμού;',
     'option_a': 'Τα δίνω', 'option_b': 'Τα αρνούμαι και ενημερώνω την τράπεζα', 'option_c': 'Κλείνω το τηλέφωνο',
     'correct_answer': 'b', 'explanation': 'Αρνηθείτε και ενημερώστε την τράπεζα!', 'difficulty': 'easy'},
    
    # Θεματική 3: Social Media Privacy (4 ερωτήσεις)
    {'category': 'adult', 'theme': 'social_privacy', 'question_number': 11,
     'question_text': 'Ποιος μπορεί να δει τα posts σας αν το προφίλ είναι δημόσιο;',
     'option_a': 'Μόνο οι φίλοι', 'option_b': 'Όλοι', 'option_c': 'Κανείς',
     'correct_answer': 'b', 'explanation': 'Δημόσιο προφίλ = όλοι μπορούν να δουν!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'social_privacy', 'question_number': 12,
     'question_text': 'Είναι ασφαλές να δημοσιεύετε τη διεύθυνσή σας online;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Μερικές φορές',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην δημοσιεύετε τη διεύθυνσή σας!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'social_privacy', 'question_number': 13,
     'question_text': 'Ποια ρύθμιση ενισχύει την ιδιωτικότητα;',
     'option_a': 'Location tagging', 'option_b': 'Friends only posts', 'option_c': 'Public posts',
     'correct_answer': 'b', 'explanation': 'Το "Μόνο φίλοι" προστατεύει την ιδιωτικότητά σας!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'social_privacy', 'question_number': 14,
     'question_text': 'Τι πρέπει να αποφεύγετε να δημοσιεύετε;',
     'option_a': 'Φωτογραφίες φαγητού', 'option_b': 'Προσωπικά δεδομένα όπως ΑΦΜ', 'option_c': 'Τοποθεσία ταξιδιών',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην δημοσιεύετε ΑΦΜ ή αριθμούς καρτών!', 'difficulty': 'easy'},
    
    # Θεματική 4: Online Banking (4 ερωτήσεις)
    {'category': 'adult', 'theme': 'online_banking', 'question_number': 15,
     'question_text': 'Τι σημαίνει το λουκετάκι σε μια ιστοσελίδα;',
     'option_a': 'Ότι είναι ασφαλής (HTTPS)', 'option_b': 'Ότι χρειάζεται κωδικό', 'option_c': 'Ότι είναι κλειδωμένη',
     'correct_answer': 'a', 'explanation': 'Το λουκετάκι σημαίνει ασφαλή σύνδεση HTTPS!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'online_banking', 'question_number': 16,
     'question_text': 'Είναι ασφαλές να χρησιμοποιείτε δημόσιο Wi-Fi για online banking;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Μερικές φορές',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην κάνετε banking σε δημόσιο Wi-Fi!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'online_banking', 'question_number': 17,
     'question_text': 'Ποια μέθοδος πληρωμής είναι πιο ασφαλής;',
     'option_a': 'Κατάθεση σε IBAN από email', 'option_b': 'Μέσω έμπιστης πλατφόρμας (PayPal)', 'option_c': 'Μετρητά',
     'correct_answer': 'b', 'explanation': 'Έμπιστες πλατφόρμες είναι πιο ασφαλείς!', 'difficulty': 'medium'},
    
    {'category': 'adult', 'theme': 'online_banking', 'question_number': 18,
     'question_text': 'Τι πρέπει να προσέχετε όταν κατεβάζετε εφαρμογές;',
     'option_a': 'Αν έχουν καλές κριτικές', 'option_b': 'Αν είναι από επίσημο κατάστημα', 'option_c': 'Και τα δύο',
     'correct_answer': 'c', 'explanation': 'Έλεγξε και τα δύο για ασφάλεια!', 'difficulty': 'easy'},
    
    # Θεματική 5: Device Security (2 ερωτήσεις)
    {'category': 'adult', 'theme': 'network_security', 'question_number': 19,
     'question_text': 'Τι είναι VPN;',
     'option_a': 'Εικονικό ιδιωτικό δίκτυο', 'option_b': 'Πρόγραμμα γραφικών', 'option_c': 'Social media',
     'correct_answer': 'a', 'explanation': 'Το VPN κρυπτογραφεί τη σύνδεσή σας!', 'difficulty': 'medium'},
    
    {'category': 'adult', 'theme': 'network_security', 'question_number': 20,
     'question_text': 'Γιατί πρέπει να ενημερώνετε τακτικά τις εφαρμογές;',
     'option_a': 'Για αισθητική', 'option_b': 'Για λόγους ασφαλείας', 'option_c': 'Για να αλλάζει το logo',
     'correct_answer': 'b', 'explanation': 'Οι ενημερώσεις διορθώνουν τρύπες ασφαλείας!', 'difficulty': 'easy'},
    
    # Θεματική 6: Digital Literacy (10 ερωτήσεις)
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 21,
     'question_text': 'Όταν διαβάζετε μια είδηση online, πώς ελέγχετε αν είναι αληθινή;',
     'option_a': 'Την κοινοποιώ αν συμφωνώ', 'option_b': 'Ελέγχω την πηγή', 'option_c': 'Δεν με απασχολεί',
     'correct_answer': 'b', 'explanation': 'Πάντα ελέγχετε την πηγή της είδησης!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 22,
     'question_text': 'Τι είναι η παραπληροφόρηση (fake news);',
     'option_a': 'Μια άποψη που δε μου αρέσει', 'option_b': 'Εσκεμμένα ψευδές περιεχόμενο', 'option_c': 'Χιούμορ',
     'correct_answer': 'b', 'explanation': 'Fake news είναι σκόπιμα παραπλανητικό περιεχόμενο!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 23,
     'question_text': 'Ποια πηγή θεωρείτε πιο αξιόπιστη;',
     'option_a': 'Επαληθευμένο μέσο ενημέρωσης', 'option_b': 'Blog με πολλούς followers', 'option_c': 'Οποιοδήποτε Google result',
     'correct_answer': 'a', 'explanation': 'Επαληθευμένα μέσα είναι πιο αξιόπιστα!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 24,
     'question_text': 'Έχετε ελέγξει ποτέ αν μια φωτογραφία online είναι αληθινή;',
     'option_a': 'Ναι, με αντίστροφη αναζήτηση', 'option_b': 'Όχι, δεν ξέρω πώς', 'option_c': 'Δεν με ενδιαφέρει',
     'correct_answer': 'a', 'explanation': 'Η αντίστροφη αναζήτηση εικόνας βοηθά στον έλεγχο!', 'difficulty': 'medium'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 25,
     'question_text': 'Πώς χειρίζεστε άρθρα που προκαλούν φόβο;',
     'option_a': 'Τα διαβάζω αλλά ελέγχω την πηγή', 'option_b': 'Τα κοινοποιώ άμεσα', 'option_c': 'Τα αποφεύγω',
     'correct_answer': 'a', 'explanation': 'Διαβάστε αλλά ελέγξτε πάντα την πηγή!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 26,
     'question_text': 'Ξέρετε τι είναι το echo chamber;',
     'option_a': 'Όχι', 'option_b': 'Ναι - όταν βλέπουμε μόνο απόψεις που συμφωνούμε', 'option_c': 'Κάτι με μουσική',
     'correct_answer': 'b', 'explanation': 'Echo chamber = θάλαμος αντήχησης απόψεων!', 'difficulty': 'medium'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 27,
     'question_text': 'Πιστεύετε ότι οι αλγόριθμοι επηρεάζουν τι βλέπετε online;',
     'option_a': 'Όχι', 'option_b': 'Ναι', 'option_c': 'Δεν γνωρίζω',
     'correct_answer': 'b', 'explanation': 'Οι αλγόριθμοι επιλέγουν τι βλέπετε!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 28,
     'question_text': 'Έχετε πέσει ποτέ θύμα παραπληροφόρησης;',
     'option_a': 'Ναι', 'option_b': 'Όχι', 'option_c': 'Ίσως',
     'correct_answer': 'c', 'explanation': 'Πολλοί από εμάς έχουμε παραπλανηθεί κάποια στιγμή!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 29,
     'question_text': 'Πόσο άνετα νιώθετε να διασταυρώνετε πληροφορίες;',
     'option_a': 'Πολύ άνετα', 'option_b': 'Λίγο', 'option_c': 'Καθόλου',
     'correct_answer': 'a', 'explanation': 'Η διασταύρωση πληροφοριών είναι σημαντική δεξιότητα!', 'difficulty': 'easy'},
    
    {'category': 'adult', 'theme': 'digital_literacy', 'question_number': 30,
     'question_text': 'Από πού ενημερώνεστε κυρίως;',
     'option_a': 'Κοινωνικά δίκτυα', 'option_b': 'Επαγγελματικά μέσα', 'option_c': 'Παραδοσιακά ΜΜΕ',
     'correct_answer': 'b', 'explanation': 'Τα επαγγελματικά μέσα έχουν συνήθως υψηλότερη αξιοπιστία!', 'difficulty': 'easy'},
]

# ============================================
# ΕΠΑΓΓΕΛΜΑΤΙΕΣ - 35 ΕΡΩΤΗΣΕΙΣ
# ============================================

professional_questions = [
    # Θεματική 1: Advanced Auth (5 ερωτήσεις)
    {'category': 'professional', 'theme': 'advanced_auth', 'question_number': 1,
     'question_text': 'Τι είναι MFA;',
     'option_a': 'Multi Factor Authentication', 'option_b': 'Mail Forwarding Application', 'option_c': 'Media File Access',
     'correct_answer': 'a', 'explanation': 'MFA = πολλαπλοί παράγοντες επαλήθευσης!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_auth', 'question_number': 2,
     'question_text': 'Τι είναι Single Sign-On (SSO);',
     'option_a': 'Ένας κωδικός για όλα με ασφάλεια', 'option_b': 'Password manager', 'option_c': 'VPN',
     'correct_answer': 'a', 'explanation': 'SSO επιτρέπει μία σύνδεση για πολλές εφαρμογές!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'advanced_auth', 'question_number': 3,
     'question_text': 'Ποιο password policy είναι πιο ασφαλές;',
     'option_a': 'Min 8 χαρακτήρες', 'option_b': 'Min 12 χαρακτήρες με complexity', 'option_c': 'Όποιο θυμάται ο χρήστης',
     'correct_answer': 'b', 'explanation': 'Minimum 12 χαρακτήρες με πολυπλοκότητα είναι ασφαλέστερο!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'advanced_auth', 'question_number': 4,
     'question_text': 'Τι είναι password manager;',
     'option_a': 'Αποθήκευση και δημιουργία ισχυρών κωδικών', 'option_b': 'Αποθήκευση φωτογραφιών', 'option_c': 'VPN',
     'correct_answer': 'a', 'explanation': 'Password managers διαχειρίζονται ασφαλείς κωδικούς!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_auth', 'question_number': 5,
     'question_text': 'Ποια μέθοδος αυθεντικοποίησης είναι πιο ασφαλής;',
     'option_a': 'Password μόνο', 'option_b': 'Password + token ή app', 'option_c': 'Password + email',
     'correct_answer': 'b', 'explanation': 'Password + hardware token ή app είναι το πιο ασφαλές!', 'difficulty': 'medium'},
    
    # Θεματική 2: Social Engineering (5 ερωτήσεις)
    {'category': 'professional', 'theme': 'social_engineering', 'question_number': 6,
     'question_text': 'Τι είναι spear phishing;',
     'option_a': 'Γενικά phishing emails', 'option_b': 'Στοχευμένο phishing σε συγκεκριμένο άτομο', 'option_c': 'Scam SMS',
     'correct_answer': 'b', 'explanation': 'Spear phishing = στοχευμένη επίθεση!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'social_engineering', 'question_number': 7,
     'question_text': 'Τι είναι social engineering;',
     'option_a': 'Επίθεση σε social media', 'option_b': 'Εξαπάτηση ανθρώπων για πρόσβαση σε πληροφορίες', 'option_c': 'Χρήση bots',
     'correct_answer': 'b', 'explanation': 'Social engineering χειραγωγεί ανθρώπους!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'social_engineering', 'question_number': 8,
     'question_text': 'Ποιο είναι παράδειγμα social engineering;',
     'option_a': 'Email με ιό', 'option_b': 'Τηλεφώνημα από "τεχνική υποστήριξη"', 'option_c': 'Fake news',
     'correct_answer': 'b', 'explanation': 'Ψεύτικη τεχνική υποστήριξη είναι κλασικό social engineering!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'social_engineering', 'question_number': 9,
     'question_text': 'Τι πρέπει να κάνετε αν λάβετε ύποπτο email στο εταιρικό;',
     'option_a': 'Να το προωθήσω σε συναδέλφους', 'option_b': 'Να το αναφέρω στο IT/security team', 'option_c': 'Να το αγνοήσω',
     'correct_answer': 'b', 'explanation': 'Πάντα ενημερώνετε το security team!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'social_engineering', 'question_number': 10,
     'question_text': 'Ποια μέθοδος μειώνει τον κίνδυνο social engineering;',
     'option_a': 'Awareness training', 'option_b': 'Νέο antivirus', 'option_c': 'Πιο γρήγορο internet',
     'correct_answer': 'a', 'explanation': 'Η εκπαίδευση προσωπικού είναι η καλύτερη άμυνα!', 'difficulty': 'easy'},
    
    # Θεματική 3: Cloud & Network Security (5 ερωτήσεις)
    {'category': 'professional', 'theme': 'cloud_network', 'question_number': 11,
     'question_text': 'Τι είναι VPN;',
     'option_a': 'Εικονικό ιδιωτικό δίκτυο', 'option_b': 'Antivirus', 'option_c': 'Password manager',
     'correct_answer': 'a', 'explanation': 'VPN δημιουργεί ασφαλή σύνδεση!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'cloud_network', 'question_number': 12,
     'question_text': 'Ποια είναι η κύρια απειλή σε cloud περιβάλλον;',
     'option_a': 'Malware', 'option_b': 'Κακή διαχείριση προσβάσεων', 'option_c': 'Αργό internet',
     'correct_answer': 'b', 'explanation': 'Η κακή διαχείριση προσβάσεων είναι μεγάλος κίνδυνος!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'cloud_network', 'question_number': 13,
     'question_text': 'Τι είναι DDoS attack;',
     'option_a': 'Virus σε υπολογιστή', 'option_b': 'Επίθεση υπερφόρτωσης server', 'option_c': 'Spam email',
     'correct_answer': 'b', 'explanation': 'DDoS υπερφορτώνει servers με αιτήματα!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'cloud_network', 'question_number': 14,
     'question_text': 'Τι είναι firewall;',
     'option_a': 'Φυσικός τοίχος', 'option_b': 'Σύστημα φιλτραρίσματος κυκλοφορίας δικτύου', 'option_c': 'Antivirus',
     'correct_answer': 'b', 'explanation': 'Firewall φιλτράρει την κυκλοφορία δικτύου!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'cloud_network', 'question_number': 15,
     'question_text': 'Τι είναι Zero Trust;',
     'option_a': 'Μη εμπιστοσύνη σε κανέναν χρήστη εξ ορισμού', 'option_b': 'Απαγόρευση πρόσβασης', 'option_c': 'VPN τύπου',
     'correct_answer': 'a', 'explanation': 'Zero Trust = επαλήθευση για όλους, πάντα!', 'difficulty': 'medium'},
    
    # Θεματική 4: GDPR & Compliance (5 ερωτήσεις)
    {'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 16,
     'question_text': 'Τι είναι GDPR;',
     'option_a': 'Γενικός Κανονισμός Προστασίας Δεδομένων (ΕΕ)', 'option_b': 'Τεχνολογία encryption', 'option_c': 'Firewall',
     'correct_answer': 'a', 'explanation': 'GDPR = κανονισμός της ΕΕ για προσωπικά δεδομένα!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 17,
     'question_text': 'Ποιο είναι προσωπικό δεδομένο;',
     'option_a': 'Η IP διεύθυνση', 'option_b': 'Το είδος του browser', 'option_c': 'Το μέγεθος οθόνης',
     'correct_answer': 'a', 'explanation': 'Η IP διεύθυνση είναι προσωπικό δεδομένο!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 18,
     'question_text': 'Πότε απαιτείται DPIA;',
     'option_a': 'Όταν επεξεργάζεσαι ευαίσθητα δεδομένα', 'option_b': 'Όταν αγοράζεις antivirus', 'option_c': 'Όταν αλλάζεις password',
     'correct_answer': 'a', 'explanation': 'DPIA απαιτείται για ευαίσθητα δεδομένα!', 'difficulty': 'hard'},
    
    {'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 19,
     'question_text': 'Τι σημαίνει data breach;',
     'option_a': 'Προστασία δεδομένων', 'option_b': 'Παραβίαση και διαρροή δεδομένων', 'option_c': 'Backup αρχείων',
     'correct_answer': 'b', 'explanation': 'Data breach = παραβίαση ασφαλείας δεδομένων!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'gdpr_compliance', 'question_number': 20,
     'question_text': 'Ποια αρχή εποπτεύει το GDPR στην Ελλάδα;',
     'option_a': 'ΑΔΑΕ', 'option_b': 'Αρχή Προστασίας Δεδομένων Προσωπικού Χαρακτήρα', 'option_c': 'Υπουργείο Ψηφιακής Διακυβέρνησης',
     'correct_answer': 'b', 'explanation': 'Η ΑΠΔΠΧ εποπτεύει το GDPR στην Ελλάδα!', 'difficulty': 'medium'},
    
    # Θεματική 5: Incident Response (5 ερωτήσεις)
    {'category': 'professional', 'theme': 'incident_response', 'question_number': 21,
     'question_text': 'Ποιο είναι το πρώτο βήμα σε security incident;',
     'option_a': 'Απόκρυψη συμβάντος', 'option_b': 'Ενημέρωση αρμόδιων και isolation', 'option_c': 'Restart συστήματος',
     'correct_answer': 'b', 'explanation': 'Άμεση ενημέρωση και απομόνωση!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'incident_response', 'question_number': 22,
     'question_text': 'Τι είναι vulnerability scan;',
     'option_a': 'Έλεγχος αδυναμιών συστημάτων', 'option_b': 'Καθαρισμός cache', 'option_c': 'Backup',
     'correct_answer': 'a', 'explanation': 'Vulnerability scan εντοπίζει αδυναμίες!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'incident_response', 'question_number': 23,
     'question_text': 'Τι είναι penetration test;',
     'option_a': 'Εξωτερική επίθεση για αξιολόγηση αδυναμιών', 'option_b': 'Update εφαρμογών', 'option_c': 'Κατέβασμα antivirus',
     'correct_answer': 'a', 'explanation': 'Penetration testing δοκιμάζει την ασφάλεια!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'incident_response', 'question_number': 24,
     'question_text': 'Τι είναι SIEM;',
     'option_a': 'Πρόγραμμα γραφικών', 'option_b': 'Security Information and Event Management', 'option_c': 'Password manager',
     'correct_answer': 'b', 'explanation': 'SIEM συλλέγει και αναλύει security events!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'incident_response', 'question_number': 25,
     'question_text': 'Τι είναι endpoint protection;',
     'option_a': 'Antivirus μόνο', 'option_b': 'Ολοκληρωμένη προστασία συσκευών τελικού χρήστη', 'option_c': 'VPN',
     'correct_answer': 'b', 'explanation': 'Endpoint protection προστατεύει συσκευές χρηστών!', 'difficulty': 'easy'},
    
    # Θεματική 6: Advanced Practices (10 ερωτήσεις)
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 26,
     'question_text': 'Τι είναι η αρχή του ελάχιστου δικαιώματος (least privilege);',
     'option_a': 'Πρόσβαση μόνο σε ό,τι είναι απαραίτητο', 'option_b': 'Πλήρη πρόσβαση για όλους', 'option_c': 'Κανείς δεν έχει πρόσβαση',
     'correct_answer': 'a', 'explanation': 'Least privilege = ελάχιστα απαραίτητα δικαιώματα!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 27,
     'question_text': 'Ποιο είναι σωστό για τη διαχείριση δικαιωμάτων;',
     'option_a': 'Ενημερώνονται τακτικά με βάση τον ρόλο', 'option_b': 'Δίνονται μία φορά', 'option_c': 'Όλοι έχουν κοινό λογαριασμό',
     'correct_answer': 'a', 'explanation': 'Τα δικαιώματα πρέπει να ενημερώνονται τακτικά!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 28,
     'question_text': 'Τι είναι το BYOD (Bring Your Own Device);',
     'option_a': 'Τεχνική hacking', 'option_b': 'Πολιτική χρήσης προσωπικών συσκευών στην εργασία', 'option_c': 'Cloud backup',
     'correct_answer': 'b', 'explanation': 'BYOD = χρήση προσωπικών συσκευών στη δουλειά!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 29,
     'question_text': 'Ποιοι κίνδυνοι σχετίζονται με το BYOD;',
     'option_a': 'Ασφαλέστερες συνδέσεις', 'option_b': 'Κίνδυνος απώλειας δεδομένων και malware', 'option_c': 'Ταχύτερη επεξεργασία',
     'correct_answer': 'b', 'explanation': 'BYOD αυξάνει κινδύνους απώλειας δεδομένων!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 30,
     'question_text': 'Τι είναι η πολιτική cookies σε websites;',
     'option_a': 'Δεν έχει σημασία', 'option_b': 'Πρέπει να συμμορφώνεται με GDPR', 'option_c': 'Την ορίζει η Google',
     'correct_answer': 'b', 'explanation': 'Η πολιτική cookies πρέπει να είναι GDPR-compliant!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 31,
     'question_text': 'Ποιο ΔΕΝ είναι καλό παράδειγμα ασφάλειας;',
     'option_a': 'Ανανέωση κωδικών κάθε 3 μήνες', 'option_b': 'Αποθήκευση κωδικών σε post-it', 'option_c': 'Χρήση MFA',
     'correct_answer': 'b', 'explanation': 'Ποτέ μην γράφετε κωδικούς σε post-it!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 32,
     'question_text': 'Τι είναι honeypot στην κυβερνοασφάλεια;',
     'option_a': 'Προστατευτικό για emails', 'option_b': 'Παγίδα που προσελκύει επιτιθέμενους', 'option_c': 'Antivirus',
     'correct_answer': 'b', 'explanation': 'Honeypot = παγίδα για επιτιθέμενους!', 'difficulty': 'hard'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 33,
     'question_text': 'Τι είναι το shadow IT;',
     'option_a': 'Εγκεκριμένα εργαλεία', 'option_b': 'Μη εξουσιοδοτημένες τεχνολογίες που χρησιμοποιούν εργαζόμενοι', 'option_c': 'Dark web apps',
     'correct_answer': 'b', 'explanation': 'Shadow IT = μη εγκεκριμένα εργαλεία!', 'difficulty': 'medium'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 34,
     'question_text': 'Ποια είναι η σωστή αντίδραση σε data leak;',
     'option_a': 'Αγνοώ', 'option_b': 'Καταγράφω και ενημερώνω την ομάδα', 'option_c': 'Αλλάζω προσωπικά passwords',
     'correct_answer': 'b', 'explanation': 'Άμεση αναφορά και καταγραφή!', 'difficulty': 'easy'},
    
    {'category': 'professional', 'theme': 'advanced_practices', 'question_number': 35,
     'question_text': 'Τι είναι η αρχή "Security by Design";',
     'option_a': 'Ασφάλεια στο τέλος', 'option_b': 'Ασφάλεια από την αρχή στον σχεδιασμό', 'option_c': 'Δεν είναι απαραίτητη',
     'correct_answer': 'b', 'explanation': 'Security by Design = ασφάλεια από την αρχή!', 'difficulty': 'easy'},
]

def insert_all_questions():
    """Εισαγωγή όλων των ερωτήσεων"""
    with app.app_context():
        # Διαγραφή παλιών
        print("Διαγραφή παλιών ερωτήσεων...")
        Question.query.delete()
        
        all_questions = child_questions + adult_questions + professional_questions
        
        print(f"Εισαγωγή {len(all_questions)} ερωτήσεων...")
        
        for q in all_questions:
            question = Question(**q)
            db.session.add(question)
        
        db.session.commit()
        
        print(f"\n✅ Επιτυχής εισαγωγή {len(all_questions)} ερωτήσεων!")
        print(f"   - Παιδιά: {len(child_questions)} ερωτήσεις")
        print(f"   - Ενήλικες: {len(adult_questions)} ερωτήσεις")
        print(f"   - Επαγγελματίες: {len(professional_questions)} ερωτήσεις")

