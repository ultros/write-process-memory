import ctypes as c
from ctypes import wintypes as w

pid = 7328
addresses = 0x007FF6B0A679AF

k32 = c.windll.kernel32
OpenProcess = k32.OpenProcess
OpenProcess.argtypes = [w.DWORD, w.BOOL, w.DWORD]
OpenProcess.restype = w.HANDLE

WriteMemory = k32.WriteProcessMemory
WriteMemory.argtypes = [w.HANDLE, w.LPCVOID, w.LPVOID, c.c_size_t, c.POINTER(c.c_size_t)]
WriteMemory.restype = w.BOOL

CloseHandle = k32.CloseHandle
CloseHandle.argtypes = [w.HANDLE]
CloseHandle.restype = w.BOOL

process_handle = OpenProcess(0x0020 | 0x0008, False, pid)
# 0x0020 = VirtualMemoryWrite
# 0x0008 = VirtualMemoryOperation

data_to_write = c.c_short(0x9090)

print(WriteMemory(process_handle, addresses, c.byref(data_to_write), c.sizeof(data_to_write), None))

CloseHandle(pid)
