"""
Behave environment.py - REQUIRED by Behave framework

Behave automatically looks for this file and calls these functions:
- before_all() - Once before all tests
- after_all() - Once after all tests
- before_scenario() - Before each scenario
- after_scenario() - After each scenario

SDK patches these to track test events for BrowserStack.
"""

def before_all():
    """Runs once before all scenarios"""
    print("Starting test run...")


def after_all(context):
    """Runs once after all scenarios"""
    print("Test run complete!")


def before_scenario(context, scenario):
    """Runs before each scenario"""
    print(f"\nStarting: {scenario.name}")


def after_scenario(context, scenario):
    """Runs after each scenario"""
    status = "PASSED" if scenario.status == 'passed' else "FAILED"
    print(f"Finished: {scenario.name} - {status}")
