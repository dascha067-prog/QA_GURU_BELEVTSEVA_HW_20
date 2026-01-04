from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    context: str = "emulator"
    timeout: float = 10.0

    platformName: str | None = None
    deviceName: str | None = None
    app: str | None = None
    command_executor: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
