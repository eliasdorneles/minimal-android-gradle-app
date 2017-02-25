import android
from android.util import Log
from android.widget import LinearLayout
from android.widget import Button
from android.graphics import Color


class MyApp:
    def onStart(self):
        global activity
        print("Application starting up")
        self.layout = layout = android.widget.LinearLayout(self)
        layout.setOrientation(LinearLayout.VERTICAL)

        button1 = Button(self)
        button1.setText("Press me")
        button2 = Button(self)
        button2.setText("Press me too!")
        button2.setBackgroundColor(Color.YELLOW)

        layout.addView(button1)
        layout.addView(button2)

        layout.setBackgroundColor(Color.GREEN)
        activity.setContentView(app.layout)


app = MyApp()
activity = android.PythonActivity.setListener(app)
