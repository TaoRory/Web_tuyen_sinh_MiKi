// JavaScript Document
function layntnam(){
		var d=new Date();
		var thu=d.getDay() /* thu trong tuan 0 -6*/
		if(thu==0){ thu="Chúa Nhật,"}
		if(thu==1){ thu="Thứ hai,"}
		if(thu==2){ thu="Thứ ba,"}
		if(thu==3){ thu="Thứ tư,"}
		if(thu==4){ thu="Thứ năm,"}
		if(thu==5){ thu="Thứ sáu,"}
		if(thu==6){ thu="Thứ bảy,"}
		var ngay=d.getDate() /* lấy ngày trong tháng 1-31*/
		var thang=d.getMonth()+1 /* lay tháng 0-11*/
		var nam=d.getFullYear()
		if(ngay<10){ ngay="0"+ngay}
		if(thang<10){ thang="0"+thang}	
		document.getElementById("ntnam").innerHTML=thu+ngay+"/"+thang+"/"+nam
	}
layntnam()

function laygio()
		{
		var d=new Date()
		var gio=d.getHours()
		var phut=d.getMinutes()
		if(phut<10){ phut="0"+phut}
		var giay=d.getSeconds()
		if(giay<10){ giay="0"+giay}
		document.getElementById("dongho").innerHTML=gio+":"+phut+":"+giay
		setTimeout(laygio,1000)	
		}
	laygio()

	function mytest(anh,text)
			{	
			document.getElementById("demo").innerHTML=text;			
			document.getElementById("anhDoi").src="img/a"+anh+".jpg";
		
			}