# Simple Flask Timer

## Purpose
Just a very simple Flask timer implementation for me to use to test a cluster.

My idea is to use github actions to containerize this project and its dependancies to an image that'll be used
by my cluster to get familiar with how Kubernetes works. The end result is I have an image that I can use to
deploy on the cluster and access the site from exposed ports on the cluster. 


## Future Uses

* I plan to turn this into a CI/CD Pipeline where the CI portion is handled by Github Actions to containerize the
code and its dependancies. The CD portion will be handled by my cluster using some tool to actually use this container
and expose the ports and all that sweet stuff to access the page.

* Without an image, to test the main.py use the following command: `flask --app main.py run -p 5000`, this let's you run
on a test server without having to rebuild an image everytime. However, within the image itself I choose to use Gunicorn
to run the flask application as specified within the Dockerfile.
