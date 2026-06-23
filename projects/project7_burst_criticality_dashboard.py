"""[프로젝트 7] 버스트·임계성 분석 대시보드
한 번의 기록에서 네트워크 버스트와 임계성을 함께 그려 비교한다.
"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=10); rec.wait_until_stopped()
        path = rec.file["path"]
    with RecordingView(path) as r:
        r.analyse_network_bursts(0.1, 1.0, 0.5).plot()
        r.analyse_criticality(0.05, 0.9).plot_avalanche_sizes()

if __name__ == "__main__":
    main()
