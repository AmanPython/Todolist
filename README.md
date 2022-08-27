# Django Rest Framework
## About

- [Environment Setup](#environment-setup)
- [Models and Custom user model](#models-and-custom-user-model)
- [User Registration](#user-registration)
- [JWT Authentication](#jwt-authentication)
- [User Login](#user-login) 
- [Sending Email](#sending-email)
- [User Email Verification](#user-email-verification)
- [Unittesting](#unittesting)
- [Viewsets and urls](#viewsets-and-urls)
- [Generic API Views](#generic-api-views)
- [CORS and REST](#cors-and-rest)
- [Django Template and Static Setup](#django-template-and-static-setup)
- [Pagination Support](#pagination-support)
- [API Documentation](#api-documentation)
- [Postman documentation integration](#postman-documentation-integration)
- [Protect documentation views](#protect-documentation-views)
- [Admin and models](#admin-and-models)
- [Test coverage and reporting](#test-coverage-and-reporting)
- [Github + Travis ci integration](#github--travis-ci-integration)
- [Deployment](#deployment)

## Environment Setup 
   - Creating Django Project
     - django-admin startproject todolistapi .
   - Virtual Environment Setup
     - Create virtual Environment
     > virtualenv DRF
     - Activate virtual Environment
     > source DRF/bin/activate
     - Install the Requirments
     > pip3 install -r requirements.txt
   - Settings.py
     - INSTALLED_APPS = [
     - 'rest_framework',
     - ]
   - Creating New Apps
     - python manage.py startapp todos
     - python manage.py startapp authentication
   - Update Setings.py
     - INSTALLED_APPS = [
     - 'todos',
     - 'authentication',
     ]
   - Initialize Git
     - git init
     - Adding .gitignore file

     
## Models and Custom user model
   - Creating a Tracking Model (Step - 1)
     - Create helpers folder
     - __init__.py
     - models.py
   - Writing code in models.py
     ```
     from django.db import models
     class TrackingModel(models.Model):
         created_at = models.DateTimeField(auto_now_add = True)
         updated_at = models.DateTimeField(auto_now = True)
         class Meta:
            abstract = True
            ordering = ('-created_at')
     ```
   - Edit Authentication Model
     ```
     from django.db import models
     from helpers.models import TrackingModel
     
     class User(TrackingModel):
         pass
     ```     
   - Updating a Tracking Model (Step - 2)
     - Edit Authentication Model
     ```
     from django.contrib.auth.models import (PermissionMixin,BaseUserManager,AbstractBaseUser)
     
     class User(AbstractBaseUser,PermissionMixin,BaseUserManage):
     username_validator = UnicodeUsernameValidator()          // copying from PermissionMixin > AbstractUser
     
     class MyUserManager(UserManager):
        pass
     
     ```
     - Update Settings.py
       - AUTH_USER_MODEL = "authentication.User"
       git commit id - 2b705ac0dd7bc06782563d8e4d85c2fd327e6092
  
  
## User Registration
## JWT Authentication
## User Login
## Sending Email
## User Email Verification
## Unittesting
## Viewsets and urls
## Generic API Views
## CORS and REST
## Django Template and Static Setup
## Pagination Support
## API Documentation
## Postman documentation integration
## Protect documentation views
## Admin and models
## Test coverage and reporting
## Github + Travis ci integration
## Deployment

