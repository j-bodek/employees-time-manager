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
lowest value in later jobs. To calculate that value it use following equation
n - length of list of jobs that employee can do and are in current day
T_n - sum of available time of all another employees that are present and able to do n-th job
t_n - time needed to do n-th job
![equation](https://latex.codecogs.com/svg.image?\sum_{k}^{n}\frac{t_n}{T_n}" title="\sum_{k}^{n}\frac{t_n}{T_n})

