# Python SDK

Реализован пакет `docmost-sdk` в `python/`:
- DocmostClient с api_token и email/password (cookie через httpx)
- 109 Pydantic-моделей + 23 service API (генератор `python/scripts/generate_sdk.py`)
- parse_data() для типизации ответов
- pyproject.toml (hatchling), README, py.typed
- Обновлён корневой README.md
