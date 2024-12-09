# Caminho do ambiente virtual
VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Criar o ambiente virtual
.PHONY: venv
venv:
	@python3 -m venv $(VENV)
	@echo "Ambiente virtual criado em $(VENV)"
	@$(PIP) install --upgrade pip > /dev/null
	@echo "Pip atualizado."

# Instalar dependências usando o ambiente virtual
.PHONY: install
install: venv
	@$(PIP) install -r requirements.txt > /dev/null
	@echo "Dependências instaladas."

# Rodar a aplicação usando o ambiente virtual
.PHONY: run
run: venv install
	@$(PYTHON) -m flask --app run.py run --debug
	@echo "Aplicação em execução."

# Limpar o ambiente virtual
.PHONY: clean
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@rm -rf $(VENV)
	@echo "Ambiente virtual removido e caches..."

# faz o test do flake8 no code excluído o venv
.PHONY: flake
flake:
	@echo 'Checking flake8...'
	@flake8 --exclude $(VENV)