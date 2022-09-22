<p align="center">
  <img src="http://msa.u2d.ai/images/msa_logo_big.png?raw=true" alt="MSA SDK image"/>
</p>

------
<p align="center">
    <em>msaStorageDict - Dict with a backend storage</em>
<br>
    Optimized for use with FastAPI/Pydantic.
<br>
  <a href="https://pypi.org/project/msaStorageDict" target="_blank">
      <img src="https://img.shields.io/pypi/v/msaStorageDict?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypi.org/project/msaStorageDict" target="_blank">
      <img src="https://img.shields.io/pypi/pyversions/msaStorageDict.svg?color=%2334D058" alt="Supported Python versions">
  </a>
</p>

------

**Documentation**: <a href="https://msa.u2d.ai/" target="_blank">MSA SDK Documentation (http://msa.u2d.ai/)</a>

------

## Features
- **Dict with Storage Backend**: Use Dict's with backend storage like redis.


## Main Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
  combined with  [SQLAlchemy](https://www.sqlalchemy.org/) and [Pydantic](https://pydantic-docs.helpmanual.io/), with all
  their features .


### Usage example is in the app module \_\_init\_\_.py

```python
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - U2D.ai / S.Welcker
"""
from typing import Optional, List

from sqlmodel import SQLModel

from msaStorageDict.admin.utils.fields import Field
from msaStorageDict.models.service import get_msa_app_settings
from msaStorageDict.service import MSAApp


async def test_timer_min():
    app.logger.info("msaStorageDict Test Timer Async Every Minute")


def test_timer_five_sec():
    app.logger.info("msaStorageDict Test Timer Sync 5 Second")


class TestArticle(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(title='ArticleTitle', max_length=200)
    description: Optional[str] = Field(default='', title='ArticleDescription', max_length=400)
    status: bool = Field(None, title='status')
    content: str = Field(title='ArticleContent')


class TestCategory(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(title='ArticleTitle', max_length=200)
    description: Optional[str] = Field(default='', title='ArticleDescription', max_length=400)
    status: bool = Field(None, title='status')
    content: str = Field(title='ArticleContent')


get_msa_app_settings.cache_clear()
settings = get_msa_app_settings()
settings.title = "u2d.ai - MSA/SDK MVP"
settings.version = "0.0.1"
settings.debug = True

app = MSAApp(settings=settings, auto_mount_site=True,
             sql_models=[TestArticle, TestCategory],
             contact={"name": "msaStorageDict", "url": "http://u2d.ai", "email": "stefan@u2d.ai"},
             license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT", })

app.scheduler.task("every 1 min", func=test_timer_min )
app.scheduler.task("every 5 sec", func=test_timer_five_sec )

app.logger.info("Initialized " + settings.title + " " + settings.version)


@app.on_event("startup")
async def startup():
    app.logger.info("msaStorageDict Own Startup MSAUIEvent")
    #app.mount_site()


@app.on_event("shutdown")
async def shutdown():
    app.logger.info("msaStorageDict Own Shutdown MSAUIEvent")


if __name__ == '__main__':
    pass
```

# Typical Run Log
![Typical Log Run](./docs/images/msa_sdk_run.png)

## Interface Preview


#### Home Screen with System Info
- Open `http://127.0.0.1:8090/admin/` in your browser:
<p align="center">
  <img src="http://msa.u2d.ai/images/msa_admin_home.png?raw=true" alt="Home"/>
</p>

#### CRUD of SQLModels Screen
<p align="center">
  <img src="http://msa.u2d.ai/images/msa_admin_crud.png?raw=true" alt="CRUD"/>
</p>

#### Login Screen
- Open `http://127.0.0.1:8090/admin/auth/form/login` in your browser:
<p align="center">
  <img src="http://msa.u2d.ai/images/msa_auth_login.png?raw=true" alt="Login"/>
</p>

#### OpenAPI Interactive Documentation (Swagger) Screen
- Open `http://127.0.0.1:8090/#/admin/docs` in your browser:
<p align="center">
  <img src="http://msa.u2d.ai/images/msa_admin_openapi.png?raw=true" alt="OpenAPI"/>
</p>

#### Profiler Screen
- Open `http://127.0.0.1:8090/#/admin/profiler` in your browser:
<p align="center">
  <img src="http://msa.u2d.ai/images/msa_admin_profiler.png?raw=true" alt="Profiler"/>
</p>

## License Agreement

- `msaStorageDict`Based on `MIT` open source and free to use, it is free for commercial use, but please clearly show the copyright information about msaStorageDict - Auth Admin in the display interface.


## How to create the documentation

We use mkdocs and mkdocsstring. The code reference and nav entry get's created virtually by the triggered python script /docs/gen_ref_pages.py while ``mkdocs`` ``serve`` or ``build`` is executed.

### Requirements Install for the PDF creation option:
PDF Export is using mainly weasyprint, if you get some errors here pls. check there documentation. Installation is part of the msaStorageDict, so this should be fine.

We can now test and view our documentation using:

    mkdocs serve

Build static Site:

    mkdocs build


## Build and Publish
  
Build:  

    python setup.py sdist

Publish to pypi:

    twine upload dist/*