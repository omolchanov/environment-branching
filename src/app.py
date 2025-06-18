"""
The Environment Branching strategy — where each environment (dev, stage, prod) maps to a dedicated Git branch —
is a classic and simple CI/CD approach.

How It Works

You have three long-living branches:
- dev: for daily development and integration work.
- stage: for staging/pre-production testing.
- prod: for code ready for release.

Code progresses by merging from one branch to the next (usually via PRs):
feature/* ➜ dev ➜ stage ➜ prod

CI/CD pipelines are triggered per branch:
- Push to dev: deploy to Dev environment.
- Push to stage: deploy to Staging.
- Push to prod: deploy to Production.

Common Flow
- Feature branches are created off dev.
- Developers push features to dev and create PRs.
- When dev is stable, it's merged into stage.
- After QA testing on stage, it's merged into prod.
- Production deploys happen after merging to prod.
  Feature1 --> Dev
  Feature2 --> Dev
  Dev --> Stage
  Stage --> Prod

Test Timing Overview
Stage	             Unit Tests	                Integration Tests	             Acceptance Tests
On Push/PR to dev	Yes (fast feedback)	️        Optional (mocked DB, if quick)	 Skip (too slow)
On Merge to stage	Run again (for safety)	    Yes (real services or test DB)	 Yes (automated end-to-end tests)
Before/On prod deployment	 Smoke check only	On staging	                     Run critical acceptance suite

Feature branch -> run only unit tests on push

"""


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(message="Hello, World!"), 200


@app.route('/feature-1')
def featurer_1():
    return jsonify(message="Feature 1"), 200


if __name__ == '__main__':
    app.run()

