import java.util.*;

class Timestamp {
        int hrs;
        int mins;
        int secs;
        
        public Timestamp() {}
        
        public Timestamp(int h, int m, int s) {
            hrs = h;
            mins = m;
            secs = s;
        }

        void fillTimes() {
            Calendar now;
            now = Calendar.getInstance();
            hrs = now.get(Calendar.HOUR_OF_DAY);
            mins = now.get(Calendar.MINUTE);
            secs = now.get(Calendar.SECOND);
        }
}
