package wethinkcode.botworld.model;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CoordTest
{
    @Test
    void incrementX(){
        Position p = new Position( 0, 0 );
        Position result = p.incrementX();
        assertEquals( 1, result.x() );
        assertNotEquals( p, result );
    }

    @Test
    void decrementX(){
        Position p = new Position( 0, 0 );
        Position result = p.decrementX();
        assertEquals( -1, result.x() );
        assertNotEquals( p, result );
    }

    @Test
    void incrementY(){
        Position p = new Position( 0, 0 );
        Position result = p.incrementY();
        assertEquals( 1, result.y() );
        assertNotEquals( p, result );
    }

    @Test
    void decrementY(){
        Position p = new Position( 0, 0 );
        Position result = p.decrementY();
        assertEquals( -1, result.y() );
        assertNotEquals( p, result );
    }

    @Test
    void equalCoordsAreEqualButNotTheSame(){
        Position p1 = new Position( 42, 55 );
        Position p2 = new Position( 42, 55 );
        assertEquals( p1, p2 );
        assertEquals( p1.hashCode(), p2.hashCode() );
        assertNotSame( p1, p2 );
    }
}
