# Makefile
# ============================================================================
# Globals
# ============================================================================
CONTAINER_NAME:="armoni-bot"
TAG:=$(shell git log -1 --pretty=format:"%H")

# ============================================================================
# Development Commands
# ============================================================================

.PHONY: build
build: ## Build the docker image.
	docker build \
		--build-arg VERSION=$(TAG) \
		-t $(CONTAINER_NAME) . \

.PHONY: run
run: ## Runing the bot.
	docker-compose stop
	docker-compose up

.PHONY: lock-dependencies
lock-dependencies: ## Lock poetry dependencies.
	docker run \
		-v `pwd`:/app \
		--env-file .env \
		-it $(CONTAINER_NAME) poetry lock \

.PHONY: lint
lint: ## Run service linting.
	docker run \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/.pylintrc:/app/.pylintrc \
		--env-file .env \
		$(CONTAINER_NAME) \
		poetry run pylint /app/src

.PHONY: black
black: ## Code formatting.
	docker run \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/pyproject.toml:/app/pyproject.toml \
		--env-file .env \
		$(CONTAINER_NAME) \
		poetry run black /app/src

.PHONY: test
test: ## Run service linting.
	docker run \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/tests:/app/tests \
        --env-file .env \
		$(CONTAINER_NAME) \
		poetry run pytest /app/tests

.PHONY: debug
debug: ## Run service linting.
	docker-compose stop
	docker-compose run $(CONTAINER_NAME) \
		/bin/bash -c "poetry run pytest ${test_dir} -s -vv"

.PHONY: terminal
terminal:
	docker run \
		-v `pwd`:/app \
		--env-file .env \
		-it $(CONTAINER_NAME) bash