# scos_usrp
USRP support for scos-sensor

Requires pip>=18.1 (upgrade using `python3 -m pip install --upgrade pip`)

 This repository includes many 700MHz band actions in [scos_usrp/configs/actions](scos_usrp/configs/actions). Action
 classes, RadioInterface, GPSInterface, and signals are used from [scos_actions](https://github.com/ntia/scos_actions).

For information on adding actions, see the [scos_actions documentation](https://github.com/ntia/scos_actions).

This plugin requires the UHD drivers to be installed. The easiest way to install the drivers is to use an existing
docker image as the base image. The default base image in scos-sensor (currently set to 
`BASE_IMAGE=docker.pkg.github.com/ntia/scos_usrp/uhd_b2xx_py3:3.13.1.0-rc1`) has the UHD drivers. However, it requires
[authentication to GitHub packages](https://help.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages#authenticating-to-github-packages)
using a
[GitHub personal access token](https://help.github.com/en/packages/publishing-and-managing-packages/about-github-packages#about-tokens).
This is temporary until this repository is made public. ***Alternatively, you can use the image hosted on Docker Hub
without authentication:*** `BASE_IMAGE=smsntia/uhd_b2xx_py3`.

## Running Unit Tests
First set `DOCKER_GIT_CREDENTIALS` by running
`export DOCKER_GIT_CREDENTIALS="$(cat ~/.git-credentials)"` if using git credential manager
or by running
`export DOCKER_GIT_CREDENTIALS=https://<username>:<password>@github.com` replacing \<username\> with your GitHub username
and \<password\> with your GitHub password.
Since the UHD drivers are required for testing, the tests are run inside a container with the UHD drivers.
```base
docker build -f docker/Dockerfile-test -t usrp_test --build-arg DOCKER_GIT_CREDENTIALS .
docker run usrp_test
```
