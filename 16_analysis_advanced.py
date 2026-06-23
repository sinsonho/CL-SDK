"""16장 · 고급 분석 지표 — 임계성·기능적 연결성"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=10)
        rec.wait_until_stopped()
        path = rec.file["path"]
    with RecordingView(path) as r:
        crit = r.analyse_criticality(0.05, 0.9)
        conn = r.analyse_functional_connectivity(0.05, 0.2)
        crit.plot_avalanche_sizes()         # 아발란치 크기 분포
        crit.plot_branching_ratio()         # 분기비
        conn.plot()                         # 연결성 그래프

if __name__ == "__main__":
    main()
