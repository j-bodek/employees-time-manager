# employees-time-manager
Web application which take as input:
- employee info (employee id, presence, which job levels is he able to do)
- time needed to do job in every level per day

And output most optimal distribution of employees time to show if in any of
job levels is shortage of available time.

# Technologies used to build it:
- Python
- Django
- JavaScript
- HTML
- CSS
- PostgreSQL

# How it works?
After user add employees info to table then he can send csv file which specify 
amount of time needed for every job level per day (there is 10 job levels).
Then algorithm starts distributing employees time from highest level jobs
(for example level 10 is more important to do then level 6). Firstly it find 
all employees that are able to do this job then pick from them one which has 
lowest value in later jobs. To calculate that value it

\[ \sum_{n=1}^{\infty} 2^{-n} = 1 \]
