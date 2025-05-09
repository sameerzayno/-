
from microbit import *

# عرض الاسم الأول عند التشغيل
display.scroll("Qmar")

# إعلان متغير عددي
counter = 0

while True:
    # عند الضغط على الزر A، عرض أيقونة قل
                display.show(Image.HEART)

                    # عند الضغط على الزر B، زيادة المتغير بمقدار 1
                        if button_b.was_pressed():
                                counter += 1

                                    # عند هز الجهاز، عرض الأعداد الزوجية من 0 
                                                for i in range(0, 11, 2):
                                                            display.show(str(i))
                                                                        sleep(500)