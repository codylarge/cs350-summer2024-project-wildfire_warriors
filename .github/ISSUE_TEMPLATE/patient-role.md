---
name: Patient Role
about: 'Patient''s role in a Hospital Management System '
title: ''
labels: ''
assignees: ''

---

**As a patient** [role]
**I need to view my medical records and appointments** [function]
**So that I can stay informed about my health** [benefit]
### Details and Assumptions
* Patients have limited access to their own medical records
* They can view past and upcoming assignments
* They can seed their diagnoses treatments, and prescriptions
### Acceptance Criteria
```gherkin
Given a patient is logged into their system
When the patient navigates to their medical records page
Then the patient can view their own medical records and appointment history 
```
