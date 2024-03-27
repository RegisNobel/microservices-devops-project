End to end microservices devops project

3/1/2024 
    - finished devleoping basic app (front and backend services)
    - tested form and admin pages
    - pushed changes to github
  

3/4/2024
    - added a branch on github
    - develop the email sender service on new branch
    - tested the email sender service
    - pushed changes to github

3/5/2024
    - merged the email sender service to the main branch
    - started script to run all services

3/11/2024
    - finished the shell script to run/stop all services
    - added a Makefile to do various tasks
    - tested the script/makefile
    - pushed changes to github

3/13/2024
    - added update button to admin page
    - tested the update button
    - removed hardcoded values from code (used environment variables)
    - added delete button to admin page
    - tested the delete button
    - pushed changes to github

3/21/2024
    - added __init__.py to all services to enable importing
    - added unit tests for the frontend endpoints
    - tested using pytest
    - added linting to all py files using make and black
    - pushed changes to github

3/26/2024
    - wrote docker files for each service
    - added a docker compose file to run all services + mysqldb service
    - removed unused packages from all requirements.txt files
    - Docker compose worked but services were not able to connect to each other
    - py files needed to be updated with service names instead of localhost for docker compose to work
    - App successfully ran with docker compose

    - pushed changes to github
