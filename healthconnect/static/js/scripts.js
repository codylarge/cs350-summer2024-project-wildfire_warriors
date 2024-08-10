
document.addEventListener("DOMContentLoaded", function() {
    var roleField = document.getElementById("id_role");
    var primaryDoctorField = document.getElementById("id_primary_doctor");
    roleField.addEventListener("change", function() {
        if (this.value === "patient") {
            primaryDoctorField.style.display = "block";
            primaryDoctorField.setAttribute("required", "required");
        } else {
            primaryDoctorField.style.display = "none";
            primaryDoctorField.removeAttribute("required");
        }
    });
    // Trigger the change event on page load to ensure the correct initial state
    roleField.dispatchEvent(new Event('change'));
});