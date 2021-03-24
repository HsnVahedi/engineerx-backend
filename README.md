<p align="center">

  <h3 align="center">EngineerX Backend Microservices</h3>

  <p align="center">
    <a href="https://github.com/HsnVahedi/engineerx-backend/issues/new">Report bug</a>
    ·
    <a href="https://github.com/HsnVahedi/engineerx-backend/issues/new">Request feature</a>
  </p>
</p>


## Table of contents

- [Introduction to EngineerX project](#introduction-to-engineerx-project)
- [EngineerX Backend Microservices](#engineerx-backend-microservices)
- [Run Development Environment](#run-development-environment)
- [Run Production Environment](#run-production-environment)
- [EngineerX code repositories](#engineerx-code-repositories)





## Introduction to EngineerX project

EngineerX is an open source web application designed for engineers and specialists. It lets them share their ideas, create tutorials, represent themselves, employ other specialists and ...

Currently, The project is at it's first steps and includes a simple but awesome [Content Management System (CMS)](https://en.wikipedia.org/wiki/Content_management_system) that lets content providers to create and manage blog posts.

Key features of the project:

- It's [cloud native](https://en.wikipedia.org/wiki/Cloud_native_computing) and can easily get deployed on popular cloud providers like (AWS, Azure and ...)
- It benefits from microservices architectural best practices. It uses technologies like [docker](https://www.docker.com/) and [kubernetes](https://kubernetes.io/) to provide a horizontally scalable infrastructure with high availability.
- It includes a wide range of popular development frameworks and libraries like: [django](https://www.djangoproject.com/), [reactjs](https://reactjs.org/), [nextjs](https://nextjs.org/), [wagtail](https://wagtail.io/) and ...
- It benefits from [TDD](https://en.wikipedia.org/wiki/Test-driven_development) best practices and uses [unittest](https://docs.python.org/3/library/unittest.html#module-unittest), [jest](https://jestjs.io/), [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/) and [cypress](https://www.cypress.io/) for different kinds of tests.
- It uses [Jenkins](https://www.jenkins.io/) declarative pipeline syntax to implement [CI/CD](https://en.wikipedia.org/wiki/CI/CD) pipelines. (Pipeline as code)
- Developers are able to write different kinds of tests and run them in a parallelized and non-blocking manner. In other words, testing environment is also elastic and scalable.
- It uses [Terraform](https://www.terraform.io/) to provision the required cloud infrastructure so it's really easy to deploy the whole project and destroy it whenever it's not needed any more. (Infrastructure as code)
- It's built on top of wagtail. Wagtail enables django developers to have a professional headless CMS which can be customized for many types of businesses.




## engineerx-backend-microservices
This repository contains the project's backend microservices. The most important microservice is a django project located [here](https://github.com/HsnVahedi/engineerx-backend/tree/main/engineerx), which is created by wagtail.

Wagtail has many built-in features including Elastic Search integration. To see all of wagtail's built-in features, check [this](https://wagtail.io/features/#) out.

Here is our blog's PostPage which inherits wagtail's Page:

    class PostPage(Page):
        image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
        )
        sections = StreamField(SectionsBlock())
        tags = ClusterTaggableManager(through=TaggedPost, blank=True)

        api_fields = [
            APIField('image', serializer=ImageRenditionField('min-1500x200')),
            APIField('image_16x9', serializer=ImageRenditionField('fill-1600x900-c70', source='image')),
            APIField('sections'),
            APIField('tags'),
            APIField('owner_info'),
        ]

        content_panels = Page.content_panels + [
            ImageChooserPanel('image'),
            StreamFieldPanel('sections'),
            FieldPanel('tags')
        ]
        ...

The page model has a few fields:

- `sections`: Contains page's content. Check Wagtail's StreamField [Documentation](https://docs.wagtail.io/en/stable/topics/streamfield.html) to know more about it's amazing features.
- `api_fields`: These read-only fields are required to expose page's information through REST api.
- `content_panels`: These panels are used by wagtail to create an appropriate django form for the page.





## Run Development Environment

#### 1. Clone this repository:
    git clone https://github.com/HsnVahedi/engineerx-backend
#### 2. Build the docker image:
    cd engineerx-backend/engineerx
    docker build . -t engineerx-backend-django:latest
#### 3. Run the docker container and publish it's port:
    docker run -it -p 8000:8000 engineerx-backend-django:latest bash
#### 4. Create development database:
    python manage.py makemigrations && python manage.py migrate
#### 5. Initialize the database with randomly generated objects:
    mkdir media && mv -vn downloads/ media/downloads/
    python manage.py initdb
#### 6. Create an admin user:
    python manage.py createsuperuser
#### 7. Start the development server:
    python manage.py runserver 0.0.0.0:8000
    
Now you can see the project is running on `127.0.0.1:8000/`. Now go to `127.0.0.1:8000/admin` and login if required.





## Run Production Environment

#### 1. Clone this repository:
    git clone https://github.com/HsnVahedi/engineerx-backend
#### 2. Pull the required docker images:
    cd engineerx-backend
    docker-compose pull
#### 3. Start the production server:
    docker-compose up
#### 4. Now open another terminal and execute bash in the django container:
    docker-compose exec backend bash
#### 5. Initialize the database with randomly generated objects:
    python manage.py initdb
#### 6. Create an admin user:
    python manage.py createsuperuser

Now you can see the project is running on `127.0.0.1:8000/`. Now go to `127.0.0.1:8000/admin` and login if required.




## EngineerX code repositories

EngineerX is a big project and consists of several code bases:

- [engineerx-aws-cli](https://github.com/HsnVahedi/engineerx-aws-cli)
- [engineerx-aws-infrastructure](https://github.com/HsnVahedi/engineerx-aws-infrastructure)
- [engineerx-aws-deployment](https://github.com/HsnVahedi/engineerx-aws-deployment)
- [engineerx-backend](https://github.com/HsnVahedi/engineerx-backend)
- [engineerx-frontend](https://github.com/HsnVahedi/engineerx-frontend)
- [engineerx-integration](https://github.com/HsnVahedi/engineerx-integration)
- [engineerx-backend-unittest](https://github.com/HsnVahedi/engineerx-backend-unittest)
- [engineerx-frontend-unittest](https://github.com/HsnVahedi/engineerx-frontend-unittest)
- [engineerx-integration-test](https://github.com/HsnVahedi/engineerx-integration-test)
- [engineerx-efs-pv](https://github.com/HsnVahedi/engineerx-efs-pv)
- [engineerx-efs-pvc](https://github.com/HsnVahedi/engineerx-efs-pvc)
- [engineerx-backend-latest-tag](https://github.com/HsnVahedi/engineerx-backend-latest-tag)
- [engineerx-frontend-latest-tag](https://github.com/HsnVahedi/engineerx-frontend-latest-tag)
