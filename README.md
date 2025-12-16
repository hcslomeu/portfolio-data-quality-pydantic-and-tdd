# Portfolio for Data Quality using Pydantic (with TDD demo)

---

**📚 Documentation**: <a href="https://hcslomeu.github.io/portfolio-data-quality-pydantic-and-tdd/" target="_blank">https://hcslomeu.github.io/portfolio-data-quality-pydantic-and-tdd/</a>

**💻 Source Code**: <a href="https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd" target="_blank">https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd</a>

---

This repository showcases a data quality monitoring project using Pandera, which is derived from Pydantic. The primary goal is to demonstrate how to enforce data contracts and perform data transformations in a reliable and testable manner.

The files in the `app` folder contain the core logic for the ETL (Extract, Transform, Load) process, including schema definitions and transformation functions. This documentation provides an overview of the project, the data contracts, the transformations applied, and also demonstrates my skills to generate clear and well design documentation for users.


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