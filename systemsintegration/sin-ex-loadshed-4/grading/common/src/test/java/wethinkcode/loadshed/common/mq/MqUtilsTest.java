package wethinkcode.loadshed.common.mq;

import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.TextMessage;

import org.junit.jupiter.api.*;
import wethinkcode.loadshed.common.mq.MQ.DestinationType;
import wethinkcode.loadshed.common.mq.test.MqTestFixture;

import static org.junit.jupiter.api.Assertions.*;
import static wethinkcode.loadshed.common.mq.MQ.DestinationType.QUEUE;
import static wethinkcode.loadshed.common.mq.MQ.DestinationType.TOPIC;

/**
 * Tests both ActiveMqReceiver and MqTopicSender all in one.
 */
public class MqUtilsTest extends MqTestFixture
{
    public static final String TEST_STRING = "Banzaaaaaiiiiii";

    @Test
    void sendAndReceiveTopicEvent(){
        try(  ActiveMqReceiver rcvr = new ActiveMqReceiver( DestinationType.TOPIC ) ){
            rcvr.listenOn( MQ.TEST_TOPIC, (Message message) -> {
                try{
                    System.out.println( "Topic received " + ((TextMessage) message).getText() );
                    assertEquals( TEST_STRING, ((TextMessage) message).getText() );
                }catch( JMSException e ){
                    throw new RuntimeException( e );
                }
            } );

            sendTestMessage( MQ.TEST_TOPIC, TEST_STRING );
            snooze( 10 );
        }catch( JMSException | RuntimeException e ){
            fail( e );
        }
    }

    @Test
    void sendAndReceiveQueueMessage(){
        try(  ActiveMqReceiver rcvr = new ActiveMqReceiver( DestinationType.QUEUE ) ){
            sendTestMessage( MQ.TEST_QUEUE, TEST_STRING );
            snooze( 10 );
            Message incoming = rcvr.receive( MQ.TEST_QUEUE );
            String msg = ((TextMessage) incoming).getText();
            assertEquals( TEST_STRING, msg );
        }catch( JMSException ex ){
            fail( ex );
        }
    }

    @Test
    void listenOnQueueShouldFail(){
        ActiveMqReceiver r = new ActiveMqReceiver( DestinationType.QUEUE );
        assertThrows( IllegalStateException.class, () -> {
            r.listenOn( MQ.TEST_QUEUE, (msg) -> {});
        });
    }

    @Test
    void receiveFromTopicShouldFail(){
        ActiveMqReceiver r = new ActiveMqReceiver( DestinationType.TOPIC );
        assertThrows( IllegalStateException.class, () -> {
            r.receive( MQ.TEST_TOPIC );
        });
    }

    private void sendTestMessage( String destination, String s ) throws JMSException{
        DestinationType kind = destination.startsWith( "queue:" )
            ? QUEUE
            : TOPIC;
        final ActiveMqSender tx = new ActiveMqSender( kind ).openOn( destination );
        tx.send( s );
        tx.close();
    }

    private static void snooze( int milliseconds ){
        try{
            Thread.sleep( milliseconds );
        }catch( InterruptedException ex ){
            // ...
        }
    }
}
