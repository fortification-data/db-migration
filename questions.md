# Questions

Do we want to roll-up country-level variables?
    - I.e. "current population" that gets the most recent population?


Digital Ocean VS Heroku?

Python vs Go for db_migration + Backend
    - Likely Python due to easier hires/onboarding


Staging VS Prod environments
    - heroku is good for this for backend BUT
    - digital ocean would require two distinct apps
      - how to link backend environment to frontend?
        - just always have a frontend staging branch/active PR
        - vercel auto-deploys sites based on PRs 🙂
