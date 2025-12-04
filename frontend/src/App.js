import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from 'recharts';
import { Shield, AlertTriangle, Award, TrendingUp, CheckCircle, XCircle, Target, BookOpen } from 'lucide-react';
import DemographicsForm from './components/DemographicsForm';
//import AnimatedBackground from './AnimatedBackground';

const CyberQuizApp = () => {
  const [stage, setStage] = useState('category');
  const [category, setCategory] = useState(null);
  const [sessionId, setSessionId] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [questions, setQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState([]);
  const [results, setResults] = useState(null);
  const [demographics, setDemographics] = useState({});
  const [showFeedback, setShowFeedback] = useState(false);
  const [lastAnswer, setLastAnswer] = useState(null);

  const mockQuestions = {
    child: [
      {
        id: 1,
        theme: 'passwords',
        question_text: 'Ποιος είναι ένας καλός κωδικός;',
        options: { a: '123456', b: 'toonomamou', c: '$uperK0d1k0$' },
        correct_answer: 'c',
        explanation: 'Ένας δυνατός κωδικός έχει γράμματα, αριθμούς και σύμβολα!'
      }
    ],
    adult: [
      {
        id: 3,
        theme: 'passwords_auth',
        question_text: 'Τι είναι Two Factor Authentication (2FA);',
        options: { a: 'Έλεγχος δύο email', b: 'Έλεγχος με κωδικό + άλλο στοιχείο', c: 'Δεν ξέρω' },
        correct_answer: 'b',
        explanation: 'Το 2FA προσθέτει ένα επιπλέον επίπεδο ασφάλειας πέρα από τον κωδικό.'
      }
    ],
    professional: [
      {
        id: 4,
        theme: 'advanced_auth',
        question_text: 'Τι είναι MFA;',
        options: { a: 'Multi Factor Authentication', b: 'Mail Forwarding Application', c: 'Media File Access' },
        correct_answer: 'a',
        explanation: 'MFA απαιτεί πολλαπλούς παράγοντες επαλήθευσης!'
      }
    ]
  };

  const categories = [
    { id: 'child', name: 'Παιδιά', icon: '👶', color: 'from-blue-400 to-blue-600', description: '8-12 ετών' },
    { id: 'adult', name: 'Ενήλικες', icon: '👨‍💼', color: 'from-green-400 to-green-600', description: 'Γενικοί χρήστες' },
    { id: 'professional', name: 'Επαγγελματίες', icon: '💼', color: 'from-purple-400 to-purple-600', description: 'IT & Advanced' }
  ];

  const startSession = (selectedCategory) => {
    setCategory(selectedCategory);
    setSessionId(`session-${Date.now()}`);
    setStage('demographics');
  };

  const saveDemographics = async () => {
    try {
      const response = await fetch(`http://localhost:5000/api/questions/${category}`);
      const data = await response.json();
      
      console.log('Fetched questions:', data);
      console.log('Number of questions:', data.length);
      
      if (data && data.length > 0) {
        setQuestions(data);
        setStage('quiz');
      } else {
        alert('Δεν βρέθηκαν ερωτήσεις!');
      }
    } catch (error) {
      console.error('Error fetching questions:', error);
      setQuestions(mockQuestions[category] || mockQuestions.child);
      setStage('quiz');
    }
  };

  const submitAnswer = (answer) => {
    const question = questions[currentQuestion];
    const isCorrect = answer === question.correct_answer;
    
    setLastAnswer({
      isCorrect,
      correctAnswer: question.correct_answer,
      explanation: question.explanation,
      userAnswer: answer
    });
    
    setUserAnswers([...userAnswers, { questionId: question.id, answer, isCorrect }]);
    setShowFeedback(true);
  };

  const nextQuestion = () => {
    setShowFeedback(false);
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      completeQuiz();
    }
  };

  const generateRecommendations = (results, category) => {
    const recommendations = [];
    
    Object.entries(results.theme_scores).forEach(([theme, score]) => {
      if (score < 60) {
        const rec = getRecommendationForTheme(theme, category, 'high');
        if (rec) recommendations.push(rec);
      } else if (score < 80) {
        const rec = getRecommendationForTheme(theme, category, 'medium');
        if (rec) recommendations.push(rec);
      }
    });
    
    if (recommendations.length === 0) {
      recommendations.push({
        theme: 'general',
        text: category === 'child' 
          ? 'Τα πας υπέροχα! Συνέχισε να είσαι προσεκτικός/η online! 🌟'
          : category === 'adult'
          ? 'Εξαιρετική επίδοση! Συνεχίστε να εφαρμόζετε καλές πρακτικές ασφάλειας! 🎯'
          : 'Άριστη γνώση cybersecurity! Μοιραστείτε τις γνώσεις σας με τους συναδέλφους! 💼',
        priority: 'low'
      });
    }
    
    return recommendations;
  };

  const getRecommendationForTheme = (theme, category, priority) => {
    const recommendations = {
      child: {
        passwords: {
          high: 'Οι κωδικοί είναι σαν το κλειδί του σπιτιού σου! Χρησιμοποίησε δυνατούς κωδικούς με γράμματα, αριθμούς και σύμβολα! 🔐',
          medium: 'Μην μοιράζεσαι τους κωδικούς σου με φίλους - ούτε καν με τον καλύτερό σου! 🤫'
        },
        phishing: {
          high: 'Πρόσεχε τα ύποπτα μηνύματα! Αν κάτι φαίνεται περίεργο, ρώτα έναν ενήλικα! ⚠️',
          medium: 'Δείξε πάντα τα μηνύματα από αγνώστους στους γονείς σου! 👨‍👩‍👧'
        },
        social_media: {
          high: 'Μην δέχεσαι φίλους που δεν γνωρίζεις στα social media! Μόνο πραγματικούς φίλους! 📱',
          medium: 'Μην ανεβάζεις φωτογραφίες χωρίς την άδεια των γονιών σου! 📸'
        },
        privacy: {
          high: 'Το όνομα, η διεύθυνση και το σχολείο σου είναι μυστικά! Μην τα λες σε αγνώστους online! 🔒',
          medium: 'Ρώτα πάντα τους γονείς πριν μοιραστείς πληροφορίες στο internet! 🙋'
        },
        online_behavior: {
          high: 'Να είσαι ευγενικός/ή online όπως και στην πραγματική ζωή! Όχι bullying! 💙',
          medium: 'Αν κάποιος σε ενοχλεί online, μίλα αμέσως σε έναν ενήλικα! 🆘'
        },
        safe_browsing: {
          high: 'Επισκέπτου μόνο ιστοσελίδες που εγκρίνουν οι γονείς σου! 🌐',
          medium: 'Αν ένα site σου ζητάει χρήματα ή πληροφορίες, κλείσε το και πες στους γονείς! 🚫'
        },
        influencers: {
          high: 'Όχι όλα όσα βλέπεις σε βίντεο είναι αλήθεια! Ρώτα έναν ενήλικα αν δεν είσαι σίγουρος/η! 🎬',
          medium: 'Οι influencers πληρώνονται για να διαφημίζουν προϊόντα - σκέψου πριν πιστέψεις! 🤔'
        }
      },
      adult: {
        passwords_auth: {
          high: 'Χρησιμοποιήστε μοναδικούς, δυνατούς κωδικούς για κάθε λογαριασμό! Εγκαταστήστε ένα password manager! 🔐',
          medium: 'Ενεργοποιήστε το Two-Factor Authentication (2FA) σε όλους τους σημαντικούς λογαριασμούς! 📱'
        },
        phishing: {
          high: 'Προσοχή στα ύποπτα emails! Ελέγξτε πάντα τον αποστολέα και μην κάνετε κλικ σε links! ⚠️',
          medium: 'Μην εμπιστεύεστε emails που ζητούν επείγουσα δράση ή προσωπικά στοιχεία! 🎣'
        },
        social_media: {
          high: 'Ελέγξτε τις ρυθμίσεις απορρήτου στα social media! Περιορίστε ποιος βλέπει τις αναρτήσεις σας! 🔒',
          medium: 'Προσέξτε τι μοιράζεστε δημόσια - μπορεί να χρησιμοποιηθεί για social engineering! 📱'
        },
        privacy: {
          high: 'Διαβάστε τις πολιτικές απορρήτου των υπηρεσιών που χρησιμοποιείτε! Περιορίστε τα δεδομένα που μοιράζεστε! 🛡️',
          medium: 'Χρησιμοποιήστε VPN σε δημόσια Wi-Fi και απενεργοποιήστε το location tracking! 🌐'
        },
        online_shopping: {
          high: 'Αγοράζετε μόνο από έμπιστες ιστοσελίδες με HTTPS! Ελέγξτε reviews και πιστοποιήσεις! 🛒',
          medium: 'Μην αποθηκεύετε πιστωτικές κάρτες σε sites - χρησιμοποιήστε εικονικές κάρτες! 💳'
        },
        device_security: {
          high: 'Ενημερώνετε τακτικά λειτουργικό σύστημα και εφαρμογές! Χρησιμοποιήστε antivirus! 💻',
          medium: 'Κλειδώνετε τη συσκευή σας όταν δεν τη χρησιμοποιείτε! Χρησιμοποιήστε δυνατό PIN! 🔐'
        }
      },
      professional: {
        advanced_auth: {
          high: 'Εφαρμόστε MFA σε όλα τα εταιρικά συστήματα! Χρησιμοποιήστε hardware tokens για κρίσιμες υπηρεσίες! 🔑',
          medium: 'Εφαρμόστε Zero Trust architecture και least privilege access! 🛡️'
        },
        social_engineering: {
          high: 'Εκπαιδεύστε το προσωπικό σε tactic social engineering! Κάντε simulated phishing tests! 🎓',
          medium: 'Εφαρμόστε verification procedures για ευαίσθητες αιτήσεις (π.χ. wire transfers)! ☎️'
        },
        network_security: {
          high: 'Εφαρμόστε network segmentation, IDS/IPS και regular security audits! 🔍',
          medium: 'Χρησιμοποιήστε firewalls και encryption για όλη την εταιρική επικοινωνία! 🔒'
        },
        incident_response: {
          high: 'Αναπτύξτε και δοκιμάστε incident response plan! Ορίστε ξεκάθαρα roles και procedures! 📋',
          medium: 'Εφαρμόστε logging και monitoring για γρήγορη ανίχνευση απειλών! 📊'
        },
        compliance: {
          high: 'Εξασφαλίστε συμμόρφωση με GDPR, ISO 27001 και άλλα standards! Κάντε τακτικά audits! ⚖️',
          medium: 'Τεκμηριώστε όλες τις security policies και procedures! 📄'
        },
        data_protection: {
          high: 'Εφαρμόστε data encryption at rest και in transit! Κάντε τακτικά encrypted backups! 💾',
          medium: 'Εφαρμόστε Data Loss Prevention (DLP) tools και access controls! 🔐'
        }
      }
    };
    
    return {
      theme: theme,
      text: recommendations[category]?.[theme]?.[priority] || 'Συνεχίστε να βελτιώνετε τις γνώσεις σας σε αυτόν τον τομέα! 📚',
      priority: priority
    };
  };

  const completeQuiz = () => {
    const correctCount = userAnswers.filter(a => a.isCorrect).length;
    const totalQuestions = questions.length;
    const scorePercentage = Math.round((correctCount / totalQuestions) * 100);
    
    const themeScores = {};
    questions.forEach((q, idx) => {
      if (!themeScores[q.theme]) {
        themeScores[q.theme] = { correct: 0, total: 0 };
      }
      themeScores[q.theme].total++;
      if (userAnswers[idx]?.isCorrect) {
        themeScores[q.theme].correct++;
      }
    });
    
    const theme_scores = {};
    Object.keys(themeScores).forEach(theme => {
      theme_scores[theme] = Math.round(
        (themeScores[theme].correct / themeScores[theme].total) * 100
      );
    });
    
    let performance_level = 'beginner';
    if (scorePercentage >= 90) performance_level = 'expert';
    else if (scorePercentage >= 75) performance_level = 'advanced';
    else if (scorePercentage >= 60) performance_level = 'intermediate';
    
    const finalResults = {
      total_score: scorePercentage,
      correct_answers: correctCount,
      total_questions: totalQuestions,
      performance_level: performance_level,
      theme_scores: theme_scores,
      recommendations: generateRecommendations({
        total_score: scorePercentage,
        theme_scores: theme_scores
      }, category)
    };

    setResults(finalResults);
    setStage('results');
  };

  if (stage === 'category') {
    return (
      <>
                <div className="min-h-screen animated-bg p-8" style={{ position: 'relative', zIndex: 1 }}>
          <div className="max-w-6xl mx-auto">
            <div className="text-center mb-16 animate-fade-in">
              <div className="flex items-center justify-center mb-6">
                <Shield className="w-20 h-20 text-cyan-400 animate-pulse" />
              </div>
              <h1 className="text-6xl font-bold text-white mb-4 bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400">
                CyberSafe Quiz
              </h1>
              <p className="text-xl text-gray-300">Αξιολόγηση Κυβερνοασφάλειας & Ψηφιακού Γραμματισμού</p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {categories.map((cat) => (
                <button
                  key={cat.id}
                  onClick={() => startSession(cat.id)}
                  className="group relative overflow-hidden rounded-2xl bg-white/10 backdrop-blur-lg border border-white/20 p-8 hover:scale-105 hover:bg-white/20 transition-all duration-300 shadow-2xl"
                >
                  <div className={`absolute inset-0 bg-gradient-to-br ${cat.color} opacity-0 group-hover:opacity-20 transition-opacity duration-300`} />
                  <div className="relative z-10">
                    <div className="text-6xl mb-4">{cat.icon}</div>
                    <h3 className="text-2xl font-bold text-white mb-2">{cat.name}</h3>
                    <p className="text-gray-300">{cat.description}</p>
                    <div className="mt-6 flex items-center justify-center text-cyan-400 group-hover:text-cyan-300">
                      <span className="mr-2">Ξεκίνα</span>
                      <TrendingUp className="w-5 h-5" />
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>
      </>
    );
  }

  if (stage === 'demographics') {
  return (
    <div className="min-h-screen animated-bg">
      <DemographicsForm
        category={category}
        onSubmit={saveDemographics}
        onBack={() => setStage('category')}
      />
    </div>
  );
}

  if (stage === 'quiz' && questions.length > 0) {
    const question = questions[currentQuestion];
    const progress = ((currentQuestion + 1) / questions.length) * 100;

    return (
      <>
               <div className="min-h-screen animated-bg p-8" style={{ position: 'relative', zIndex: 1 }}>
          <div className="max-w-4xl mx-auto">
            <div className="mb-8">
              <div className="flex justify-between text-white mb-2">
                <span>Ερώτηση {currentQuestion + 1} από {questions.length}</span>
                <span>{Math.round(progress)}%</span>
              </div>
              <div className="h-3 bg-white/20 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-gradient-to-r from-cyan-400 to-purple-500 transition-all duration-500"
                  style={{ width: `${progress}%` }}
                />
              </div>
            </div>

            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20 mb-6">
              <div className="flex items-start mb-6">
                <AlertTriangle className="w-8 h-8 text-yellow-400 mr-4 flex-shrink-0" />
                <h3 className="text-2xl font-bold text-white">{question.question_text}</h3>
              </div>

              <div className="space-y-4">
                {Object.entries(question.options).map(([key, value]) => (
                  <button
                    key={key}
                    onClick={() => submitAnswer(key)}
                    disabled={showFeedback}
                    className={`w-full text-left p-6 rounded-xl border-2 transition-all duration-300 ${
                      showFeedback
                        ? key === question.correct_answer
                          ? 'bg-green-500/30 border-green-400'
                          : key === lastAnswer?.userAnswer
                          ? 'bg-red-500/30 border-red-400'
                          : 'bg-white/5 border-white/20'
                        : 'bg-white/10 border-white/30 hover:bg-white/20 hover:border-cyan-400'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <span className="text-2xl font-bold text-cyan-400 mr-4">{key.toUpperCase()}</span>
                        <span className="text-white text-lg">{value}</span>
                      </div>
                      {showFeedback && key === question.correct_answer && (
                        <CheckCircle className="w-6 h-6 text-green-400" />
                      )}
                      {showFeedback && key === lastAnswer?.userAnswer && key !== question.correct_answer && (
                        <XCircle className="w-6 h-6 text-red-400" />
                      )}
                    </div>
                  </button>
                ))}
              </div>

              {showFeedback && (
                <div className={`mt-6 p-6 rounded-xl ${lastAnswer.isCorrect ? 'bg-green-500/20 border-2 border-green-400' : 'bg-red-500/20 border-2 border-red-400'}`}>
                  <div className="flex items-center mb-3">
                    {lastAnswer.isCorrect ? (
                      <>
                        <CheckCircle className="w-6 h-6 text-green-400 mr-2" />
                        <span className="text-green-400 font-bold text-xl">Σωστά! 🎉</span>
                      </>
                    ) : (
                      <>
                        <XCircle className="w-6 h-6 text-red-400 mr-2" />
                        <span className="text-red-400 font-bold text-xl">Λάθος</span>
                      </>
                    )}
                  </div>
                  <p className="text-white mb-4">{lastAnswer.explanation}</p>
                  <button
                    onClick={nextQuestion}
                    className="bg-gradient-to-r from-cyan-500 to-purple-500 text-white px-8 py-3 rounded-lg font-bold hover:shadow-2xl hover:scale-105 transition-all duration-300"
                  >
                    {currentQuestion < questions.length - 1 ? 'Επόμενη Ερώτηση' : 'Δες Αποτελέσματα'}
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </>
    );
  }

  if (stage === 'results' && results) {
    const themeData = Object.entries(results.theme_scores).map(([name, score]) => ({
      theme: name.replace('_', ' '),
      score: score,
      fullMark: 100
    }));

    const performanceColor = {
      expert: 'text-green-400',
      advanced: 'text-blue-400',
      intermediate: 'text-yellow-400',
      beginner: 'text-orange-400'
    };

    return (
      <>
               <div className="min-h-screen animated-bg p-8" style={{ position: 'relative', zIndex: 1 }}>
          <div className="max-w-6xl mx-auto">
            <div className="text-center mb-12">
              <Award className="w-24 h-24 text-yellow-400 mx-auto mb-6 animate-bounce" />
              <h1 className="text-5xl font-bold text-white mb-4">Συγχαρητήρια!</h1>
              <div className="text-8xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-400 mb-4">
                {results.total_score}%
              </div>
              <p className="text-2xl text-gray-300">
                Επίπεδο: <span className={`font-bold ${performanceColor[results.performance_level]}`}>
                  {results.performance_level.toUpperCase()}
                </span>
              </p>
              <p className="text-gray-400 mt-2">
                {results.correct_answers} / {results.total_questions} σωστές απαντήσεις
              </p>
            </div>

            <div className="grid md:grid-cols-2 gap-8 mb-12">
              <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
                <h3 className="text-xl font-bold text-white mb-4 flex items-center">
                  <Target className="w-6 h-6 mr-2 text-cyan-400" />
                  Επίδοση ανά Θεματική
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={themeData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#ffffff20" />
                    <XAxis dataKey="theme" tick={{ fill: '#fff' }} />
                    <YAxis tick={{ fill: '#fff' }} />
                    <Tooltip contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '8px' }} />
                    <Bar dataKey="score" fill="url(#colorGradient)" radius={[8, 8, 0, 0]} />
                    <defs>
                      <linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stopColor="#06b6d4" />
                        <stop offset="100%" stopColor="#a855f7" />
                      </linearGradient>
                    </defs>
                  </BarChart>
                </ResponsiveContainer>
              </div>

              <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
                <h3 className="text-xl font-bold text-white mb-4">Ραντάρ Επίδοσης</h3>
                <ResponsiveContainer width="100%" height={300}>
                  <RadarChart data={themeData}>
                    <PolarGrid stroke="#ffffff30" />
                    <PolarAngleAxis dataKey="theme" tick={{ fill: '#fff', fontSize: 12 }} />
                    <PolarRadiusAxis tick={{ fill: '#fff' }} />
                    <Radar name="Score" dataKey="score" stroke="#06b6d4" fill="#06b6d4" fillOpacity={0.5} />
                  </RadarChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
              <h3 className="text-2xl font-bold text-white mb-6 flex items-center">
                <BookOpen className="w-7 h-7 mr-3 text-purple-400" />
                Προτάσεις Βελτίωσης
              </h3>
              <div className="space-y-4">
                {results.recommendations.map((rec, idx) => (
                  <div
                    key={idx}
                    className={`p-6 rounded-xl border-2 ${
                      rec.priority === 'high' ? 'bg-red-500/20 border-red-400' : rec.priority === 'medium' ? 'bg-yellow-500/20 border-yellow-400' : 'bg-green-500/20 border-green-400'
                    }`}
                  >
                    <div className="flex items-start">
                      <AlertTriangle className={`w-6 h-6 mr-3 flex-shrink-0 ${rec.priority === 'high' ? 'text-red-400' : rec.priority === 'medium' ? 'text-yellow-400' : 'text-green-400'}`} />
                      <div>
                        <h4 className="text-white font-bold mb-2">{rec.theme.toUpperCase()}</h4>
                        <p className="text-gray-

                        200">{rec.text}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="text-center mt-12">
              <button
                onClick={() => window.location.reload()}
                className="bg-gradient-to-r from-cyan-500 to-purple-500 text-white px-12 py-4 rounded-lg font-bold text-lg hover:shadow-2xl hover:scale-105 transition-all duration-300"
              >
                Νέο Quiz
              </button>
            </div>
          </div>
        </div>
      </>
    );
  }

  return <div>Loading...</div>;
};

export default CyberQuizApp;