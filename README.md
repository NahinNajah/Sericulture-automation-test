Sericulture application is a web-based database software, that holds project-specific data
about every recipient benefited from the Bangladesh Silk Development Board. Furthermore,
Which offers data dependability and integrity. Guarantee privacy, consistency, and accuracy
of data. The system allows admin to add or delete users data. The application implements
CRUD operation for admin to create projects carried out by the Bangladesh Silk Development
Board (BSDB), classification system have been implemented to categorize different types of
project. various sub-items associated with different project types to store relevant projectspecific
information. For report filtering it provide choices depending on specified criteria,
such as District, Upazila, Center, Code, National ID (NID), and type, to create customized
report. Ensures that admin users generates report that offer insightful analysis of beneficiary
data. Additionally, admin user can directly pay the beneficiaries their fund from the system by
selecting specific user.
These are some basic functionality and workflow performed by the system, where all functional
test are executed by manually and also with help of automation tools.

For the unit test I decided to work with selenium automation tool, where I have tested a
bulk amount of beneficiary data insertion from a excel file. Selenium allow testers to run tests
directly on their desired browser, drive interactions on requisite web pages, and rerun them
without any manual input. It supports variety of programming languages, though i chose to
work using python.
At first, I had to install the correct version of chrome driver following that, all necessary selenium
library to conduct the test. This unit test is planned in a way, that it takes all necessary input
field information from a excel file for adding new beneficiary data in the form. Hence, all
required actions are performed without any necessary of manual input. In order to pass verdict
for the automation test, the following scenario is to be considered:
• The test is considered ”Pass”, if the browser is fully loaded and user authentication is
successful and it is successfully entering the beneficiaries data in the application.
• The test is considered as ”Failed”, if the browser is not loaded and redirected to required
pages, furthermore it is not saving any data from excel file.
To achieve the desired result selenium extracts the required element from web HTML source.
After that the web- driver executes the task as instructed in the code.
