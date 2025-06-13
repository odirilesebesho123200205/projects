package wethinkcode.loadshed.common.mq;


import wethinkcode.loadshed.common.mq.test.MqTestFixture;

import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.TextMessage;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Tests both MqTopicReceiver and MqTopicSender all in one.
 */
public class MqTopicUtilsTest extends MqTestFixture
{
    public static final String TEST_STRING = "Banzaaaaaiiiiii";

    public static final String TEST_TOPIC = "TEST";

    @Test
    void sendAndReceiveEvent() throws JMSException, InterruptedException{
        MqTopicReceiver rcvr = new MqTopicReceiver().init( TEST_TOPIC, (Message message) -> {
            try{
                assertEquals( TEST_STRING, ((TextMessage) message).getText() );
            }catch( JMSException e ){
                throw new RuntimeException( e );
            }
        });

        sendTestMessage( TEST_STRING );
        rcvr.close();
    }

    private void sendTestMessage( String s ) throws JMSException{
        final MqTopicSender tx = new MqTopicSender().init( TEST_TOPIC );
        tx.send( s );
        tx.close();
    }
}
