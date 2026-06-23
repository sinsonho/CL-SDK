"""15장 · 기초 분석 지표 — 발화 통계·네트워크 버스트·정보 엔트로피
순수 분석이므로 시각화 백그라운드 서비스를 끄고 시작한다.
"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=3)
        rec.wait_until_stopped()
        path = rec.file["path"]
    with RecordingView(path) as r:
        firing = r.analyse_firing_stats()
        bursts = r.analyse_network_bursts(0.1, 1.0, 0.5)
        entropy = r.analyse_information_entropy(0.1)
        print("발화 통계 :", firing)
        print("정보 엔트로피:", entropy)
        bursts.plot()     # 네트워크 버스트 그림 표시

if __name__ == "__main__":
    main()
