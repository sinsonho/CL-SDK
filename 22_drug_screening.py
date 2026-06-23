"""22장 · 화합물 반응 스크리닝 (워크플로우 골격)
투여 '전'과 '후'의 발화·버스트 지표를 비교한다.
주의: 시뮬레이터는 약물에 반응하지 않는 대조군 — 실제 검증은 CL1에서.
'화합물 효과'는 여기서는 커스텀 데이터 소스로 모델링할 수 있다(14장).
"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView

def metrics(path):
    with RecordingView(path) as r:
        return {"spikes": len(r.spikes),
                "firing": r.analyse_firing_stats(),
                "bursts": r.analyse_network_bursts(0.1, 1.0, 0.5)}

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=3); rec.wait_until_stopped()
        before = rec.file["path"]
        # --- 여기서 화합물 조건을 적용한다(모델/자극/데이터 소스 교체) ---
        rec2 = neurons.record(stop_after_seconds=3); rec2.wait_until_stopped()
        after = rec2.file["path"]
    b, a = metrics(before), metrics(after)
    print("투여 전 스파이크:", b["spikes"])
    print("투여 후 스파이크:", a["spikes"])
    print("→ 차이로 효능/독성을 정량화한다(전·후 분석 지표 비교).")

if __name__ == "__main__":
    main()
