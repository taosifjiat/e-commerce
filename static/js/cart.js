var updateBtn=document.getElementsByClassName("update-cart")

for(var i=0; i< updateBtn.length;i++){
    updateBtn[i].addEventListener('click',function(){
        var productID=this.dataset.product
        var action=this.dataset.action
        console.log(productID)
        console.log(action)
        if(user =='AnonymousUser'){
            console.log("user not log in")
        }
        else{
            console.log("user log in")
            updateUserOrder(productID, action)
            console.log(productID,action)
        }
    })
}
function updateUserOrder(productID,action){
    console.log(productID,action)
    console.log("taosifjiat")
    var url="/updateitem"
    
    fetch=(url,{
        method:"POST",
        headers:{
            'content-type':'application/json',
            'x-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productID':productID,'action':action})
        
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
     console.log("data:",data)
        location.reload()
    })
}