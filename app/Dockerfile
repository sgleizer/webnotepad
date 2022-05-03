# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim


WORKDIR /app
COPY . .
EXPOSE 8880
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "Server.py"]
