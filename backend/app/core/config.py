from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = Field(default="local", alias="APP_ENV")
    agent_provider: str = Field(default="local", alias="AGENT_PROVIDER")
    knowledge_provider: str = Field(default="local", alias="KNOWLEDGE_PROVIDER")
    prompt_directory: Path = Field(default=Path("../prompts"), alias="PROMPT_DIRECTORY")
    sample_docs_directory: Path = Field(default=Path("../data/sample-docs"), alias="SAMPLE_DOCS_DIRECTORY")
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    foundry_project_endpoint: str | None = Field(default=None, alias="FOUNDRY_PROJECT_ENDPOINT")
    foundry_agent_name: str | None = Field(default=None, alias="FOUNDRY_AGENT_NAME")
    foundry_model_deployment: str | None = Field(default=None, alias="FOUNDRY_MODEL_DEPLOYMENT")
    foundry_knowledge_base_id: str | None = Field(default=None, alias="FOUNDRY_KNOWLEDGE_BASE_ID")
    azure_storage_account_url: str | None = Field(default=None, alias="AZURE_STORAGE_ACCOUNT_URL")
    azure_storage_container: str | None = Field(default=None, alias="AZURE_STORAGE_CONTAINER")


@lru_cache
def get_settings() -> Settings:
    return Settings()
