import android
from android.util import Log
from android.widget import LinearLayout
from android.widget import Button
from android.graphics import Color


class MyApp:
    def init_activity(self, activity):
        print("init_activity", activity)
        layout = android.widget.LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)

        button1 = Button(activity)
        button1.setText("Press me")
        button2 = Button(activity)
        button2.setText("Press me too!")
        button2.setBackgroundColor(Color.YELLOW)

        layout.addView(button1)
        layout.addView(button2)

        layout.setBackgroundColor(Color.GREEN)
        activity.setContentView(layout)


app = MyApp()
activity = android.PythonActivity.setListener(app)
app.init_activity(activity)

# TODO: why this doesn't work?
# app.activity = activity
# print('activity', activity)
# print('app.activity', app.activity)
