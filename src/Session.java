import java.awt.*;
import java.util.*;

class Session extends Thread {
    Calendar c1 = Calendar.getInstance();
    Calendar c2;
    Calendar start_time;
    Calendar end_time;
    Thread session_time = new Thread(TicTimer.session_time_panel);
    Thread tic_time = new Thread(TicTimer.tic_time_panel);
    SessionWatch ticwatch = new SessionWatch();
    Thread ticfree = new Thread(ticwatch);
    
    public void run() {
        start_time = Calendar.getInstance();
        session_time.start();
        tic_time.start();
        TicTimer.session_start_label.setText("Session Start Time:  " + getTimeAsString(start_time));
        // TicTimer.running_time = TicTimer.running_time + TicTimer.d_int;
        TicTimer.session_status_panel.setBackground(Color.GREEN);
        TicTimer.session_status_label.setText("Session status: running");
        TicTimer.session_time_panel.reset();
        TicTimer.tic_time_panel.reset();
        TicTimer.d_int = 5.0;
        c1 = start_time;
        c1.add(Calendar.MILLISECOND,300);
        c1.add(Calendar.SECOND,TicTimer.total_time);
        TicTimer.log_stream.println("NewTics subject " + TicTimer.patid + ", session " + TicTimer.session_number
            + ", " + TicTimer.session_type + ", began at " + TicTimer.clock_panel.getTimeAsString() + "\n");

        //Add listener to main frame
        TicTimer.main_frame.removeKeyListener(TicTimer.tic_session);
        TicTimer.main_frame.addKeyListener(TicTimer.tic_session);
        // session loop
        while ( TicTimer.session_running ) {
            TicTimer.main_frame.requestFocus();
            c2 = Calendar.getInstance();
            if ( c2.compareTo(c1) > 0 ) break;
            // c2.add(Calendar.SECOND,10);
            // TicTimer.running_time = TicTimer.running_time + TicTimer.d_int;
            try {
                Thread.sleep(100);
            } catch (Exception e) {}
        }
        if(TicTimer.session_running)
            TicTimer.endSession();
    }
    
    protected String getDigitsAsString(int i) {
        String str = Integer.toString(i);
        if (i<10) 
            return "0"+str;
        return str;
    }

    public String getTimeAsString(Calendar cal) {
        return getDigitsAsString(cal.get(Calendar.HOUR_OF_DAY)) + ":"
             + getDigitsAsString(cal.get(Calendar.MINUTE))  + ":"
             + getDigitsAsString(cal.get(Calendar.SECOND));
    }
}
