package wethinkcode.stage;

import java.util.concurrent.SynchronousQueue;

import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.TextMessage;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import kong.unirest.HttpResponse;
import kong.unirest.HttpStatus;
import kong.unirest.JsonNode;
import kong.unirest.Unirest;
import org.junit.jupiter.api.*;
import wethinkcode.loadshed.common.mq.ActiveMqReceiver;
import wethinkcode.loadshed.common.mq.ActiveMqSender;
import wethinkcode.loadshed.common.mq.MQ;
import wethinkcode.loadshed.common.mq.MQ.DestinationType;
import wethinkcode.loadshed.common.mq.test.MqTestFixture;
import wethinkcode.loadshed.common.transfer.StageDO;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

/**
 * I test StageService message sending.
 */
@Tag( "expensive" )
public class StageServiceMQTest extends MqTestFixture
{
    public static final int TEST_PORT = 7778;

    public static final int INITIAL_STAGE = 1;

    public static final int FINAL_STAGE = 7;

    private static StageService server;

    private static ObjectMapper objectMapper;

    private ActiveMqReceiver receiver;

    private ActiveMqSender sender;

    @BeforeAll
    public static void startInfrastructure() throws JMSException{
        server = startStageSvc();
        objectMapper = initObjectMapper();
    }

    @AfterAll
    public static void stopTheWorld() throws JMSException{
        server.stop();
    }

    @AfterEach
    public void closeMqConnection() throws JMSException{
        if( sender != null )sender.close();
        sender = null;
        if( receiver != null )receiver.close();
        receiver = null;
    }

    @Test
    @Timeout( 1000 )
    public void sendMqEventWhenStageChanges() throws JMSException, InterruptedException{
        SynchronousQueue<StageDO> rendezvous = new SynchronousQueue<>();
        receiver = new ActiveMqReceiver( DestinationType.TOPIC )
            .listenOn( MQ.STAGE_TOPIC, (Message m) -> {
                try{
                    StageDO s = objectMapper.readValue( ((TextMessage) m).getText(), StageDO.class );
                    System.out.println( "Got stage-change ->" + s.getStage() );
                    rendezvous.put( s );
                }catch( InterruptedException | JsonProcessingException | JMSException ex ){
                    fail( ex );
                }
            } );

        // Posting a new stage to the server should result in a stage-change message
        // getting sent to the MQ.
        final HttpResponse<JsonNode> changeStage = Unirest.post( serverUrl() + "/stage" )
            .header( "Content-Type", "application/json" )
            .body( new StageDO( FINAL_STAGE ) )
            .asJson();
        assertEquals( HttpStatus.OK, changeStage.getStatus() );

        StageDO s = rendezvous.take();
        assertEquals( FINAL_STAGE, s.getStage() );
    }

    private static StageService startStageSvc(){
        server = new StageService().initialise();
        server.start( TEST_PORT );
        return server;
    }

    private static ObjectMapper initObjectMapper(){
        final ObjectMapper mapper = new com.fasterxml.jackson.databind.ObjectMapper();
        mapper.registerModule( new JavaTimeModule() );
        return mapper;
    }

    private String serverUrl(){
        return "http://localhost:" + TEST_PORT;
    }
}
