<template>
    <div>

     
      

        <button class="button"  @click="disLogin">Login</button>
        
        
                        <div id="myModal" class="modal" v-if="show">
                                    <div class="modal-content">
                                      
                                       
                                        
                                        <span class="close" @click="hidLogin" >&times;</span>
                                        <div>
                                            <img src="https://www.shareicon.net/data/512x512/2017/05/09/885911_logo_512x512.png">
                                        </div>
                                        
                                        <span>log-in</span>
                                        <form >
                                            <input v-model="username" type="text" placeholder="username"  :class="checkUsername">
                                            <br>
                                            <input v-model="password" type="password" placeholder="password" :class="checkPassword">
                                            <br>
                                            <button class="button" @click.stop.prevent="loginSubmit" :disabled="notValid">login</button>
                                        </form>
                                    </div>
                        </div>
    </div>
</template>




<script>
import token from '../../apikey.js';
export default {
    data(){
      return{
        
        show:false,
        username:'',
        password:'',
        send:{
          username:'',
          password:''

        }

      }
    },
    computed:{
      users(){
         return this.$store.state.users
      },
      checkUsername(){
        const nameRegex = /^[a-zA-z]\w{5,}$/;
        const res=nameRegex.test(this.username);
        console.log(res);
        return res ? 'valid' : 'invalid'
      },
      checkPassword(){
        const nameRegex = /^\w{3,}$/;
        const res=nameRegex.test(this.password);
        console.log(res);
        return res ? 'valid' : 'invalid'
      },
      notValid(){

        if(this.checkPassword==='valid' && this.checkUsername==='valid'){
          return false
        }
        else{
          return true
        }

      }

    },
    methods:{
      disLogin(){
          this.show=true
      },
      hidLogin(){
        this.show=false
        
      },
      loginSubmit(){
        console.log("not active")
        this.send.username=this.username,
        this.send.password=this.password
        fetch('http://127.0.0.1:8000/api/userAuth/',{
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                    'Authorization': token.HiddenToken

                  },
                  body: JSON.stringify(this.send)})
        .then(res=> res.json())
        .then((data)=>{
          
          
          
          this.$store.commit('set_user',data),
          this.$store.commit('set_auth',data.id),
          
          this.fetchimg(data[0].id)
        })
        
        this.$router.push('about/')
          
      },
      fetchimg(userId){
        fetch('http://127.0.0.1:8000/api/userImage/',{
              method: 'POST',
              headers: {
                
                'Content-Type': 'application/json',
                'Authorization': token.HiddenToken
              },
              body: JSON.stringify({"user":userId}),
              })
      .then(res=> res.json())
      .then((data)=>{
        
        this.$store.commit('set_myphotos',data)})


      }
      
    }
}
</script>


<style scoped>
.button {
  
  border: none;
  color: black;
  padding: 15px 32px;
  font-weight: 700;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}



.modal {
  display: block; 
  position: fixed; 
  z-index: 1; 
  left: 0;
  top: 0;
  width: 100%;
  height: 100%; 
  overflow: auto; 
  
  background-color: rgba(0,0,0,0.4); 
}
img{
    width:  60px;
    
    margin-right: auto;
    
   
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto; 
  padding: 20px;
  border: 1px solid #888;
  width: 30%; 
}


form input[type="text"],
form input[type="password"] {
  max-width:300px;
  width: 80%;
  line-height:3em;
  font-family: 'Ubuntu', sans-serif;
  margin:1em 2em;
  border-radius:5px;
  /* border:2px solid #f2f2f2; */
  outline:none;
  padding-left:10px;
}
.valid{
 border:2px solid #f2f2f2;
}
.invalid{
  border:2px solid #f2f2f2;
  border-bottom:2px solid red;

}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>