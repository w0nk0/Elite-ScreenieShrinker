from PyInstaller.lib.macholib.util import fsencoding

__author__ = 'nico'
__version__ = "1.0"

DIR = "."

from os import listdir, unlink
from PIL import Image

files = listdir(DIR)


def out_name(fn, directory):
    fn = fn.replace(".bmp", ".jpg")
    counter = 0
    while fn in listdir(directory):
        fs = fn.split(".")
        fn = fs[0] + "-" + str(counter) + "." + ".".join(fs[1:])
        print fn
    return fn


print '\nThis will compress the big .bmp\'s in E:D\'s screenshot folder into much smaller .jpgs. \n' \
      'It will make \'fake\' versions of the old bmp files that are empty \n' \
      'so that E:D will keep increasing the screenshot numbers and your shots are in \n' \
      'chronological order. Otherwise, E:D would start at Screenshot_0000 again.\n' \
      '\n\nYou need to copy this into your E:D screenshots folder (my pictures/Elite Dangerous) and run it from there.\n'

if not "y" in raw_input('Are you sure you want to do this (y/n)?'):
    raise SystemExit

print '\nProcessing begins.\n'

count = 0
fakes = 0
for f in files:
    if not '.bmp' in f:
        continue
    if not 'creenshot' in f:
        continue
    try:
        fakes += 1
        im = Image.open(f)
        print ""

        print 'Processing', f, " .. ",

        outf = out_name(f, DIR)
        print 'Saving to ', outf, "..",
        im.save(outf, quality=90)

        print 'Done. Truncating..',
        unlink(f)
        with open(f, 'wt') as new_file:
            new_file.write("")
        new_file.close()
        print 'Done!',
        count += 1
    except Exception, err:
        if 'identify' in str(err):
            continue
        print 'Couldn\'t convert', f, err

print "\n", count, ' files processed!'
if not count and not fakes:
    print '\nNo screenshots processed, did you copy to and run this program from your E:D screenie folder?'

dummy = raw_input('Done.\n\nPress Enter to exit!')