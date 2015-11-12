"""
sample code to control "cmd" i/o programetically
"""

def tostring(buf, max):
    _s = []
    for i in range(0, max):
        _s.append(str(buf[i]))
    return "".join(_s)

from System.Diagnostics import Process
p = Process()
p.StartInfo.UseShellExecute = False
p.StartInfo.RedirectStandardOutput = True
p.StartInfo.RedirectStandardInput = True
p.StartInfo.FileName = 'cmd.exe'
p.StartInfo.Arguments = '/k'

p.Start()
i = p.StandardInput
o = p.StandardOutput

from System import Array, Char
buf = Array[Char](range(128))
read = o.ReadAsync(buf, 0, 128)
