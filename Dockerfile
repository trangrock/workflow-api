FROM python:3.11

# Do not compile code upon first invocation
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
ENV PYTHONDONTWRITEBYTECODE=1

# Set workdir
WORKDIR /usr/src/app

# Install System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends

# Upgrade pip
RUN python -m pip install -U pip

RUN pip install poetry

# Necessary step to avoid poetry to install its deps in a virtualenv
RUN poetry config virtualenvs.create false && poetry config virtualenvs.in-project false

# Copy dependencies files
COPY pyproject.toml poetry.lock ./

RUN poetry install

# Copy source code
COPY . .

# Copy the entrypoint script & make it executable
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x "/entrypoint.sh"

# Set the default entrypoint to run the app
ENTRYPOINT ["/entrypoint.sh"]
