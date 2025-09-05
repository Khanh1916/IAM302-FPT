#!/usr/bin/python
# Copyright (C) 2010 Michael Ligh

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os, time, glob, shutil
from optparse import OptionParser
import subprocess

vm_paths = {
    '/Library/Application Support/VMware Fusion/vmrun': 'fusion',
    '/usr/bin/vmrun': 'ws',
    'C:\\Program Files (x86)\\VMware\\VMware Player\\vmrun.exe': 'ws',
}

def pinfo(msg):
    print ("[INFO] ", msg)

def perror(msg):
    print ("[ERROR] ", msg)

class VMwareAuto:
    def __init__(self, vmx):
        self.vmx = vmx
        self.vmrun  = None
        self.vmtype = None

        if not os.path.isfile(vmx):
            raise 'Cannot find vmx file in ' + vmx

        for (path,type) in vm_paths.items():
            if os.path.isfile(path):
                self.vmrun = path
                self.vmtype = type
                break

        if self.vmrun == None:
            raise 'Cannot find vmrun in ' + ','.join(vm_paths.keys())
        else:
            print ('Found vmrun (running on %s)') % self.vmtype

    def setuser(self, user, passwd):
        self.user = user
        self.passwd = passwd

    def run_cmd(self, cmd, args=[], guest=False):
        print ('Executing ' + cmd + ' please wait...')
        pargs = [self.vmrun, '-T', self.vmtype]
        if guest:
            pargs.extend(['-gu', self.user])
            pargs.extend(['-gp', self.passwd])

        pargs.append(cmd)
        pargs.append(self.vmx)
        pargs.extend(args)

        proc = subprocess.Popen(
            pargs,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        return proc.communicate()[0]

    def list(self):
        pargs = [self.vmrun, 'list']
        print (pargs)
        proc = subprocess.Popen(
            pargs,
            stdout=subprocess.PIPE
        )
        return proc.communicate()[0]

    def start(self):
        return self.run_cmd('start')

    def stop(self):
        return self.run_cmd('stop')

    def revert(self, snapname):
        return self.run_cmd('revertToSnapshot', [snapname])

    def suspend(self):
        return self.run_cmd('suspend')

    def scrshot(self, outfile):
        return self.run_cmd('captureScreen', [outfile], guest=True)

    def copytovm(self, src, dst):
        if not os.path.isfile(src):
            perror('Cannot locate source file ' + src)
            return
        return self.run_cmd(
            'copyFileFromHostToGuest', [src, dst], guest=True)

    def copytohost(self, src, dst):
        return self.run_cmd(
            'copyFileFromGuestToHost', [src, dst], guest=True)

    def winexec(self, file, args=''):
        return self.run_cmd(
            'runProgramInGuest',
            [
                '-noWait',
                '-interactive',
                '-activeWindow',
                file, args
            ],
            guest=True)

    def findmem(self):
        path = os.path.dirname(self.vmx)
        mems = glob.glob('%s/*.vmem' % (path))
        mems = [m for m in mems if "Snapshot" not in m]
        return mems[0] if len(mems) else ''

def main(argv):
    print ('Nothing to do. Import me!')
    return 0

if __name__ == '__main__':
    main(sys.argv)
