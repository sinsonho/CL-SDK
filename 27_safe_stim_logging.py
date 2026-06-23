"""27장 — 안전한 자극과 재현 가능한 로깅.

핵심 두 가지:
1) 전하 균형: 음의 선행 위상 biphasic 자극(StimDesign) 사용.
2) 반복은 BurstDesign 으로(개별 자극 200Hz/채널 한계, ChannelQueueFull 회피).
3) 실험 조건은 data stream attributes 에 남겨 재현성을 확보한다.
"""
import cl
from cl import ChannelSet, StimDesign, BurstDesign


def main():
    with cl.open() as neurons:
        # (1) 실험 메타데이터를 기록에 남긴다 → 나중에 RecordingView 로 그대로 복원
        meta = neurons.create_data_stream(
            name="experiment_meta",
            attributes={"protocol": "A1", "pulse_uA": -1.0, "author": "신선호"},
        )

        recording = neurons.record(stop_after_seconds=20)

        channels = ChannelSet(20, 42, 51, 60)
        # (2) 전하 균형 biphasic: -1.0µA 가 먼저, +1.0µA 가 뒤 (폭 160µs)
        design = StimDesign(160, -1.0, 160, 1.0)

        # (3) 같은 자극을 20회 40Hz 로 — 개별 반복 대신 버스트로 안전하게
        burst = BurstDesign(20, 40)

        meta.update_attributes({"phase": "stim_on"})
        neurons.stim(channels, design, burst)

        recording.wait_until_stopped()
        print("자극·기록 완료. 분석은 이후 RecordingView 로 수행하세요.")


if __name__ == "__main__":
    main()
