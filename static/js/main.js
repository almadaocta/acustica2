var layer=0;
$(function() {
    function runLayer(l){
        
        $(".disabled").removeClass('disabled');
        $.ajax({
            url : '/api',
            data: {
                "material":document.getElementById('material').value,
                "filtrado":document.getElementById('filtrado').value,
                "length":document.getElementById('length').value,
                "height":document.getElementById('height').value,
                "thickness":document.getElementById('thickness').value,
                "material2":document.getElementById('material2').value,
                "thickness2":document.getElementById('thickness2').value,
                "layer":l
            },
            success: function(data) {
                rc=data['rc'];
                rs=data['rs'];
                ri=data['ri'];
                rd=data['rd'];
                davy=document.getElementById('davy').checked;
                cremer=document.getElementById('cremer').checked;
                iso=document.getElementById('iso').checked;
                sharp=document.getElementById('sharp').checked;
                freq=data['freq'];
                N=data['N'];

                rw=data['rw'];
                stc=data['stc'];
                C=data['C'];
                Ctr=data['Ctr'];
                C503150=data['C503150'];
                C505000=data['C505000'];
                C1005000=data['C1005000'];
                CTR501350=data['CTR501350'];
                CTR505000=data['CTR505000'];
                CTR1005000=data['CTR1005000'];

                console.log(rw)
                

                $('.rwValue').html(rw);
                $('.stcValue').html(stc);
                $('.cValue').html(C);
                $('.ctrValue').html(Ctr);
                $('.C503150Value').html(C503150);
                $('.C505000Value').html(C505000);
                $('.C1005000Value').html(C1005000);
                $('.CTR501350Value').html(CTR501350);
                $('.CTR505000Value').html(CTR505000);
                $('.CTR1005000Value').html(CTR1005000);




                var data = [];
                var trace1 = {
                    x: N,
                    y: rc,
                    name: 'Cremer',
                    type: 'scatter',
                    line: {
                        color: 'rgb(245, 0, 87)',
                    }
                };
                var trace2 = {
                    x: N,
                    y: rd,
                    name: 'Davy',
                    type: 'scatter',
                    line: {
                        color: 'rgb(101, 31, 255)',
                    }
                };
                var trace3 = {
                    x: N,
                    y: rs,
                    name: 'Sharp',
                    type: 'scatter',
                    line: {
                        color: 'rgb(0, 230, 118)',
                    }
                };
                var trace4 = {
                    x: N,
                    y: ri,
                    name: 'ISO',
                    type: 'scatter',
                    line: {
                        color: 'rgb(255, 196, 0)',
                    }
                };                
                if (cremer){
                    data.push(trace1);
                }
                if (davy){
                    data.push(trace2);
                }
                if (sharp){
                    data.push(trace3);
                }
                if (iso){    
                    data.push(trace4);
                }
                
                graphdiv=document.getElementById('graph');
                var layout = {
                    xaxis: {
                        tickmode: "array",
                        tickvals: N,
                        ticktext: freq,
                        title: {
                            text: 'Frecuencia [Hz]',
                            font: {
                            family: 'monospace',
                            size: 18,
                            color: '#212121'
                            }
                        },
                    },
                    yaxis:{
                        title: {
                            text: 'R [Db]',
                            font: {
                            family: 'monospace',
                            size: 18,
                            color: '#212121'
                            }
                        },
                    },
                    paper_bgcolor: "rgba(250,250,250, 0.8)",
                    plot_bgcolor: "rgba(250,250,250, 0.8)",
                    showlegend: true,
                    hovermode:true
                }
    
                Plotly.newPlot(graphdiv, data,layout);

                
                

            }
        });
    }
    $(document).ready(function() {
        graphdiv=document.getElementById('graph');
        var data1 = [];
        var layout = {
            xaxis: {
                title: {
                    text: 'Frecuencia [Hz]',
                    font: {
                      family: 'monospace',
                      size: 18,
                      color: '#212121'
                    }
                },
            },
            yaxis:{
                title: {
                    text: 'R [Db]',
                    font: {
                      family: 'monospace',
                      size: 18,
                      color: '#212121'
                    }
                },
            },
            paper_bgcolor: "rgba(250,250,250, 0.8)",
            plot_bgcolor: "rgba(250,250,250, 0.8)",
            showlegend: true,
            hovermode: false
        }
        Plotly.newPlot(graphdiv,data1,layout);
    });
    $('.addLayer').click(function() { 
        if (layer==0){
            $('.layerM').css('display','flex');
            $('.addLayer').addClass('removeLayer');
            $('.removeLayer').removeClass('addLayer');
            $('.removeLayer').html('<i class="fas fa-times"></i>Eliminar');
            layer=1;
        }
        else{
            $('.layerM').css('display','none');
            $('.removeLayer').addClass('addLayer');
            $('.addLayer').removeClass('removeLayer');
            $('.addLayer').html('<i class="fas fa-plus"></i>Agregar capa')
            layer=0;
        }
    });

    $('#calc').click(function() {
        if (layer==0){
            if ((!document.getElementById('length').value) || (!document.getElementById('height').value) || (!document.getElementById('thickness').value)){
                $('.error2').css('display','none');
                $('.error1').css('display','initial');
            }else if ((document.getElementById('length').value <= 0) || (document.getElementById('height').value <= 0) || (document.getElementById('thickness').value <= 0)){
                $('.error1').css('display','none');
                $('.error2').css('display','initial');
            }else{
                $('.error2').css('display','none');
                $('.error1').css('display','none');
                $('.openIndicadores').css('display','flex');
                runLayer(layer);
            }
        }else if(layer==1){
            if ((!document.getElementById('length').value) || (!document.getElementById('height').value) || (!document.getElementById('thickness').value) || (!document.getElementById('thickness2').value)){
                $('.error2').css('display','none');
                $('.error1').css('display','initial');
            }else if ((document.getElementById('length').value <= 0) || (document.getElementById('height').value <= 0) || (document.getElementById('thickness').value <= 0) || (document.getElementById('thickness2').value <=0)){
                $('.error1').css('display','none');
                $('.error2').css('display','initial');
            }else{
                $('.error2').css('display','none');
                $('.error1').css('display','none');
                $('.openIndicadores').css('display','flex');    
                runLayer(layer);
            }
        } 
    });
    var clicks = 1;
    $('.openIndicadores').click(function() {
        if (clicks % 2 == 1){
            $('.expandIndicadores').css('display','flex')
            $('.openIndicadores').html('<i class="fas fa-times"></i>')
            $('.openIndicadores').addClass('closeIndicadores')
        }else if(clicks % 2 == 0){
            $('.expandIndicadores').css('display','none')
            $('.openIndicadores').html('<span>Índices evaluadores</span>')
            $('.openIndicadores').removeClass('closeIndicadores')
        }
        clicks= clicks + 1;
    });

})









