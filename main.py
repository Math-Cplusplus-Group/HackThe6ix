#
#  main.py
#  HackThe6ix
#
#  Created by Jeffrey, Maliha, Justin  and Lennart on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import sys
import time

import Painter
#import visualization



if __name__ == "__main__":
    t = time.time()

    # Initialize the Master and check its state
    #mas = Master.Master()
    #mas.printState()
    #mas.run()
    #visualization.visualization()

    pain = Painter.Painter()
    pain.mainloop()


    print "\n\nDone in " + str(time.time() - t) + " s"
