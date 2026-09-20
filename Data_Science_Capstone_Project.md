# Data Science Capstone Project

**Year-Long Project:** Sunday Sessions, Weeks 1–16

Over the next 12–16 weeks, you'll develop a full data science project of your own choosing, from a first idea through a finished analysis you can present. Each Sunday session builds on the last: you'll define a problem, track down real data, explore and clean it, apply techniques you're learning in class, and revise your approach as you learn what the data actually allows. Your approach is expected to change along the way. What matters most right now is a clear, specific problem statement to start from.

## Project Timeline & Milestones

This is the roadmap for the whole project. Each phase has a checkpoint deliverable due at the end of it. These keep the project moving and give you—and your instructor—a chance to catch problems early, before they become a crisis in week 15.

| Phase | Weeks | Focus | Deliverable |
|---|---|---|---|
| **Phase 1: Frame the Problem** | Weeks 1–2 | Brainstorm topics, research feasibility, write and submit your Project Proposal (Parts 1–4 below). | Project Proposal (written) |
| **Phase 2: Find & Understand Your Data** | Weeks 3–5 | Locate real data sources, pull sample data, check for gaps/quality issues, document what you actually have vs. what you hoped for. | Data Inventory + revised data plan |
| **Phase 3: Clean & Explore (EDA)** | Weeks 6–8 | Clean the dataset, handle missing values, build summary stats and visualizations, look for patterns that inform your approach. | EDA Notebook/Report + updated problem statement |
| **Phase 4: Apply Techniques** | Weeks 9–12 | Build and test models or analyses (regression, classification, clustering, etc.), compare approaches, iterate based on results. | Working Model/Analysis + midpoint check-in presentation |
| **Phase 5: Refine & Interpret** | Weeks 13–14 | Improve your model or analysis, evaluate performance honestly, connect results back to your original problem statement. | Draft Results Summary |
| **Phase 6: Present & Reflect** | Weeks 15–16 | Finalize visuals and findings, prepare and deliver a final presentation, write a short reflection on how your approach changed. | Final Presentation + Final Report + Reflection |

## Part 1: Project Proposal

**Due:** End of Phase 1

Your proposal has four parts. Submit it in writing; a page or two is plenty. Nothing here is locked in; you'll revisit and revise it as the project develops.

### 1. Problem Statement

This is the most important part of the assignment. In a few sentences, answer:

- What real-world question or problem are you trying to understand or solve?
- Who would care about the answer, and why does it matter?
- What would “success” look like: a prediction, a classification, an insight, or a recommendation?

Be specific. “I want to study climate change” is too broad. “I want to predict whether a given day will have poor air quality in my city based on weather and traffic patterns” is a problem statement.

### 2. Possible Data Sources

- List 2–3 candidate datasets or data sources, such as public datasets, APIs, surveys you could run, or scraped data.
- For each one, note what it would actually provide and what is uncertain. Is it complete, accessible, and recent enough?
- Note what you would do if your first-choice data source does not work out; you will test this for real in Phase 2.

### 3. Techniques You Intend to Use

- What kind of analysis do you think this needs? For example, classification, regression, clustering, time-series analysis, or NLP.
- What tools or languages do you expect to use? For example, Python, pandas, or scikit-learn.

This is a hypothesis, not a commitment. It is completely fine to say, “I think I’ll need classification, but I’m not sure yet.” You’ll firm this up once you’ve explored real data in Phase 3.

### 4. Known Unknowns

List the open questions you do not have answers to yet: things about your data or approach that you plan to figure out as you go. Revising your plan later is not a failure; it is part of doing data science.

## Part 2: Data Inventory

**Due:** End of Phase 2

Once you have actually gone looking for your data, document what you found:

- Which source(s) did you end up using, and how did they differ from what you originally proposed?
- How much data do you have—rows, time range, categories—and is it enough?
- What is missing, messy, or biased in a way that could affect your project?
- Include a revised problem statement if your understanding of the data has changed.

## Part 3: EDA Report

**Due:** End of Phase 3

After cleaning your data and exploring it, summarize what you learned:

- Key summary statistics and at least three visualizations of your data.
- Patterns, correlations, or surprises you found.
- How this changes—or confirms—your planned approach for Phase 4.

## Part 4: Midpoint Check-In

**Due:** End of Phase 4

Prepare a short in-class presentation of 5–10 minutes covering:

- The technique(s) you applied and why.
- Early results, even if they are rough or unfinished.
- What is working, what is not, and what you plan to try next.

## Part 5: Final Presentation, Report & Reflection

**Due:** End of Phase 6

- **Final Presentation:** 8–12 minutes, covering your problem, data, approach, results, and limitations.
- **Final Report:** A written summary of your project from problem statement through results, 2–4 pages plus visuals/code.
- **Reflection:** Half a page on how your problem statement, data sources, or techniques changed since your original proposal, and why.

## Sample Project (For Reference)

### Problem Statement

> Can I predict how many bikes will be rented from my city’s bike-share program on a given day, based on weather conditions?

### Why It Matters

Bike-share operators need to know how many bikes to have available; understanding weather’s effect could help with planning.

### Possible Data Sources

- City open bike-share trip data, if publicly available.
- Historical weather data, including temperature, precipitation, and wind, from a public weather API.
- A holiday/weekday calendar to capture non-weather effects.

### Techniques (Initial Guess)

- Start with exploratory data analysis: plot rentals versus temperature and rentals versus day of week.
- Try linear regression first because it is simple and interpretable.
- If the relationship looks non-linear, consider a decision tree or random forest regressor.

### Known Unknowns

- It is not yet clear whether the bike-share data will have enough historical range.
- Weather alone may not be predictive enough; day-of-week and holiday features may be needed.
- The real signal might turn out to be something else entirely, such as special events. Revisit this once the data is available.

### How This Might Evolve Across the Term

- **Phase 2:** The city’s bike-share data only goes back 18 months, so the project scope is adjusted to a shorter time window.
- **Phase 3:** EDA shows rentals depend heavily on weekday versus weekend, so day-of-week is added as a key feature.
- **Phase 4:** Linear regression underperforms on rainy days, so the project switches to a random forest model.
- **Phase 5:** Local events such as concerts and marathons explain some outliers; this is noted as a limitation in the final report.

## How You’ll Be Graded

You’ll be graded on the quality of your reasoning and the care you put into each checkpoint:

- Is your problem statement specific and answerable?
- Did you think critically about the limitations of your data?
- Did you genuinely revise your approach based on what you learned, rather than forcing your original plan to fit?

This matters more than whether your final project matches your original proposal exactly. In fact, a project that evolved thoughtfully is a sign that you did this right.
