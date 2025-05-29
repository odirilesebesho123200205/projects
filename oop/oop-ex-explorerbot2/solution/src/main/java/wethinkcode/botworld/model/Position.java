package wethinkcode.botworld.model;

import java.util.Objects;

public record Position( int x, int y )
{
    public Position incrementX(){
        return new Position( x() + 1, y() );
    }

    public Position decrementX(){
        return new Position( x() - 1, y() );
    }

    public Position incrementY(){
        return new Position( x(), y() + 1 );
    }

    public Position decrementY(){
        return new Position( x(), y() - 1 );
    }

    @Override
    public String toString(){
        return "Position[" + x() + '@' + y() + ']';
    }
}
