from idc import *
from idautils import *
 
currentBase = idaapi.get_imagebase()
fixedBase = 0x100000000L
firstSegment = idc.FirstSeg()

def do_iboot_rebase():
	print "Current base: " + hex(currentBase)
	print "Current Segment: " + hex(firstSegment)
	if (idc.rebase_program(fixedBase, MSF_FIXONCE) == MOVE_SEGM_OK):
		print "did rebase!"
		if (idc.SetSegAddressing(idc.FirstSeg(), 2) > 0):
			print "did bitness fix!"
			pass
		pass
	pass
	if (MakeCode(fixedBase) == 0):
		print "fixed load payload"
		pass

if (currentBase == fixedBase):
	print "Our base is already fixed! Refusing to continue."
else:
	if (currentBase == 0x0L):
		do_iboot_rebase();
	else:
		print "Something's wrong... we can't work with this image."

