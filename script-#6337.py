# coding: utf-8
#
import uiautomator2 as u2
import time
d = u2.connect()

d(description="Open menu").click()
d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/nav_list"]/android.widget.RelativeLayout[2]').click()
d(resourceId="de.danoeh.antennapod.debug:id/secondaryActionIcon").click()

d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/fragmentLayout"]/android.widget.LinearLayout[1]').click()
time.sleep(2)

d.drag(0.059, 0.788, 0.929, 0.793)
d(resourceId="de.danoeh.antennapod.debug:id/butFF").click()
d(resourceId="de.danoeh.antennapod.debug:id/butFF").click()


