import android
from android.util import Log
from android.widget import LinearLayout
from android.widget import Button


class MyApp:
    def __init__(self):
        self._activity = None

    def link_activity(self, activity):
        self._activity = activity

    def onCreate(self):
        layout = LinearLayout(self._activity)
        layout.setOrientation(LinearLayout.VERTICAL)

        button1 = Button(self._activity)
        button1.setText("Press me")
        button2 = Button(self._activity)
        button2.setText("Press me too!")

        layout.addView(button1)
        layout.addView(button2)

        self._activity.setContentView(layout)

    def onStart(self):
        print('activity onStart', self._activity)

    def onResume(self):
        print('activity onResume', self._activity)

    def something_else(self):
        print('something_else')


app = MyApp()
activity = android.PythonActivity.setListener(app)

app.link_activity(activity)

# TODO: why this doesn't work?
# app.activity = activity
# print('activity', activity)
# print('app.activity', app.activity)
