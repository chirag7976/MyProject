let startrecordingbtn = document.getElementById('startRecordingbtn');
let recording_alert_div=document.getElementById('recordingalert');
let timer_Element=document.getElementById('timer-border');
let timer_section_element=document.getElementById('timer_section');


startrecordingbtn.addEventListener('click',()=>{

    alertify.confirm("Are you sure you want to Start Test?",
                            function(){
                                // Yes button callback
                                alertify.success('Recording Started!');
                                startrecordingbtn.setAttribute('style','animation: shadow-pulse 1s infinite;');
                                startrecordingbtn.setAttribute('disabled','');
                                recording_alert_div.removeAttribute('hidden');
                                timer_section_element.removeAttribute('hidden');
                                startRecording();
                                var time=120;
                                var x=setInterval(function(){
                                    minutes= Math.floor(time/60);
                                    seconds=Math.floor(time%60);

                                    document.getElementById('timer').innerHTML= minutes+" m"+' : '+seconds+" s" ;
                                    time=time-1;
                                    if (seconds < 0) {
                                        document.getElementById('timer').innerHTML="Time's Up" ;
                                        clearInterval(x);
                                    }
                                }, 1000);
                            },
                            function(){
                                //alertify.error('Cancel')
                                alertify.error('cancel!');
                            }
    )
});


function startRecording() {

    let testId=document.getElementById('testId');

    // Instantiate xhr object
    let xhr= new XMLHttpRequest();

    xhr.open("GET", "/student/ajaxStartRecording?testId=" + testId.value, true);
    xhr.send();

    //on progress

    // open the object
    xhr.onload=function () {
        if(this.status === 200){
            let time_up =document.getElementById('timer').innerText;
            if(time_up == "Time's Up"){
            timer_section_element.setAttribute('hidden','');
            let finish_test_element=document.getElementById('finish_test');
            setTimeout(() => {
                finish_test_element.removeAttribute('hidden')
            }, 2000);
            recording_alert_div.setAttribute('hidden','');
            startrecordingbtn.removeAttribute('style')
             }
        }
        else{
            alertify.error(
            'something went wrong'
            );
        }
    }
}
