DOCKER_IMAGE = google/cloud-sdk:latest
AUTH_VOLUME = gcloud-config
DOCKER_RUN_CMD_DEV = --rm --volumes-from ${AUTH_VOLUME} -w /app -v ${CURDIR}:/app
DOCKER_ENV_INIT = gcloud auth login && pip install google-cloud-automl

dockerenv:
	docker run -ti --name ${AUTH_VOLUME} ${DOCKER_IMAGE} ${DOCKER_ENV_INIT}

bash: dockerenv
	docker run -ti ${DOCKER_RUN_CMD_DEV} ${DOCKER_IMAGE} /bin/bash

create-model: dockerenv
	docker run ${DOCKER_RUN_CMD_DEV} ${DOCKER_IMAGE} python language_entity_extraction_create_model_test.py


.PHONY: dockerenv bash dev