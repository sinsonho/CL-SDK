"""[프로젝트 13] 뉴런-LLM 하이브리드 에이전트 (인터페이스 골격)
LLM/디지털 측의 '상태'를 자극으로 인코딩하고, 뉴런의 발화를 '특징'으로 읽어 되돌린다.
실제 LLM 연동은 외부 라이브러리 몫 — 여기서는 인터페이스 패턴만 보여 준다.
"""
import cl
from cl import ChannelSet, StimDesign

def encode_state_to_stim(neurons, state_value):
    ch = state_value % 64
    neurons.stim(ChannelSet(ch), StimDesign(160, -1.0, 160, 1.0))

def read_features(tick):
    return [s.channel for s in tick.analysis.spikes]   # 발화 채널을 특징 벡터로

def main():
    with cl.open() as neurons:
        for tick in neurons.loop(ticks_per_second=50, stop_after_seconds=3):
            encode_state_to_stim(neurons, tick.iteration)   # 디지털 → 뉴런
            features = read_features(tick)                  # 뉴런 → 디지털
            # features 를 LLM/정책에 넘겨 다음 행동을 결정(외부)
    print("하이브리드 인터페이스 데모 종료")

if __name__ == "__main__":
    main()
