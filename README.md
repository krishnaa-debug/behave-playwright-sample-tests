# BrowserStack SDK + Playwright + Behave Sample

Simple Behave BDD test with Playwright on BrowserStack.

## What's Included

- 1 test scenario (open Google, verify title)
- BrowserStack configuration
- Minimal environment.py (25 lines)
- Python + Behave setup

## Setup (2 minutes)

### 1. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Add credentials to browserstack.yml
```yaml
userName: YOUR_USERNAME
accessKey: YOUR_ACCESS_KEY
```

### 3. Run test
```bash
browserstack-sdk behave features/ --no-capture
```

## Expected Result

- Console: `1 feature passed, 1 scenario passed`
- Wait 10 seconds
- Check https://automate.browserstack.com - Session with video/screenshots
- Check https://observer.browserstack.com - Test Observability data

## Files

```
├── browserstack.yml          # Add your credentials here
├── environment.py            # Behave lifecycle (minimal, 25 lines)
├── requirements.txt          # Dependencies
├── features/sample_test.feature    # Test scenario
└── steps/test_steps.py      # Step implementations
```

## Key Points

- **environment.py:** Behave requires it (framework standard). SDK works whether you modify it or not.
- **Custom logging:** Safe to add - doesn't interfere with SDK tracking.
- **SDK integration:** Automatic via `browserstack-sdk behave` command.

## Release Notes
### Version 1.41.0 (2026-03-12)
🚀 **New Features**
Added Accessibility support for Behave(Playwright)

### Version 1.40.0 (2026-03-09)
🚀 **New Features**
Added TRA automate support for Behave(Playwright)



