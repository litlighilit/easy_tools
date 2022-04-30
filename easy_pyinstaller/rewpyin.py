from io import BytesIO

from _data import executable,PYINST_PATH,SPLIT,ERROR
def rewrite(filename=PYINST_PATH):
    pre=BytesIO()
    with open(filename,"rb") as f:
        for line in f:
            if b"python" in line:
                li=line.split(SPLIT)
                assert len(li)==2,ERROR
                _before,_after=li # "_after" should be python executable's path
                assert 65<=_after[0]<=112,ERROR
                line=_before+SPLIT+b'.\..\python.exe'
            pre.write(line)
    with open(filename,"wb") as f:
        f.write(pre.getvalue())
        


if __name__=='__main__':
    rewrite()