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
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## Introduction to EngineerX project

EngineerX is an open source web application designed for engineers and specialists letting them share their ideas, create tutorials, represent themselves, employ other specialists and ...

Currently, The project is at it's first steps and includes a simple but awesome [Content Management System (CMS)](https://en.wikipedia.org/wiki/Content_management_system) that lets content providers to create and manage blog posts.

Key features of the project:

- It's [cloud native](https://en.wikipedia.org/wiki/Cloud_native_computing) and can easily get deployed on popular cloud providers like (AWS, Azure and ...)
- It benefits from microservices architectural best practices. It uses technologies like [docker](https://www.docker.com/) and [kubernetes](https://kubernetes.io/) to provide a horizontally scalable infrastructure with high availability.
- It includes a wide range of popular development frameworks and libraries like: [django](https://www.djangoproject.com/), [reactjs](https://reactjs.org/), [nextjs](https://nextjs.org/), [wagtail](https://wagtail.io/) and ...
- It benefits from [TDD](https://en.wikipedia.org/wiki/Test-driven_development) best practices and uses [unittest](https://docs.python.org/3/library/unittest.html#module-unittest), [jest](https://jestjs.io/), [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/) and [cypress](https://www.cypress.io/) for different kinds of tests.
- It uses [Jenkins](https://www.jenkins.io/) declarative pipeline syntax to implement [CI/CD](https://en.wikipedia.org/wiki/CI/CD) pipelines. (Pipeline as code)
- Developers are able to write different kinds of tests and run them in a parallelized and non-blocking manner.
- It uses [Terraform](https://www.terraform.io/) to provision the required cloud infrastructure so it's really easy to deploy the whole project and destroy it whenever it's not needed any more. (Infrastructure as code)
- It has built on top of wagtail. Wagtail enables django developers to have a professional headless CMS which can be customized for many types of businesses.

## What's included
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

The page model has a few fields:

- `sections`: Contains page's content. Check Wagtail's StreamField [Documentation](https://docs.wagtail.io/en/stable/topics/streamfield.html) to know more about it's amazing features. 


## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://reponame/blob/master/CONTRIBUTING.md) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://reponame/issues/new).

## Contributing

Please read through our [contributing guidelines](https://reponame/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, all HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Main author](https://github.com/usernamemainauthor).

Editor preferences are available in the [editor config](https://reponame/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <https://editorconfig.org/>.

## Creators

**Creator 1**

- <https://github.com/usernamecreator1>

## Thanks

Some Text

## Copyright and license

Code and documentation copyright 2011-2018 the authors. Code released under the [MIT License](https://reponame/blob/master/LICENSE).

Enjoy :metal:
