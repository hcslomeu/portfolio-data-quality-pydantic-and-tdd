<div align="center">

# Portfolio for Data Quality using Pandera (with TDD demo)

</div>

<p align="center">
[![ci](https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd/actions/workflows/CI.yaml/badge.svg)](https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd/actions/workflows/CI.yaml)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Built with Pydantic](https://img.shields.io/badge/Built%20with-Pydantic-blue)]()
[![Built with Pandera](https://img.shields.io/badge/Built%20with-Pandera-blue)]()
</p>

---

<p align="center">
**📚 Documentation**: <a href="https://hcslomeu.github.io/portfolio-data-quality-pydantic-and-tdd/" target="_blank">https://hcslomeu.github.io/portfolio-data-quality-pydantic-and-tdd/</a>
</p>
<p align="center">
**💻 Source Code**: <a href="https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd" target="_blank">https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd</a>
</p>

---

This repository showcases a data quality monitoring project using Pandera, which is derived from Pydantic. The primary goal is to demonstrate how to enforce data contracts and perform data transformations in a reliable and testable manner.



The files in the `app` folder contain the core logic for the ETL (Extract, Transform, Load) process, including schema definitions and transformation functions. This documentation provides an overview of the project, the data contracts, the transformations applied, and also demonstrates my skills to generate clear and well design documentation for users.



## Features



*   **Data Quality Enforcement:** Uses Pandera to define and validate data schemas.

*   **TDD Approach:** Includes a suite of tests to ensure the reliability of the transformation logic.

*   **Clear Documentation:** Provides comprehensive documentation for the project, including this README and a generated documentation site.

*   **Reproducible Environment:** Uses `poetry` and `pyenv` to ensure a consistent development environment.



## Getting Started



### Prerequisites



*   [Python 3.12.1](https://www.python.org/downloads/release/python-3121/)

*   [pyenv](https://github.com/pyenv/pyenv)

*   [poetry](https://python-poetry.org/docs/)



### Installation



1.  Clone the repository:



    ```bash

    git clone https://github.com/hcslomeu/portfolio-data-quality-pydantic-and-tdd.git

    cd portfolio-data-quality-pydantic-and-tdd

    ```



2.  Set the correct Python version using `pyenv`:



    ```bash

    pyenv install 3.12.1

    pyenv local 3.12.1

    ```



3.  Configure poetry and activate the virtual environment:



    ```bash

    poetry env use 3.12.1

    poetry shell

    ```



4.  Install the project dependencies:



    ```bash

    poetry install

    ```



### Environment Variables



This project requires a `.env` file in the root directory with the following variables for database connection:



```

POSTGRES_HOST=your_host

POSTGRES_USER=your_user

POSTGRES_PASSWORD=your_password

POSTGRES_DB=your_database

POSTGRES_PORT=your_port

```



## Usage



The project uses `taskipy` to simplify running common commands. You can see the available tasks in the `[tool.taskipy.tasks]` section of the `pyproject.toml` file.



To execute the main ETL pipeline, run:



```bash

poetry run python app/etl.py

```



## Running the tests



To run the test suite, use the following command:



```bash

poetry run task test

```



This will execute the tests using `pytest`.



## Documentation



To view the project documentation locally, run:



```bash

poetry run task doc

```



This will start a local server, and you can access the documentation at `http://127.0.0.1:8000`.
