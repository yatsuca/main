import heapq # �v���C�I���e�B�E�L���[

class my_network:
    # **************************************************
    # �l�b�g���[�N�N���X
    # **************************************************
    
    def __init__(self, undirected=False):
        # **************************************************
        # �R���X�g���N�^
        # undirected : �������i�f�t�H���g�F�L���j
        # **************************************************
        # �m�[�h�f�B�N�V���i��������
        self.node_dict = {}
        # �����O���t��
        self.undirected = undirected
        # �v���C�I���e�B�E�L���[
        self.queue = []
    
    class node:
        # **************************************************
        # �m�[�h�N���X
        # **************************************************
        
        def __init__(self):
            # **************************************************
            # �R���X�g���N�^
            # **************************************************
            # �אڃm�[�h����{�m�[�h���F�d��}
            self.adjacent_node = {}
            # �ŒZ�o�H���̑O��̃m�[�h�̖��O
            self.last_node = None
            # ���̎��_�̍ŒZ����
            self.dist = None
            # �ŒZ�o�H����t���O
            self.is_decision = False

    def add_node(self, arg_nodes):
        # **************************************************
        # �m�[�h�̒ǉ�
        # arg_nodes : �m�[�h�̖��̃��X�g
        # **************************************************
        # �m�[�h���X�g�Ƀm�[�h�C���X�^���X�ǉ�
        for name in arg_nodes:
            self.node_dict[name] = self.node()
            
    def add_edge(self, arg_edges):
        # **************************************************
        # �G�b�W�̒ǉ�
        # arg_edges : �G�b�W��\���^�v���̃��X�g�ifrom, to, weight�j
        # **************************************************
        # �m�[�h�C���X�^���X�Ƀf�[�^�ǉ�
        for edge_tuple in arg_edges:
            # �v�f���ŕ��򂵁A�d�ݕt��
            weight = 1
            if len(edge_tuple) == 3:
                weight = edge_tuple[2]
            # �s��̃m�[�h�ݒ�
            self.node_dict[edge_tuple[0]].adjacent_node[edge_tuple[1]] = weight
            # �����̏ꍇ�t�������ݒ�
            if self.undirected:
                self.node_dict[edge_tuple[1]].adjacent_node[edge_tuple[0]] = weight
        
    def dijkstra(self, start, goal):
        # **************************************************
        # �_�C�N�X�g���@�ɂ��ŒZ�o�H�T��
        # start : �J�n�m�[�h�̖���
        # **************************************************
        # �X�^�[�g�m�[�h���L���[�ɒǉ� 
        heapq.heappush(self.queue, (0, start, None))
        
        # �L���[����ɂȂ�܂�
        while (len(self.queue) != 0):
            # �����ŏ��̃L�[���擾
            dist, key, last = heapq.heappop(self.queue)
            
            # ����ς݂̃m�[�h�̏ꍇ����
            if self.node_dict[key].is_decision:
                continue
                
            # ����t���O�𗧂ċ����m��A�O��m�[�h�X�V
            self.node_dict[key].is_decision = True
            self.node_dict[key].dist = dist
            self.node_dict[key].last_node = last
            
            
            # �S�[���ɂ�����I��
            if key == goal:
                break
            
            # �m��m�[�h����̋����v�Z
            # �Ȃ����Ă���m�[�h�m�F
            for adj_key in self.node_dict[key].adjacent_node.keys():
                # �܂����肵�Ă��Ȃ��ꍇ
                if not self.node_dict[adj_key].is_decision:
                    # �D��x�t���L���[��(dist, key)��ǉ�
                    heapq.heappush(self.queue, (dist + self.node_dict[key].adjacent_node[adj_key], adj_key, key))
                    
        # last_node �����ǂ��ďo��
        path = []
        last = goal
        while True:
            path.append(last)
            last = self.node_dict[last].last_node
            if last is None:
                break
        # ���]���ďo��
        return path[::-1]