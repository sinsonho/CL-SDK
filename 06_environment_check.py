"""6장 · 설치/환경 확인
CL-SDK가 제대로 설치되었는지, 시뮬레이터로 동작하는지 확인한다.
실행:  python 06_environment_check.py
"""
import sys
import cl

def main():
    print("Python    :", sys.version.split()[0])          # 3.12 이상이어야 함
    print("cl 모듈   :", cl.__name__)
    print("시뮬레이터:", cl.is_simulator())                # 로컬에서는 True
    with cl.open() as neurons:
        print("채널 수   :", neurons.get_channel_count())   # 64
        print("샘플레이트:", neurons.get_frames_per_second(), "Hz")  # 25000
    print("환경 준비 완료 — 첫 코드를 실행할 수 있습니다.")

if __name__ == "__main__":
    main()
