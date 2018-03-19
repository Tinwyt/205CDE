$('#SelectProduct').change(function(e){
if($(this).val() == "Cap"||$(this).val() == "Tote-bag"){
    $("#Size option[value='Fixed']").prop('disabled',false);
    $("#Size option[value='XS']").prop('disabled',true);
    $("#Size option[value='S']").prop('disabled',true);
    $("#Size option[value='M']").prop('disabled',true);
    $("#Size option[value='L']").prop('disabled',true);
    $("#Size option[value='XL']").prop('disabled',true);
}
else {
      
    $("#Size option[value='Fixed']").prop('disabled',true);
    $("#Size option[value='XS']").prop('disabled',false);
    $("#Size option[value='S']").prop('disabled',false);
    $("#Size option[value='M']").prop('disabled',false);
    $("#Size option[value='L']").prop('disabled',false);
    $("#Size option[value='XL']").prop('disabled',false);
    }
})

function Confirm(){
        var opt1=document.getElementById("SelectProduct").value;
        var opt2=document.getElementById("Size").value;
	    var opt3=document.getElementById("Name").value;
        var opt4=document.getElementById("Email").value;
        var opt5=document.getElementById("ShippingAddress").value;
        var response= confirm("Are you sure?\n\nProduct:"+opt1+"\n\nSize:"+opt2+"\n\nName:"+opt3+"\n\nEmail:"+opt4+"\n\nShipping Address:\n"+opt5);
        return response;
}
