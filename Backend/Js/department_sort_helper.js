// This script ensures that when a student signs up and fills in their profile,
// they are automatically added to a department-based structure in localStorage.

function storeByDepartment(profile) {
    const deptKey = `dept_${profile.department.toLowerCase()}`;
  
    // Fetch current department list
    let deptList = JSON.parse(localStorage.getItem(deptKey)) || [];
  
    // Check for duplicate matric
    const exists = deptList.some(s => s.matric === profile.matric);
    if (!exists) {
      deptList.push(profile);
      localStorage.setItem(deptKey, JSON.stringify(deptList));
    }
  }
  
  // Attach this logic inside profile_update.html after successful profile creation
  // Example:
  // storeByDepartment(profile);
  
  // To retrieve all users by department somewhere else:
  function getStudentsByDepartment(dept) {
    const deptKey = `dept_${dept.toLowerCase()}`;
    return JSON.parse(localStorage.getItem(deptKey)) || [];
  }
  
  // Optional: Get all department keys
  function getAllDepartments() {
    const keys = Object.keys(localStorage);
    return keys.filter(k => k.startsWith("dept_")).map(k => k.replace("dept_", ""));
  }
  
  // UI Preview Function (Optional):
  function previewDepartmentStudents(dept, containerId) {
    const container = document.getElementById(containerId);
    const students = getStudentsByDepartment(dept);
  
    if (!students.length) {
      container.innerHTML = `<p>No students found for ${dept}</p>`;
      return;
    }
  
    const table = document.createElement("table");
    table.innerHTML = `
      <thead><tr><th>Matric No</th><th>Name</th><th>Level</th></tr></thead>
      <tbody>
        ${students.map(s => `
          <tr><td>${s.matric}</td><td>${s.fullname}</td><td>${s.level}</td></tr>
        `).join('')}
      </tbody>
    `;
    container.innerHTML = "";
    container.appendChild(table);
  }
  
  // Export functions globally if needed
  window.DepartmentHelper = {
    storeByDepartment,
    getStudentsByDepartment,
    getAllDepartments,
    previewDepartmentStudents
  };
  