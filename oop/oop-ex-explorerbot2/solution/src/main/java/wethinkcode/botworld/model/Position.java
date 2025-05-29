package wethinkcode.botworld.model;

public record Position( int x, int y )
{
    public Position right(){
        return new Position( x() + 1, y() );
    }

    public Position left(){
        return new Position( x() - 1, y() );
    }

    public Position down(){
        return new Position( x(), y() + 1 );
    }

    public Position up(){
        return new Position( x(), y() - 1 );
    }

    @Override
    public String toString(){
        return "Position[" + x() + '@' + y() + ']';
    }
}
