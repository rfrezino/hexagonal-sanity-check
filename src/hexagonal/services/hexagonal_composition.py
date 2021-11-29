from typing import Optional, List

from hexagonal.domain.hexagonal_layer import HexagonalLayer


class HexagonalComposition(List[HexagonalLayer]):

    def get_layer_index_by_module_name(self, module: str) -> Optional[int]:
        for idx, layer in enumerate(self):
            if module in layer.directories:
                return idx + 1

        return None

    def __add__(self, next_layer) -> 'HexagonalComposition':
        self.clear()
        self.append(next_layer)
        return self

    def __rshift__(self, next_layer: HexagonalLayer) -> 'HexagonalComposition':
        self.append(next_layer)
        return self
