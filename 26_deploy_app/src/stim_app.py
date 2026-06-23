"""26장 — 배포 가능한 애플리케이션 예제.

이 파일은 BaseApplication 을 상속한 '정식 애플리케이션'이다.
- python -m cl.app.init  로 뼈대를 만들고,
- python -m cl.app.pack  으로 설치용 ZIP을 만들 수 있다.

설정(MyAppConfig)은 pydantic 모델이라 잘못된 값은 실행 전에 걸러진다.
실제 CL1에서는 결과 기록이 /data/recordings/ 에 저장된다.
"""
from cl.app import BaseApplication, BaseApplicationConfig, RunSummary, OutputType


class StimAppConfig(BaseApplicationConfig):
    target_channel: int = 42        # 자극할 채널
    pulse_uA: float = -1.0          # 음의 선행 위상 전류 (전하 균형)
    record_seconds: int = 10        # 기록 길이(초)


class StimApp(BaseApplication[StimAppConfig]):
    def run(self, config: StimAppConfig, output_directory: str) -> RunSummary:
        import cl
        from cl import ChannelSet, StimDesign

        with cl.open() as neurons:
            recording = neurons.record(stop_after_seconds=config.record_seconds)

            # 전하 균형 biphasic 자극: 음수(-) 위상이 먼저, 같은 크기 양수(+)가 뒤
            design = StimDesign(160, config.pulse_uA, 160, -config.pulse_uA)
            neurons.stim(ChannelSet(config.target_channel), design)

            recording.wait_until_stopped()

        return RunSummary(
            type=OutputType.TEXT,
            content=(f"채널 {config.target_channel} 에 {abs(config.pulse_uA)}µA "
                     f"전하 균형 자극 후 {config.record_seconds}초 기록 완료"),
        )

    @staticmethod
    def config_class() -> type[StimAppConfig]:
        return StimAppConfig
