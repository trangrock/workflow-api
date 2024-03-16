.DEFAULT_GOAL := help
.PHONY: build shell dev prod test lint clean help
# Set bash as default shell
SHELL := bash
# Run all commands in a single shell
.ONESHELL:
# Warn if undefined variables are referenced
MAKEFLAGS += --warn-undefined-variables
# Disable default rules
MAKEFLAGS += --no-builtin-rules

build: ## Build the project docker image(s) without using internal docker cache
	docker compose build --no-cache workflow-api

clean: ## Stop docker containers and remove all generated files
	docker compose down -t 2 -v --remove-orphans
	docker compose rm -f -v

shell: ## Run shell in the container
	docker compose run --rm --service-ports workflow-api shell

dev: ## Run in development mode
	docker compose run --rm --service-ports workflow-api dev

prod: ## Run in production mode
	docker compose run --rm --service-ports workflow-api prod

test: ## Run unit tests
	docker compose run --rm --service-ports workflow-api test

lint: ## Run linter (flake8) on the project
	docker compose run --rm --service-ports workflow-api lint

help: ## Show this help message and exit
	@cat $(MAKEFILE_LIST) | grep -e "^[a-zA-Z_\-]*: .*## *" | awk 'BEGIN {FS = ": .*## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
