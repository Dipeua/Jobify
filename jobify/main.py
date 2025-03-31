from fastapi import FastAPI

app = FastAPI(
	title='Jobify API',
	description='The dynamic platform to discover and apply for the best job opportunities in Cameroon. Find a job that fits your skills, preferences, and location. Simple, fast, and efficient.',
	version='0.1'
)

@app.get('/')
def home():
	return {'greeting': "Welcome to Jobify API! Let\'s find your dream job."}