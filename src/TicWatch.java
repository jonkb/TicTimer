/**Tic-free time panel
 * Keeps track of time since last tic.
 * Sends the tenIend event when ten seconds pass without tics
 */
import java.awt.*;
import javax.swing.*;
import java.util.*;

class TicWatch extends JPanel implements Runnable {
    Integer sec_elapsed = new Integer(0);
    Calendar time1;
    Calendar time2;
    Calendar timer = Calendar.getInstance();
    boolean run = true;
    JLabel tLabel = new JLabel();
    static Font bigFont = new Font("arial", Font.BOLD, 26);
    
    TicWatch() {
        this.setPreferredSize(new Dimension(440,40));
        this.add(tLabel);
        tLabel.setFont(bigFont);
        this.refreshTimeDisplay();
    }
    
    public void reset() {
        timer.set(Calendar.HOUR_OF_DAY,0);
        timer.set(Calendar.MINUTE,0);
        timer.set(Calendar.SECOND,0);
        sec_elapsed = 0;
        time1 = Calendar.getInstance();
        this.refreshTimeDisplay();
    }

    public void run() {
        run = true;
        time2 = Calendar.getInstance();
        time2.add(Calendar.SECOND,1);
        time2.add(Calendar.MILLISECOND,-1);
        timer_loop: for (;;) {
            time1 = Calendar.getInstance();
            try {
                Thread.sleep(100);
            } catch (Exception e) {}
            
            if ( time1.after(time2) && run ) {
                time2.add(Calendar.SECOND,1);
                timer.add(Calendar.SECOND,1);
                sec_elapsed++;
            }
            
            if ( sec_elapsed > 9 ) {
                TicTimer.tenIEnd();
                this.reset();
            }
            
            this.refreshTimeDisplay();
            if ( ! run ) break timer_loop;
        }
    }

    public void pauseWatch() {
        run = false;
    }

    protected String getDigitsAsString(int i) {
        String str = Integer.toString(i);
        if (i<10) return "0"+str;
        return str;
    }
    
    public String getTimeAsString() {
        return getDigitsAsString(timer.get(Calendar.HOUR_OF_DAY)) + ":"
             + getDigitsAsString(timer.get(Calendar.MINUTE))  + ":"
             + getDigitsAsString(timer.get(Calendar.SECOND));
    }

    public void refreshTimeDisplay() {
        String display = "Tic-free time:  " + getTimeAsString();
        tLabel.setText( display );
        tLabel.repaint();
    }
}
