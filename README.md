<p align="center">
  <img src="http://msastoragedict.u2d.ai/images/logo_big.png?raw=true" alt="MSA StorageDict image"/>
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

**Documentation**: <a href="https://msastoragedict.u2d.ai/" target="_blank">MSA Storage Dict Documentation (https://msastoragedict.u2d.ai/)</a>

------

## Features
- **Dict with Storage Backend**: Use Dict's with backend storage like redis.


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