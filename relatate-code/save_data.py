# 对象持久化
import pickle 

def saveData(path, recordmat):
    file = open(path, "wb")
    pickle.dump(recordmat, file)
    file.close()
    # 读取保存的文件  
    # readmat = pickle.load(file)    
