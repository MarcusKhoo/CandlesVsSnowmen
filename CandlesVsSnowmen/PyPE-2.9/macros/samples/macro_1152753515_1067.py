
'''
This software is licensed under the GPL (GNU General Public License) version 2
as it appears here: http://www.gnu.org/copyleft/gpl.html
It is also included with this archive as `gpl.txt <gpl.txt>`_.
'''



import time

creation_date = 'Wed Jul 12 18:18:35 2006'
name = 'Timeout Failure for all Pythons'

def macro(self):
    print "An exception will be printed after 10 seconds, even though one should be printed after 5"
    self.root.SetStatusText("Check the log.")
    time.sleep(10)
