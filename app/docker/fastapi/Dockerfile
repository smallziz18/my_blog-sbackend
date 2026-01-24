# ================================
# Base image
# ================================
ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim-bookworm AS python-base

# ================================
# Stage 1 : build (deps Python avec uv)
# ================================
FROM python-base AS python-build-stage

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Créer un venv isolé
RUN python -m venv .venv \
    && ./.venv/bin/pip install --no-cache-dir --upgrade pip

# Copier pyproject.toml + uv.lock
COPY pyproject.toml uv.lock* ./

# Installer uv + dépendances figées dans le venv
RUN ./.venv/bin/pip install --no-cache-dir uv \
    && ./.venv/bin/uv sync --frozen

# ================================
# Stage 2 : runtime
# ================================
FROM python-base AS python-run-stage

ARG APP_HOME=/src
ARG APP_USER=fastapi
ARG APP_GROUP=fastapi

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/.venv/bin:$PATH"

WORKDIR ${APP_HOME}

# Installer dépendances système runtime
RUN apt-get update && apt-get install -y \
    libpq5 bash \
    && rm -rf /var/lib/apt/lists/*

# User non-root
RUN groupadd -r ${APP_GROUP} \
    && useradd -r -g ${APP_GROUP} -d ${APP_HOME} -m ${APP_USER}

# Copier le venv du build stage
COPY --from=python-build-stage /usr/src/app/.venv /usr/local/.venv

# Copier le code
COPY --chown=${APP_USER}:${APP_GROUP} . ${APP_HOME}

# Scripts
COPY --chown=${APP_USER}:${APP_GROUP} app/docker/fastapi/entrypoint.sh /entrypoint.sh
COPY --chown=${APP_USER}:${APP_GROUP} app/docker/fastapi/start.sh /start.sh

RUN chmod +x /entrypoint.sh /start.sh

USER ${APP_USER}

ENTRYPOINT ["/entrypoint.sh"]
