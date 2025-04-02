from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, get_db
from . import models, schemas
from sqlalchemy.orm import Session
from typing import List
from .routers import difficulty, job, region, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
	title='Jobify API',
	description='The dynamic platform to discover and apply for the best job opportunities in Cameroon. Find a job that fits your skills, preferences, and location. Simple, fast, and efficient.',
	version='0.1'
)

# Configuration CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # Remplacez par une liste spécifique d'origines autorisées
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(difficulty.router, prefix='/api')
app.include_router(region.router, prefix='/api')
app.include_router(job.router, prefix='/api')
app.include_router(user.router)

@app.get('/')
def home():
	return {'greeting': "Welcome to Jobify API! Let\'s find your dream job."}
