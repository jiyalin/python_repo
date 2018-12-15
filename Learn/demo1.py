import wget


for i in range(10):
    wget.download("http://0d61224e92fa41a1887cb35a759aa4e1-cn-shanghai.alicloudapi.com/test1?dt=20181204")
    print( "round" & i & " is done")
