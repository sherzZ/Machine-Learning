# ����־û�
import pickle 

def saveData(path, recordmat):
    file = open(path, "wb")
    pickle.dump(recordmat, file)
    file.close()
    # ��ȡ������ļ�  
    # readmat = pickle.load(file)    
