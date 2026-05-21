# TypeScript SDK

Реализован `@docmost/sdk` в `typescript/`:
- DocmostClient, axios + tough-cookie (Bearer + email/password)
- генератор `typescript/scripts/generate_sdk.py`
- 109 interfaces, 23 service API classes
- npm publish-ready: package.json, tsc -> dist/, README
- обновлён корневой README.md

Публикация: `cd typescript && npm run build && npm publish --access public`
