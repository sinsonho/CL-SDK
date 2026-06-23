"""[프로젝트 9] 기능적 연결성 네트워크 뷰어"""
import os
os.environ["CL_SDK_VISUALISATION"] = "0"
import cl
from cl import RecordingView

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=8); rec.wait_until_stopped()
        path = rec.file["path"]
    with RecordingView(path) as r:
        r.analyse_functional_connectivity(0.05, 0.2).plot()

if __name__ == "__main__":
    main()
