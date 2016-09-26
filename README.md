# Minimal Docker CI [![Build Status](https://travis-ci.org/mike42/minimal-docker-ci.svg?branch=master)](https://travis-ci.org/mike42/minimal-docker-ci)

This repository shows the sort of plumbing that you would need to use Travis CI
and docker to run tests against a running application as part of CI.

The dockerised example server simply sends "Hello World" to anybody who connects
on port 5000, and has an accompanying `.travis.yml` file which defined the
process of building, testing, and tearing down the container.

Pull requests and suggestions welcome.

### Walkthrough

This example was put together for the blog post: [How to set up Docker containers in Travis CI](https://mike42.me/blog/how-to-set-up-docker-containers-in-travis-ci).

