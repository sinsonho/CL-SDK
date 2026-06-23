"""[프로젝트 11] 신약 후보 반응 스크리너 — 투여 전·후 지표 비교 도구"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView

def baseline_then_condition(seconds=3):
    with cl.open() as neurons:
        r1 = neurons.record(stop_after_seconds=seconds); r1.wait_until_stopped()
        r2 = neurons.record(stop_after_seconds=seconds); r2.wait_until_stopped()
        return r1.file["path"], r2.file["path"]

def main():
    before, after = baseline_then_condition()
    for tag, path in [("투여 전", before), ("투여 후", after)]:
        with RecordingView(path) as r:
            print(tag, "· 스파이크:", len(r.spikes))

if __name__ == "__main__":
    main()
