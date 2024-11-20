import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
class HachiChart:
    def __init__(self,
                 font: str = "Yu Gothic", 
                 xlabel: str|None = None, 
                 ylabel: str|None = None,
                 label: list|None = None, 
                 f1: list|None = None,
                 f2: list|None = None,) -> None:
        
        # - - - - - - - - 初期化 - - - - - - - - #
        self.fig = plt.figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot()
        self.label = label
        self.f1 = f1
        self.f2 = f2
        
        # - - - - - - - - 座標軸の設定 - - - - - - - - #
        # 軸を中心にする
        self.ax.spines["bottom"].set_position("zero")
        self.ax.spines["left"].set_position("zero")
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        
        # メモリのスタイル
        self.ax.tick_params(direction="inout")
        
        # メモリの数値設定
        self.ax.set_xticks([-1, -0.5, 0, 0.5, 1])
        self.ax.set_xticklabels([-1, -0.5, 0, 0.5, 1])
        self.ax.set_yticks([-1, -0.5, 0, 0.5, 1])
        self.ax.set_yticklabels([-1, -0.5, "", 0.5, 1])

        # グラフの範囲
        self.ax.set_xlim([-1.1, 1.1])
        self.ax.set_ylim([-1.1, 1.1])
        
        # 軸ラベル
        self.ax.set_xlabel(xlabel, rotation=-90, family=font, x=0.98)
        self.ax.set_ylabel(ylabel, rotation=0, family=font, y=0.97)
        
        # - - - - - - - - 円の描画 - - - - - - - - #
        c = patches.Circle(xy=(0, 0), radius=1, fill=False)
        self.ax.add_patch(c)
        
        # - - - - - - - - プロットの設定 - - - - - - - - #
        # 点のラベル
        if (self.label == None): self.label = self.setLabel()
        if (isinstance(self.label, str)): self.label = self.label.split()

        # プロットするデータ
        if (self.f1 == None): self.f1 = self.setData()
        if (self.f2 == None): self.f2 = self.setData()

        # プロット
        if not(len(self.f1)==len(self.f2)==len(self.label)):
            raise AttributeError("The given elements have different numbers of items.")
        
        for i, j, k in zip(self.f1, self.f2, self.label):
            plt.plot(i, j, "o")
            plt.annotate(k, xy=(i, j), family=font)
            
            
            
    def setData(self) -> np.ndarray:
        return np.array(list(map(np.float64,input("値を空白区切りで入力してください。").split())))
        
    def setLabel(self) -> list[str]:
        return input("ラベルを空白区切りで入力してください。").split()

    def show(self) -> None:
        plt.show()