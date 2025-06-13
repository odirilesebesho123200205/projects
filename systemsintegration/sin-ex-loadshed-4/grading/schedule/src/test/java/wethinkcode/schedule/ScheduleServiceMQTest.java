package wethinkcode.schedule;

import javax.jms.JMSException;

import org.junit.jupiter.api.*;
import wethinkcode.loadshed.common.mq.ActiveMqSender;
import wethinkcode.loadshed.common.mq.MQ;
import wethinkcode.loadshed.common.mq.test.MqTestFixture;
import wethinkcode.stage.StageService;

import static org.junit.jupiter.api.Assertions.fail;
import static wethinkcode.loadshed.common.mq.MQ.DestinationType.TOPIC;

/**
 * TODO: javadoc ScheduleServiceMQTest
 */
@Tag( "integrationTest" )
public class ScheduleServiceMQTest extends MqTestFixture
{
    public static final int TEST_PORT = 7777;

    public static final int INITIAL_STAGE = 2;

    public static final int NEW_STAGE = 4;

    private static StageService stageSvc;

    @BeforeAll
    static void startStageService() throws JMSException{
        stageSvc = new StageService().initialise(INITIAL_STAGE,
            new ActiveMqSender( TOPIC ).openOn( MQ.STAGE_TOPIC ));
        stageSvc.start( TEST_PORT );
    }

    @AfterAll
    static void stopStageService(){
        stageSvc.stop();
    }

    @Test
    @Disabled
    void initialStageFetchedOnInit(){
        fail( "TODO" );
    }

    @Test
    @Disabled
    void stageChangeMsgUpdatesScheduleSvc(){
        fail( "TODO" );
    }
}
