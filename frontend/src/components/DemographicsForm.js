import React, { useState } from 'react';
import { User, MapPin, GraduationCap, Briefcase, Wifi } from 'lucide-react';

const DemographicsForm = ({ category, onSubmit, onBack }) => {
  const [formData, setFormData] = useState({
    gender: '',
    ageGroup: '',
    grade: '',
    schoolType: '',
    educationLevel: '',
    location: '',
    employmentSector: '',
    internetFrequency: ''
  });

  const [errors, setErrors] = useState({});

  const handleChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: '' }));
    }
  };

  const validate = () => {
    const newErrors = {};
    
    if (!formData.gender) newErrors.gender = 'Επιλέξτε φύλο';
    if (!formData.ageGroup) newErrors.ageGroup = 'Επιλέξτε ηλικία';
    
    if (category === 'child') {
      if (!formData.grade) newErrors.grade = 'Επιλέξτε τάξη';
      if (!formData.schoolType) newErrors.schoolType = 'Επιλέξτε τύπο σχολείου';
    }
    
    if (category === 'adult' || category === 'professional') {
      if (!formData.educationLevel) newErrors.educationLevel = 'Επιλέξτε επίπεδο εκπαίδευσης';
    }
    
    if (category === 'professional') {
      if (!formData.employmentSector) newErrors.employmentSector = 'Επιλέξτε τομέα απασχόλησης';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = () => {
    if (validate()) {
      onSubmit(formData);
    }
  };

  const getCategoryConfig = () => {
    switch(category) {
      case 'child':
        return {
          title: 'Στοιχεία Μαθητή',
          ages: ['8', '9', '10', '11', '12'],
          grades: ["Γ' Δημοτικού", "Δ' Δημοτικού", "Ε' Δημοτικού", "ΣΤ' Δημοτικού"],
          showGrade: true,
          showSchoolType: true,
          showEducation: false,
          showEmployment: false,
          showInternet: false
        };
      case 'adult':
        return {
          title: 'Στοιχεία Χρήστη',
          ages: ['18-30', '31-45', '46-60', '60+'],
          showGrade: false,
          showSchoolType: false,
          showEducation: true,
          showEmployment: false,
          showInternet: true
        };
      case 'professional':
        return {
          title: 'Επαγγελματικά Στοιχεία',
          ages: ['18-30', '31-45', '46-60', '60+'],
          showGrade: false,
          showSchoolType: false,
          showEducation: true,
          showEmployment: true,
          showInternet: true
        };
      default:
        return {};
    }
  };

  const config = getCategoryConfig();

  return (
    <div className="min-h-screen p-8" style={{ background: 'transparent' }}>
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-8">
          <div className="inline-block p-4 bg-purple-500/20 rounded-full mb-4">
            <User className="w-12 h-12 text-purple-400" />
          </div>
          <h2 className="text-4xl font-bold text-white mb-2">{config.title}</h2>
          <p className="text-gray-300">Συμπληρώστε τα παρακάτω στοιχεία</p>
        </div>

        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
          <div className="space-y-6">
            
            {/* Gender */}
            <div>
              <label className="flex items-center text-white font-semibold mb-3">
                <User className="w-5 h-5 mr-2 text-cyan-400" />
                Φύλο *
              </label>
              <div className="grid grid-cols-3 gap-3">
                {(category === 'child' ? ['Αγόρι', 'Κορίτσι', 'Άλλο'] : ['Άνδρας', 'Γυναίκα', 'Άλλο']).map(option => (
                  <button
                    key={option}
                    type="button"
                    onClick={() => handleChange('gender', option)}
                    className={`p-4 rounded-lg border-2 transition-all duration-300 ${
                      formData.gender === option
                        ? 'bg-cyan-500/30 border-cyan-400 text-white'
                        : 'bg-white/5 border-white/30 text-gray-300 hover:bg-white/10'
                    }`}
                  >
                    <div className="text-2xl">{option === 'Άνδρας' || option === 'Αγόρι' ? '👨' : option === 'Γυναίκα' || option === 'Κορίτσι' ? '👩' : '🧑'}
                    </div>
                    <div className="mt-2 font-medium text-sm">{option}</div>
                  </button>
                ))}
              </div>
              {errors.gender && <p className="text-red-400 text-sm mt-2">{errors.gender}</p>}
            </div>

            {/* Age */}
            <div>
              <label className="flex items-center text-white font-semibold mb-3">
                <GraduationCap className="w-5 h-5 mr-2 text-cyan-400" />
                {category === 'child' ? 'Ηλικία *' : 'Ομάδα Ηλικίας *'}
              </label>
              <div className={`grid ${config.ages.length > 4 ? 'grid-cols-5' : 'grid-cols-4'} gap-3`}>
                {config.ages.map(age => (
                  <button
                    key={age}
                    type="button"
                    onClick={() => handleChange('ageGroup', age)}
                    className={`p-4 rounded-lg border-2 transition-all duration-300 ${
                      formData.ageGroup === age
                        ? 'bg-purple-500/30 border-purple-400 text-white'
                        : 'bg-white/5 border-white/30 text-gray-300 hover:bg-white/10'
                    }`}
                  >
                    <div className="font-bold text-lg">{age}</div>
                  </button>
                ))}
              </div>
              {errors.ageGroup && <p className="text-red-400 text-sm mt-2">{errors.ageGroup}</p>}
            </div>

            {/* Grade (Children only) */}
            {config.showGrade && (
              <div>
                <label className="flex items-center text-white font-semibold mb-3">
                  <GraduationCap className="w-5 h-5 mr-2 text-cyan-400" />
                  Τάξη *
                </label>
                <select
                  value={formData.grade}
                  onChange={(e) => handleChange('grade', e.target.value)}
                  className="w-full bg-white/10 border-2 border-white/30 rounded-lg p-4 text-white focus:border-cyan-400 focus:outline-none"
                  style={{color: 'white'}}
                >
                  <option value="" style={{backgroundColor: '#1e293b'}}>Επιλέξτε...</option>
                  {config.grades.map(grade => (
                    <option key={grade} value={grade} style={{backgroundColor: '#1e293b'}}>{grade}</option>
                  ))}
                </select>
                {errors.grade && <p className="text-red-400 text-sm mt-2">{errors.grade}</p>}
              </div>
            )}

            {/* School Type (Children only) */}
            {config.showSchoolType && (
              <div>
                <label className="flex items-center text-white font-semibold mb-3">
                  <GraduationCap className="w-5 h-5 mr-2 text-cyan-400" />
                  Τύπος Σχολείου *
                </label>
                <div className="grid grid-cols-2 gap-3">
                  {['Δημόσιο', 'Ιδιωτικό'].map(type => (
                    <button
                      key={type}
                      type="button"
                      onClick={() => handleChange('schoolType', type)}
                      className={`p-4 rounded-lg border-2 transition-all duration-300 ${
                        formData.schoolType === type
                          ? 'bg-green-500/30 border-green-400 text-white'
                          : 'bg-white/5 border-white/30 text-gray-300 hover:bg-white/10'
                      }`}
                    >
                      <div className="font-medium">{type}</div>
                    </button>
                  ))}
                </div>
                {errors.schoolType && <p className="text-red-400 text-sm mt-2">{errors.schoolType}</p>}
              </div>
            )}

            {/* Education Level (Adults & Professionals) */}
            {config.showEducation && (
              <div>
                <label className="flex items-center text-white font-semibold mb-3">
                  <GraduationCap className="w-5 h-5 mr-2 text-cyan-400" />
                  Επίπεδο Εκπαίδευσης *
                </label>
                <select
                  value={formData.educationLevel}
                  onChange={(e) => handleChange('educationLevel', e.target.value)}
                  className="w-full bg-white/10 border-2 border-white/30 rounded-lg p-4 text-white focus:border-cyan-400 focus:outline-none"
                >
                  <option value="" style={{backgroundColor: '#1e293b'}}>Επιλέξτε...</option>
                  <option value="Πρωτοβάθμια" style={{backgroundColor: '#1e293b'}}>Πρωτοβάθμια</option>
                  <option value="Δευτεροβάθμια" style={{backgroundColor: '#1e293b'}}>Δευτεροβάθμια</option>
                  <option value="Τριτοβάθμια" style={{backgroundColor: '#1e293b'}}>Τριτοβάθμια</option>
                  <option value="Μεταπτυχιακό" style={{backgroundColor: '#1e293b'}}>Μεταπτυχιακό / Διδακτορικό</option>
                </select>
                {errors.educationLevel && <p className="text-red-400 text-sm mt-2">{errors.educationLevel}</p>}
              </div>
            )}

            {/* Employment Sector (Professionals only) */}
            {config.showEmployment && (
              <div>
                <label className="flex items-center text-white font-semibold mb-3">
                  <Briefcase className="w-5 h-5 mr-2 text-cyan-400" />
                  Τομέας Απασχόλησης *
                </label>
                <select
                  value={formData.employmentSector}
                  onChange={(e) => handleChange('employmentSector', e.target.value)}
                  className="w-full bg-white/10 border-2 border-white/30 rounded-lg p-4 text-white focus:border-cyan-400 focus:outline-none"
                >
                  <option value="" style={{backgroundColor: '#1e293b'}}>Επιλέξτε...</option>
                  <option value="Εκπαίδευση" style={{backgroundColor: '#1e293b'}}>Εκπαίδευση</option>
                  <option value="Πληροφορική" style={{backgroundColor: '#1e293b'}}>Πληροφορική</option>
                  <option value="Δημόσιος Τομέας" style={{backgroundColor: '#1e293b'}}>Δημόσιος Τομέας</option>
                  <option value="Ιδιωτικός Τομέας" style={{backgroundColor: '#1e293b'}}>Ιδιωτικός Τομέας</option>
                  <option value="Άλλο" style={{backgroundColor: '#1e293b'}}>Άλλο</option>
                </select>
                {errors.employmentSector && <p className="text-red-400 text-sm mt-2">{errors.employmentSector}</p>}
              </div>
            )}

            {/* Location */}
            <div>
              <label className="flex items-center text-white font-semibold mb-3">
                <MapPin className="w-5 h-5 mr-2 text-cyan-400" />
                Νομός/Περιοχή (προαιρετικό)
              </label>
              <input
                type="text"
                value={formData.location}
                onChange={(e) => handleChange('location', e.target.value)}
                placeholder="π.χ. Αττική, Θεσσαλονίκη"
                className="w-full bg-white/10 border-2 border-white/30 rounded-lg p-4 text-white placeholder-gray-400 focus:border-cyan-400 focus:outline-none"
              />
            </div>

            {/* Internet Frequency */}
            {config.showInternet && (
              <div>
                <label className="flex items-center text-white font-semibold mb-3">
                  <Wifi className="w-5 h-5 mr-2 text-cyan-400" />
                  Συχνότητα Χρήσης Διαδικτύου
                </label>
                <div className="grid grid-cols-3 gap-3">
                  {['Καθημερινά', 'Εβδομαδιαία', 'Σπάνια'].map(freq => (
                    <button
                      key={freq}
                      type="button"
                      onClick={() => handleChange('internetFrequency', freq)}
                      className={`p-4 rounded-lg border-2 transition-all duration-300 ${
                        formData.internetFrequency === freq
                          ? 'bg-blue-500/30 border-blue-400 text-white'
                          : 'bg-white/5 border-white/30 text-gray-300 hover:bg-white/10'
                      }`}
                    >
                      <div className="font-medium text-sm">{freq}</div>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Buttons */}
          <div className="flex gap-4 mt-8">
            <button
              onClick={onBack}
              className="flex-1 bg-white/10 hover:bg-white/20 text-white py-4 rounded-lg font-bold text-lg transition-all duration-300 border-2 border-white/30"
            >
              ← Πίσω
            </button>
            <button
              onClick={handleSubmit}
              className="flex-1 bg-gradient-to-r from-cyan-500 to-purple-500 hover:shadow-2xl hover:scale-105 text-white py-4 rounded-lg font-bold text-lg transition-all duration-300"
            >
              Συνέχεια στο Quiz →
            </button>
          </div>

          <p className="text-gray-400 text-sm text-center mt-4">
            * Υποχρεωτικά πεδία | Τα στοιχεία σας παραμένουν ανώνυμα
          </p>
        </div>
      </div>
    </div>
  );
};

export default DemographicsForm;