// student_helper.js

// Save signup data temporarily
function saveSignupData(data) {
    localStorage.setItem("signupData", JSON.stringify(data));
  }
  
  // Save full profile to both 'user' and 'students'
  function saveUserProfile(profile) {
    localStorage.setItem("user", JSON.stringify(profile));
    let allStudents = JSON.parse(localStorage.getItem("students")) || [];
    allStudents.push(profile);
    localStorage.setItem("students", JSON.stringify(allStudents));
  }
  
  // Get all students from localStorage
  function getAllStudents() {
    return JSON.parse(localStorage.getItem("students")) || [];
  }
  
  // Get registered courses by department, level, and semester
  function getRegisteredCourses(department, level, semester) {
    const key = `${department.toLowerCase()}_${level}_${semester.toLowerCase()}_registered`;
    return JSON.parse(localStorage.getItem(key)) || [];
  }
  
  // Combined Smart Search: name, matric, department, level, semester, course title/code
  function smartSearchStudent(query) {
    const students = getAllStudents();
    const q = query.toLowerCase();
  
    return students.filter(s => {
      const nameMatch = s.fullname?.toLowerCase().includes(q);
      const matricMatch = s.matric?.toLowerCase().includes(q);
      const deptMatch = s.department?.toLowerCase().includes(q);
      const levelMatch = s.level?.toLowerCase().includes(q);
  
      const courseMatch = ["first", "second"].some(sem => {
        const key = `${s.department.toLowerCase()}_${s.level}_${sem}_registered`;
        const courses = JSON.parse(localStorage.getItem(key)) || [];
        return courses.some(c => c.title?.toLowerCase().includes(q) || c.code?.toLowerCase().includes(q));
      });
  
      return nameMatch || matricMatch || deptMatch || levelMatch || courseMatch;
    });
  }
  
  // Display student search results inside any container
  function renderStudentResults(students, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
  
    if (students.length === 0) {
      container.innerHTML = '<p style="color:red">No matching student found.</p>';
      return;
    }
  
    container.innerHTML = students.map(student => `
      <div style="margin-bottom: 15px; padding: 10px; background: #f1f1f1; border-radius: 10px;">
        <p><strong>Name:</strong> ${student.fullname}</p>
        <p><strong>Matric Number:</strong> ${student.matric}</p>
        <p><strong>Department:</strong> ${student.department}</p>
        <p><strong>Level:</strong> ${student.level}</p>
      </div>
    `).join('');
  }
  
  // Validate required profile fields
  function isValidProfile(profile) {
    return (
      profile.fullname &&
      profile.password &&
      profile.department &&
      profile.year
    );
  }
  
  // Export for global use
  window.StudentHelper = {
    saveSignupData,
    saveUserProfile,
    getAllStudents,
    getRegisteredCourses,
    smartSearchStudent,
    renderStudentResults,
    isValidProfile
  };
  