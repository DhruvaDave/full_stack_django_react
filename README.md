# Introduction

Welcome to Firefly's take-home exercise!

In this exercise, you'll be working on and adding features to an appointment booking system similar to the one we use at Firefly.

This exercise will test you on your ability to work with an existing, full-stack codebase. The technologies used in this exercise are [Django](https://www.djangoproject.com/)/[Django REST Framework](https://www.django-rest-framework.org/), [React](https://reactjs.org/), and [Docker Compose](https://docs.docker.com/compose/). This is a tech-stack similar to what we use here at Firefly, but specific knowledge about these technologies should not be necessary and you should be able to find examples of everything you need in the existing codebase.

We ask that you dedicate no more than 4 hours to this exercise. These technologies may be entirely new to you, and we don't expect a perfect solution. It is perfectly fine to Google, refer to documentation / Stack Overflow, and even install packages that you find useful. Likewise, its fine to leverage workarounds if you get stuck on a specific technology. If this happens, please let us know so we can do better next time!

## What we're looking for

- Can you work with an existing codebase?
- Can you think about the full stack, and connect an API to a user interface?
- Can you produce code that is readable and easily reviewable?
- Can you make design choices and discuss the tradeoffs with us?

## What we are not looking for

- Mastery of specific frameworks/languages/tools
- High-level design skills (other sections of the interview loop will test for this)

## What you'll start with

This exercise involves two data models: Patients and Appointments. Appointments represent blocks of time on a doctor's schedule, which can be booked by a Patient. You will be working to allow the user of the system to book Appointments for Patients.

On the backend, you'll start with:

- Appointment and Patient models
- Appointment Create/Read/Update/Delete (CRUD) API
- Patient CRUD API

On the front-end, you'll start with:

- A component which allows creating a new Appointment
- A component which lists Appointments
- A component which lists Patients

# Your assignment

On the backend, we'd like you to add...

- Model changes and API logic which allow booking an appointment (associating a Patient with an Appointment)

On the front-end, we'd like you to add...

- A component to allow creating a new Patient
- A component which allows the user of the system to book an Appointment for a Patient
- A component to list Appointments and, if an Appointment is booked, each Appointment's associated Patient

## A few opportunities for design choices

We don't expect you to address all of these things in your solution, but here are a few things you might want to think about:

- How do you represent a booked Appointment, in your data model and in the frontend?
- How can we prevent a Patient from booking an already-booked Appointment?
- How might Appointments eventually become specific to one doctor vs. another doctor?
- What is the user's experience around booking an Appointment?
- Is it possible to delete Patients and/or Appointments? If so, what are the effects of doing so?

# Getting started

The existing code in this repo should get you up and running with a web app you can view in your local browser.

The entire stack is built and run with the Docker and Docker Compose tools. If you don't already have those installed, you can follow the instructions at: https://github.com/docker/compose-cli#getting-started.

To get the application up and running:

```shell
docker compose up --build
```

*NOTE:* the Docker step above sometimes takes a long time (>10 minutes) to install the frontend's requirements for the first time. If you are familiar with [yarn](https://yarnpkg.com/), you can cut down on this time by installing those requirements yourself before running the Docker command. To install them yourself, run:  `cd frontend && yarn install`.

Once the application is started, in a browser, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and verify that you see the Django REST Framework Api Root page. From here, you can explore the API.

The frontend is available at [http://127.0.0.1:3000/](http://127.0.0.1:3000/).

## Backend

If you are new to Django, you can focus on the `appointment_booking` directory.

The backend runs using Django and Docker. You can read more about how these work together at https://docs.docker.com/samples/django/.

The base URL for the backend is [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The Api Root page there is a good way to explore the API in the browser. As an example, you can click into "appointments" at [http://127.0.0.1:8000/appointments/](http://127.0.0.1:8000/appointments/) to view a `GET /appointments/` request. To make a request to the existing (but incomplete) endpoint to book an appointment, make a `PATCH` request to [http://127.0.0.1:8000/appointments/{appointment.pk}/book/]([http://127.0.0.1:8000/appointments/{appointment.pk}/book/])

The Django admin site is available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and is a useful way to explore your models and data. You can read more about it [here](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/). The credentials for the admin panel can be created with:

```shell
docker compose exec web python manage.py createsuperuser
```

You can run backend tests with:

```shell
docker compose exec web python manage.py test
```

When making changes to models in Django, you'll also need to run some commands to make and run database migrations:

```shell
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

## Frontend

The frontend app runs was built using React, using the standard `npx create-react-app`.

App.js is a good place to start if you're new to the structure of a React application; the main functionality of the app lives in this file and the component files (/src/components/).


## Working with Docker Compose

For an introduction to this tool, check out the [Docker Compose](https://docs.docker.com/compose/) docs.

The backend and frontend servers run in containers defined by docker-compose.yml: the `web` container for the backend Django app and the `frontend` container for the frontend React app.

To execute a command in a container:

```shell
docker compose exec CONTAINER_NAME YOUR_COMMAND
```


## Installing additional dependencies

If you need to add additional dependencies that you find useful, you will need to install the dependencies after you have edited `package.json` or `requirements.txt`.

For the backend, use:
```shell
docker compose exec web pip install -r requirements.txt
```

For the frontend, use:
```shell
docker compose exec frontend yarn install
```
