"""[프로젝트 3] 활동 기록·재생기
2초간 기록한 뒤, RecordingView로 다시 열어 요약을 출력한다.
"""
import cl
from cl import RecordingView

def main():
    with cl.open() as neurons:
        rec = neurons.record(stop_after_seconds=2)
        rec.wait_until_stopped()
        path = rec.file["path"]
    with RecordingView(path) as r:
        print("파일      :", path)
        print("스파이크 수:", len(r.spikes))
        print("자극 수   :", len(r.stims))

if __name__ == "__main__":
    main()
