"""18장 · 애플리케이션 예시 (cl.app)
실제로는 `python -m cl.app.init my_app` 으로 뼈대를 생성한다.
아래는 BaseApplication 패턴을 보여 주는 최소 예시다.
"""
import cl
from cl.app import BaseApplication, BaseApplicationConfig

class MyConfig(BaseApplicationConfig):
    pulses_per_second: int = 5      # 사용자 설정값(검증되는 Pydantic 모델)

class MyApplication(BaseApplication[MyConfig]):
    @staticmethod
    def config_class():
        return MyConfig

    def run(self, config: MyConfig, output_directory: str):
        # CL1에서 호출되는 진입점 — 여기에 내 로직을 둔다.
        with cl.open() as neurons:
            recording = neurons.record(stop_after_seconds=config.timeout_s or 1)
            recording.wait_until_stopped()
        return None
