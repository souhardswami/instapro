<template>
    <div class="likelist">

        

        

        <div id="likes" v-for="like in likes" :key="like.id">
          
                    <section>
                    
                    
                    <img :src="'http://127.0.0.1:8000'+like.profile_img" alt="">
                            <article>
                                
                                 <span class="by"><a href="#" class="author" >{{like.username}}</a></span>
                            </article>
                    
                    
                    </section>
                   
        </div>
	
    </div>
</template>

<script>
import token from '../../apikey.js';
export default {


  props:['name','triger'],


  data(){
    return{
      likes:[]
    }
  },
  watch:{
    triger(){
      this.likelist()
    }
  },
  
  methods:{

    check(){
        
        for (let i=0;i<this.likes.length;i++){
          
          if(this.likes[i].username==this.name){
            

            this.$emit('liked')
          }
        }

        },

        likelist(){
          fetch('http://127.0.0.1:8000/api/likes/',{
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'Authorization': token.HiddenToken
              },
              body: JSON.stringify({"picId":this.$store.state.picId}),
              })
          .then(res=> res.json())
          .then((data)=>{
              console.log(data)
              this.likes=data
              this.check()

            
              
              
              
            
                })
        }

    

  },

  


  mounted(){

    this.likelist()
  

     
      


  }
}
</script>

<style scoped>


.likelist{
    height:50vh;
    margin-left:  auto;
    margin-right: auto;
    width: 30%;
   overflow-y: scroll;
   overflow-x: hidden;

    
    
}
.likelist::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.likelist::-webkit-scrollbar-track {
  background-color: rgba(0, 0, 0, 0.4);
  border-radius: 10px;
}
.likelist::-webkit-scrollbar-thumb {
  background-color: #AD7D52;
  border-radius: 10px;
}

#likes {
            height: 100%;
            max-height: 46px;
                
            
}

#likes section {
                max-width: 340px;
                margin: 18px 0 0 18px;
}

#likes section img {
                    width: 40px;
                    height: 40px;

                    float: left;

                    border-radius: 50%;

                    margin: 0 18px 0 0;
}

#likes section  article {
                    max-width: 240px;
                    display: inline-block;

                    margin-bottom: 18px;
}

#likes section  article:last-child {
                        margin-bottom: 0;
                    }

#likes section  article                     p {
                        margin-top: 5px;
                        color: #82868f;

                        font-size: 14px;
}

.by {
    font-size: 12px;
    font-family: 'Raleway', sans-serif;
    font-weight: 500;
}


.author {
    
    font-weight: 600;
    text-decoration: none;
    color: #AD7D52;
}

</style>
