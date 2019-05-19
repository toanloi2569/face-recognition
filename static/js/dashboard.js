$(document).ready(function() {
  $('#province_select').change(function(){
      pv = $('#province_select').val() ;
      document.getElementById("warning").style.display = 'block' ;
      document.getElementById("circle").style.display = 'block' ;
      //alert(pv) ;
      setTimeout(function(){
        document.getElementById("warning").style.display = 'none' ;
        document.getElementById("circle").style.display = 'none' ;
      }, 500);
      // Ajax
     load_province_ajax(pv);
  });
});

function load_province_ajax(pv){
  $.ajax({
      url : "/province_ajax",
      type : "post",
      dataType:"text ",
      data : {
          "province_id" : pv
      },
      // result trong hàm success ở dưới chứa kết quả từ server trả về
      success : function (result){
          results = JSON.parse(result);
          update_statistic(results["statistic"],results["date_statistic"]);
          aa = JSON.parse(results["percent_age"]) ;
          bb = JSON.parse(results["percent_jobs"]) ;
          cc = JSON.parse(results["percent_religious"]);
          draw_chart(aa,bb,cc);
      }
}); 
}



function run_statistic(){
  document.getElementById("warning").style.display = 'block' ;
  document.getElementById("box_warning").style.display = 'block' ;
}


function ok(){
  document.getElementById("box_warning").style.display = 'none' ;
  document.getElementById("warning").style.display = 'block' ;
  document.getElementById("circle").style.display = 'block' ;
  setTimeout(function(){
    document.getElementById("warning").style.display = 'none' ;
    document.getElementById("circle").style.display = 'none' ;
  }, 150000);
  pv = $('#province_select').val() ;
  $.ajax({
    url : "/runStatistic",
    type : "post" ,
    timeout : 150000,
    dataType:"text",
    data : {
      "province_id" : pv
    },
    // result trong hàm success ở dưới chứa kết quả từ server trả về
    success : function (result){
      document.getElementById("warning").style.display = 'none' ;
      document.getElementById("circle").style.display = 'none' ;
      results = JSON.parse(result);
      update_statistic(results["statistic"],results["date_statistic"]);
      aa = JSON.parse(results["percent_age"]) ;
      bb = JSON.parse(results["percent_jobs"]) ;
      cc = JSON.parse(results["percent_religious"]);
      draw_chart(aa,bb,cc);
    }
  }); 
}
function cance(){
  document.getElementById("warning").style.display = 'none' ;
  document.getElementById("box_warning").style.display = 'none' ;
}

function max(array){
  var max = 0 ;
  array.forEach(element => {
    if (max < element) {
      max = element ;
    } ;
  });
  return Math.ceil(max) ;
}

function update_statistic(statistic,date_statistic){
  var age = document.getElementById("age");
  age.innerHTML = String(statistic["average_age"]) ;
  var poor = document.getElementById("poor");
  poor.innerHTML = String(statistic["poor_familys"])+ "hộ - " + String(statistic["percent_poor_family"] + "%");
  var date1 = document.getElementById("date1");
  var date2 = document.getElementById("date2");
  var date3 = document.getElementById("date3");
  var date4 = document.getElementById("date4");
  var date5 = document.getElementById("date5");
  var date6 = document.getElementById("date6");
  var date7 = document.getElementById("date7");
  date1.innerHTML = "Cập nhật ngày : " + String(date_statistic) ;
  date2.innerHTML = String(date_statistic) ;
  date3.innerHTML = String(date_statistic) ;
  date4.innerHTML = String(date_statistic) ;
  date5.innerHTML = String(date_statistic) ;
  date6.innerHTML = String(date_statistic) ;
  date7.innerHTML = String(date_statistic) ;

}

function draw_chart(percent_age,percent_jobs,percent_religious){
  // vẽ biểu đồ độ tuổi
  // hiển thị tỷ lệ độ tuổi lao động
  var y = document.getElementById("percent_working_age");
  y.innerHTML = "Tỷ lệ người trong độ tuổi lao động là : " + String(percent_age.percent_working_gender[0]) + " %";
  var z = document.getElementById("percent_man");
  z.innerHTML = "Tỷ lệ giới tính nam là : "+String(percent_age.percent_working_gender[1])+" % ";
  var t = document.getElementById("percent_woman");
  t.innerHTML = "Tỷ lệ giới tính nữ là : "+String(percent_age.percent_working_gender[2])+" %";
  new Chartist.Bar('#table_age', { 
      labels : percent_age.labels.reverse() ,
      series : [
        percent_age.series_man.reverse(),
        percent_age.series_woman.reverse()
      ]
    }, {
      
      seriesBarDistance: 10,
      reverseData: true,
      horizontalBars: true,
      axisY: {
        offset: 70
      }
    });
    // vẽ biểu đồ nghề nghiệp
      // hiển thị tỷ lệ thất nghiệp
      var x = document.getElementById("percent_out_of_work").innerHTML = "Tỷ lệ thất nghiệp là : " + String(percent_jobs.series[8])+"%" ;
      new Chartist.Bar('#table_jobs', {
        labels: percent_jobs.labels,
        series: [percent_jobs.series]
        }, {
         
          axisY: {
            labelInterpolationFnc: function(value) {
              return value + "%";
            }
          }
         }).on('draw', function(data) {
          if(data.type === 'bar') {
            data.element.attr({
              style: 'stroke-width: 30px'
            });
          }
      });
        
      
      
  //   // vẽ biểu đồ tôn giáo
  var data = {
    series: percent_religious.series,
  };
  
  new Chartist.Pie('#table_religious', data, {
    donut: true,
    donutWidth: 80,
    donutSolid: true,
    startAngle: 270,
    showLabel: true
  });
 
}