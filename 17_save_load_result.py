"""17장 · 결과를 저장하고 재계산 없이 다시 불러오기"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView
from cl.analysis import AnalysisResultCriticality

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=10)
        rec.wait_until_stopped(); path = rec.file["path"]
    with RecordingView(path) as r:
        result = r.analyse_criticality(0.05, 0.9)
        result.save("criticality_result.json")     # JSON으로 저장

    # 나중에: 재계산 없이 그대로 복원해 다시 그리기
    loaded = AnalysisResultCriticality.from_file("criticality_result.json")
    loaded.plot_avalanche_sizes()

if __name__ == "__main__":
    main()
