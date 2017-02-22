package org.eliasdorneles;

import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.widget.LinearLayout;
import android.widget.Button;
import android.graphics.Color;


public class Main extends Activity {
     public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Log.i("myapp", "Creating the app");

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);

        Button button1 = new Button(this);
        button1.setText("Press me");
        Button button2 = new Button(this);
        button2.setText("Press me too!");

        layout.addView(button1);
        layout.addView(button2);

        layout.setBackgroundColor(Color.BLUE);
        this.setContentView(layout);
     }
}
