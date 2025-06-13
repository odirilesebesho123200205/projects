package wethinkcode.schedule;

import javax.jms.JMSException;

import org.junit.jupiter.api.*;
import wethinkcode.loadshed.common.mq.MQ;
import wethinkcode.loadshed.common.mq.MqTopicSender;
import wethinkcode.loadshed.common.mq.test.MqTestFixture;
import wethinkcode.stage.StageService;

/**
 * TODO: javadoc ScheduleServiceMQTest
 */
@Tag( "integrationTest" )
@Disabled
public class ScheduleServiceMQTest extends MqTestFixture
{
    public static final int TEST_PORT = 7777;

    public static final int INITIAL_STAGE = 2;

    public static final int NEW_STAGE = 4;

    private static StageService stageSvc;

    @BeforeAll
    static void startStageService() throws JMSException{
        stageSvc = new StageService().initialise(
            INITIAL_STAGE,
            new MqTopicSender().init( MQ.STAGE_TOPIC ));
        stageSvc.start( TEST_PORT );
    }

    @AfterAll
    static void stopStageService(){
        stageSvc.stop();
    }

    @Test
    void initialStageFetchedOnInit(){
        throw new UnsupportedOperationException( "TODO" );
    }

    @Test
    void stageChangeMsgUpdatesScheduleSvc(){
        throw new UnsupportedOperationException( "TODO" );
    }
}
