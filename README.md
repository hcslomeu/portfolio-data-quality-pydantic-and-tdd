# Portfolio for Data Quality using Pydantic (with TDD demo)

Visit the documentation

[![image](/pic/print.png)](https://lvgalvao.github.io/workshop_02_aovivo/)


1. Clone the repository:

```bash
git clone [https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd.git](https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd.git)
cd portfolio-data-quality-pydantic-and-tdd
````

2.  Configure the correct Python version using `pyenv`:

<!-- end list -->

```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3.  Configure poetry for Python version 3.12.1 and activate the virtual environment:

<!-- end list -->

```bash
poetry env use 3.12.1
poetry shell
```

4.  Install the project dependencies:

<!-- end list -->

```bash
poetry install
```

5.  Run the tests to ensure everything is working as expected:

<!-- end list -->

```bash
poetry run task test
```

6.  Run the command to view the project documentation:

<!-- end list -->

```bash
poetry run mkdocs serve
```

7.  Run the command to execute the pipeline and perform the ETL:

<!-- end list -->

```bash
poetry run python app/etl.py
```