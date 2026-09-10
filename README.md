PRT581 Group Assessment 2 — FIFA World Cup 2026 Data Analysis

A group project analysing FIFA World Cup 2026 match and player data using Python. Each team member investigated a distinct analytic question using data wrangling, sampling, descriptive statistics, confidence intervals, and hypothesis testing (one-sample or two-sample t-test).

Project Objective

Per the assignment brief, each team member completed an independent analytic task on FIFA World Cup 2026 data, applying the full data science pipeline covered in Weeks 1–5:

Analytic question formulation
Data wrangling
Data preparation and sampling
Descriptive statistics
Inferential statistics — confidence interval
Inferential statistics — one-sample or two-sample t-test
Project Structure
Folder	Task	Author
Task1_Passing Analysis per 90 minutes	Passing performance analysis	Indra Thanet
Task2_BallPossession	Ball possession vs match outcome	Manish
Task3_UEFA_CAF_AttemptsAtGoal	Attempts at goal (UEFA vs CAF confederations)	Rojin Pradhan
Task4_Goalkeeping_Defence	Goalkeeping and defensive performance	Shishir Rai

Each folder contains that team member's own Python scripts, cleaned data, result screenshots, and a task-specific README with their full methodology and findings.

Task Summaries
Task 1 — Passing Analysis (Indra Thanet)

Investigates passing performance per 90 minutes. See Task1_Passing Analysis per 90 minutes/ for full methodology and results.

Task 2 — Ball Possession and Match Outcome (Manish)

Analytic question: Is there a statistically significant difference in average ball possession percentage between teams that win their matches and teams that lose their matches at the FIFA World Cup 2026?

Method: A random sample of n = 40 matches was drawn from each group (winning teams, losing teams). Descriptive statistics, 95% confidence intervals, and a Welch's two-sample t-test were used to compare the two groups.

Result: Winning teams averaged 50.15% possession versus 40.42% for losing teams — a statistically significant difference (t* = 5.15, p = 0.0000019). The null hypothesis was rejected: winning teams hold significantly more possession than losing teams at this tournament.

See Task2_BallPossession/README.md for the full report, including methodology, assumption checks, and limitations.

Task 3 — Attempts at Goal: UEFA vs CAF (Rojin Pradhan)

Compares attempts at goal between teams from the UEFA (Europe) and CAF (Africa) confederations. See Task3_UEFA_CAF_AttemptsAtGoal/ for full methodology and results.

Task 4 — Goalkeeping and Defensive Performance (Shishir Rai)

Investigates goalkeeping and defensive performance metrics. See Task4_Goalkeeping_Defence/ for full methodology and results.

How to Run Any Task

Each task folder is self-contained with its own numbered Python scripts, raw/cleaned data, and a README explaining the specific steps. General setup:

Install dependencies:
   pip install pandas numpy scipy matplotlib seaborn openpyxl
Navigate into the relevant task folder.
Run the numbered scripts in order (e.g., 01_...py, 02_...py, ...), as each stage typically depends on the CSV output from the previous stage.
Environment
Python 3.14.7
Conda environment: hit140env
Key libraries: pandas, numpy, scipy, matplotlib, seaborn, openpyxl
Data Sources
FIFA Official Website — https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics
The Stats Don't Lie — https://www.thestatsdontlie.com/football/world-cup-2026/
FBref — https://fbref.com/en/
Team
Name	Task
Indra Thanet	Task 1 — Passing Analysis
Manish	Task 2 — Ball Possession
Rojin Pradhan	Task 3 — Attempts at Goal (UEFA vs CAF)
Shishir Rai	Task 4 — Goalkeeping & Defence
Academic Integrity

This project was completed for PRT581 / HIT140 Assessment 2. Generative AI tools were used for coding assistance, debugging, and documentation support, as declared in the accompanying AI Usage Declaration Form. All analysis, code execution, and conclusions were reviewed and are owned by the respective task authors.