# Immediate things to do:

- [X] Add company model to store company names, id, description, sector, size (number of employees) etc...
- [X] Each user should be linked to a company id, so add that in the user model and in the registration HTML
- [X] Create a questionnaire based on the MBIT test for burnout (this should be in the forms.py)
- [X] Edit user profile page so the user can change their usernames, password, and image potentially, add name first and last as well, date of birth
- [X] Create a history page as well for the user to see past results of the questionnaire

# Long-term to-do list:

- [X] Implement role systems so different roles see different pages
- [X] Managers can view other subordinate results on a separate tab/page
- [X] Work on building a more resilient logic of burnout
- [X] Figure out potential solutions to fixing/remediating burnout (resources as a separate tab with solutions and explanations)
- [X] HIPPA compliency?
- [X] Figure out how to deploy application to AWS
- [ ] Figure out how to create a marketing/onboarding strategy to get early customers
- [ ] Figure out how to make money on the app

  - [ ] Sponsored articles and links
  - [ ] SaaS for business at low cost
  - [ ] ETC...
- [ ] Figure out how to setup postgre/mysql/mariadb etc... instead of sqlite for aws

## Subtasks:

* Check logic is same everywhere for results (using scaled score /132 strategy) (1-2 hours more of work)
* Make sure all UI forms are submittable with no issues by testing them (2-3 hours)
* Come up with advanced report analytics possible for HR page (2-3 hours)
* Come up with new features for the app (2 hour brainstorm)
* Find which is easier to migrate to postgre/mysql/mariadb for the long run in aws and implement in aws (4-5 hours)
* Logic for checking if the test page is not working, it shows test even when test is taken for that month
