"""14장 · 커스텀 데이터 소스 모듈 (import 가능해야 하므로 숫자로 시작하지 않게 둔다)
간단한 사인파 합성 신호를 만들어 시뮬레이터에 공급하는 Pull 소스.
"""
import numpy as np
from cl.sim import DataSourceBatch, SimulatorDataSource, SimulatorDataSourceMetadata

class SineSource(SimulatorDataSource):
    def __init__(self, scale: float = 50.0):
        self._scale = scale
    @property
    def metadata(self) -> SimulatorDataSourceMetadata:
        return SimulatorDataSourceMetadata(channel_count=64, duration_frames=None, seekable=True)
    def read(self, from_timestamp: int, frame_count: int) -> DataSourceBatch:
        t = np.arange(from_timestamp, from_timestamp + frame_count, dtype=np.float64)
        wave = (np.sin(t / 50.0) * self._scale).astype(np.int16)
        frames = np.repeat(wave[:, None], 64, axis=1).astype(np.int16)
        return DataSourceBatch(frames=frames)

def create_source(scale: float = 50.0) -> SimulatorDataSource:
    return SineSource(scale=scale)
