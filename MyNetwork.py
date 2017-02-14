import heapq # プライオリティ・キュー

class my_network:
    # **************************************************
    # ネットワーククラス
    # **************************************************
    
    def __init__(self, undirected=False):
        # **************************************************
        # コンストラクタ
        # undirected : 無向か（デフォルト：有向）
        # **************************************************
        # ノードディクショナリ初期化
        self.node_dict = {}
        # 無向グラフか
        self.undirected = undirected
        # プライオリティ・キュー
        self.queue = []
    
    class node:
        # **************************************************
        # ノードクラス
        # **************************************************
        
        def __init__(self):
            # **************************************************
            # コンストラクタ
            # **************************************************
            # 隣接ノード辞書{ノード名：重み}
            self.adjacent_node = {}
            # 最短経路時の前回のノードの名前
            self.last_node = None
            # その時点の最短距離
            self.dist = None
            # 最短経路決定フラグ
            self.is_decision = False

    def add_node(self, arg_nodes):
        # **************************************************
        # ノードの追加
        # arg_nodes : ノードの名称リスト
        # **************************************************
        # ノードリストにノードインスタンス追加
        for name in arg_nodes:
            self.node_dict[name] = self.node()
            
    def add_edge(self, arg_edges):
        # **************************************************
        # エッジの追加
        # arg_edges : エッジを表すタプルのリスト（from, to, weight）
        # **************************************************
        # ノードインスタンスにデータ追加
        for edge_tuple in arg_edges:
            # 要素数で分岐し、重み付け
            weight = 1
            if len(edge_tuple) == 3:
                weight = edge_tuple[2]
            # 行先のノード設定
            self.node_dict[edge_tuple[0]].adjacent_node[edge_tuple[1]] = weight
            # 無向の場合逆向きも設定
            if self.undirected:
                self.node_dict[edge_tuple[1]].adjacent_node[edge_tuple[0]] = weight
        
    def dijkstra(self, start, goal):
        # **************************************************
        # ダイクストラ法による最短経路探索
        # start : 開始ノードの名称
        # **************************************************
        # スタートノードをキューに追加 
        heapq.heappush(self.queue, (0, start, None))
        
        # キューが空になるまで
        while (len(self.queue) != 0):
            # 距離最小のキーを取得
            dist, key, last = heapq.heappop(self.queue)
            
            # 決定済みのノードの場合次へ
            if self.node_dict[key].is_decision:
                continue
                
            # 決定フラグを立て距離確定、前回ノード更新
            self.node_dict[key].is_decision = True
            self.node_dict[key].dist = dist
            self.node_dict[key].last_node = last
            
            
            # ゴールについたら終了
            if key == goal:
                break
            
            # 確定ノードからの距離計算
            # つながっているノード確認
            for adj_key in self.node_dict[key].adjacent_node.keys():
                # まだ決定していない場合
                if not self.node_dict[adj_key].is_decision:
                    # 優先度付きキューに(dist, key)を追加
                    heapq.heappush(self.queue, (dist + self.node_dict[key].adjacent_node[adj_key], adj_key, key))
                    
        # last_node をたどって出力
        path = []
        last = goal
        while True:
            path.append(last)
            last = self.node_dict[last].last_node
            if last is None:
                break
        # 反転して出力
        return path[::-1]