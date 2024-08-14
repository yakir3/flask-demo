NAME = yakir/picProject
VERSION = 1.1
DOCKER_REGISTRY = hub.docker.com/
PUSH_NAME = library/uatproxy
APP_PORT = 8080

.PHONY: clean build all
all: build docker-build clean

clean:
	@#rm *.o temp tmp
	@#docker image prune -f

build: *.py
	@#echo no need to build

docker-build: docker-image docker-run docker-tag docker-push
#docker-build: docker-image docker-push


.ONESHELL: docker-image docker-tag docker-push docker-run
docker-image:
	docker build -t ${NAME}:${VERSION} -f APP-META/Dockerfile .

docker-tag:
	@docker tag ${NAME}:${VERSION} ${DOCKER_REGISTRY}${PUSH_NAME}:${VERSION}

docker-push:
	docker push ${DOCKER_REGISTRY}${PUSH_NAME}:${VERSION}

container_name = uatproxy
docker-run: db.sqlite3
	docker stop ${container_name}
	@#docker run --name ${container_name} --rm -d -p ${APP_PORT}:${APP_PORT} ${NAME}:${VERSION}
