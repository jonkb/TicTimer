import java.awt.*;
import javax.swing.*;
import java.util.*;

class ClockView extends JPanel implements Runnable {

    private JLabel tLabel = new JLabel();
	static Font bigFont = new Font("arial", Font.BOLD, 18);

    ClockView() {
        this.setPreferredSize(new Dimension(220,40));
        this.add(tLabel);
		tLabel.setFont(bigFont);
        this.refreshTimeDisplay();
    }

    protected String getDigitsAsString(int i) {
        String str = Integer.toString(i);
        if (i<10) return "0"+str;
        return str;
    }

    public void refreshTimeDisplay() {
        Timestamp t = new Timestamp();
        t.fillTimes();
        String display = "Clock Time: " + getDigitsAsString(t.hrs) + ":"
                     + getDigitsAsString(t.mins)  + ":"
                     + getDigitsAsString(t.secs);
        tLabel.setText("  " + display );
        tLabel.repaint();
    }

    public void run() {
	    for (;;) {
		    this.refreshTimeDisplay();
		    try {
		    	Thread.sleep(500);
		    } catch (Exception e) {}
	    }
    }
	
	public String getTimeAsString() {
		return getDigitsAsString(Calendar.getInstance().get(Calendar.HOUR_OF_DAY)) + ":"
                     + getDigitsAsString(Calendar.getInstance().get(Calendar.MINUTE))  + ":"
                     + getDigitsAsString(Calendar.getInstance().get(Calendar.SECOND));
	}
}
