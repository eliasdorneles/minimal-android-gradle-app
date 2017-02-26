import android
from android.util import Log
from android.widget import LinearLayout
from android.widget import Button


class MyApp:
    def init_activity(self, activity):
        print("init_activity", activity)
        layout = android.widget.LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)

        button1 = Button(activity)
        button1.setText("Press me")
        button2 = Button(activity)
        button2.setText("Press me too!")

        layout.addView(button1)
        layout.addView(button2)

        activity.setContentView(layout)


app = MyApp()
activity = android.PythonActivity.setListener(app)
app.init_activity(activity)

# TODO: why this doesn't work?
# app.activity = activity
# print('activity', activity)
# print('app.activity', app.activity)
