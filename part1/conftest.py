import re
import pytest
from playwright.sync_api import sync_playwright, Page, expect
import pytest


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Включаем трассировку (для всех шагов)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()

        yield page

        # После теста проверяем его результат
        if request.node.rep_call.failed:
            # Сохраняем трассировку только для упавшего теста
            test_name = request.node.name
            trace_path = f"traces/{test_name}-trace.zip"
            context.tracing.stop(path=trace_path)
            print(f"\nTrace saved: {trace_path}")
        else:
            # Если тест успешен, просто останавливаем трассировку без сохранения
            context.tracing.stop()
        
        browser.close()

def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:
        setattr(item, "rep_" + call.when, call)