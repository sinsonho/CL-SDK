"""9장 · 읽기와 기록
(1) read()로 지금 흐르는 샘플 한 토막을 NumPy 배열로 가져온다.
(2) record()로 1초간 전부를 HDF5 파일로 저장한다.
(3) RecordingView로 그 파일을 다시 열어 들여다본다.
"""
import cl
from cl import RecordingView

def main():
    with cl.open() as neurons:
        # (1) 읽기 — 250 프레임(약 10ms)을 NumPy 배열로
        frames = neurons.read(250)
        print("read 형태:", frames.shape)   # (250, 64) 형태

        # (2) 기록 — 1초 뒤 자동으로 멈추는 녹화
        recording = neurons.record(stop_after_seconds=1)
        recording.wait_until_stopped()
        path = recording.file["path"]
        print("기록 저장:", path)

    # (3) 다시 열어 분석 (with 컨텍스트로 안전하게 닫기)
    with RecordingView(path) as rec:
        print("총 스파이크 수:", len(rec.spikes))
        print("샘플 배열   :", rec.samples.shape)

if __name__ == "__main__":
    main()
