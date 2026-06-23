"""21장 · 재현 가능한 실험 워크플로우
기준선 → 조건 → 기록 → 분석 → 비교. 시드를 고정하면 같은 결과가 재현된다.
(.env 에 CL_SDK_RANDOM_SEED=42 를 두면 더 확실하다)
"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView, ChannelSet, StimDesign

def record_seconds(neurons, seconds):
    rec = neurons.record(stop_after_seconds=seconds)
    rec.wait_until_stopped()
    return rec.file["path"]

def summarize(path):
    with RecordingView(path) as r:
        return len(r.spikes)

def main():
    with cl.open() as neurons:
        base = record_seconds(neurons, 2)                         # ① 기준선
        neurons.stim(ChannelSet(8, 9), StimDesign(160,-1.0,160,1.0))  # ② 조건
        cond = record_seconds(neurons, 2)                         # ③ 조건 기록
    print("기준선 스파이크:", summarize(base))                     # ④ 비교
    print("조건  스파이크:", summarize(cond))

if __name__ == "__main__":
    main()
