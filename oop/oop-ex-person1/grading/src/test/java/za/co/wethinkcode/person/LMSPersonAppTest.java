package za.co.wethinkcode.person;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class LMSPersonAppTest
{
    @Test
    void personAppRuns(){
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        System.setOut( new PrintStream( out ));

        PersonApp.main( new String[0] );

        String output = out.toString().strip().toLowerCase();
        assertEquals( 2, countOccurencesOf( "person", output ));
    }

    @Test
    void doesCountMethodWorkForNonOccuringString(){
        assertEquals( 0, countOccurencesOf( "blah", "kjlashfkjhasdkfhaskfjh" ));
    }

    private int countOccurencesOf( String wanted, String aString ){
        int start = 0;
        int mark = 0;
        int count = 0;
        while( mark >= 0 ){
            mark = aString.indexOf( wanted, start );
            if( mark < 0 ) break;
            count++;
            start = mark + wanted.length();
        }
        return count;
    }
}
