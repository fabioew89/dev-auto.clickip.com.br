# Caminho do ambiente virtual
VENV=.virt
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Criar o ambiente virtual
.PHONY: venv
venv:
	@python3 -m venv $(VENV)
	@echo "Ambiente virtual criado em $(VENV)."
	@$(PIP) install --upgrade pip > /dev/null
	@echo "Pip atualizado."

# Instalar dependências usando o ambiente virtual
.PHONY: install
install: venv
	@$(PIP) install -r requirements.txt > /dev/null
	@echo "Dependências instaladas."

# Rodar a aplicação usando o ambiente virtual
.PHONY: run
run: venv
	@$(PYTHON) -m flask --app run.py run --debug
	@echo "Aplicação em execução."

# Limpar o ambiente virtual
.PHONY: clean
clean:
	@rm -rf $(VENV)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@echo "Ambiente virtual removido e caches."

# faz o da aplicacao
.PHONY: build
build: clean venv install run
	@echo "Aplicacao rodando..."

# faz o test do flake8 no code excluído o venv
.PHONY: test
test: 
	@flake8 --exclude $(VENV)