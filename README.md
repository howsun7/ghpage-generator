# Static site generator
Generate static site with a template engine (jinja). The output can be changed by changing:
- config.yml
- source template ('templates/example.html' in this case)

## Using it
Option 1:
- clone the repo
- rm .git
- follow the [instruction of GitHub Pages](https://pages.github.com) 
- change the source files (config.yml and template)

Option 2 (better):
- follow the Github Pages link in option 1 (this repo will be used as a submodule)
- add submodule: `git submodule add [your repo link] src/`



## Generate the html
- Install dependencies: `pipenv install`
- Generate html: `python generator`


