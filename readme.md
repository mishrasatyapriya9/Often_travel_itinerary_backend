python -m venv venv  - install venv to the project
venv\\Scripts\\activate  - to activate the cmd to python enviorment
uvicorn main:app --reload  - to run the backend project
uvicorn mcp_server:mcp_app --port 8001 --reload   - to run the mcp server file so that we can get the recomendation
                                           