## Usage

```bash
envguard compare .env.example .env
```

## Exit codes

0: No differences

1: Missing variables

2: Extra variables

3: Missing and extra variables

404: File not found

## Security
EnvGuard only compares variable names.
Values are never read, stored, or logged.

## Commercial version

For commercial use, binaries, and future updates:
👉 https://gumroad.com/l/envguard
