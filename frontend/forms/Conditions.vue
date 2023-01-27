<template>
    <AuthSharedLayout>
    <div class="big-container">
        <img
class="mobile-logo"
src="@/assets/images/logos/zowasel-logo.png"
alt=""
>
        <div class="left-content">
      <h2 class="text-center">
CONDITIONS
</h2><br>

      <form
id="register-form"
method="post" 
novalidate="true"
@submit.prevent="onSubmit"
>
                    <div
v-if="farmer.error"
class="form-group mt-1"
>
                        <div class="alert alert-danger">
{{ farmer.error }}
</div>
                    </div>
                    <div
v-if="farmer.message"
class="form-group mt-1"
>
                        <div class="alert alert-success">
{{ farmer.message }}
</div>
                    </div>
            
            <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">BVN</label>
                            <input
v-model="farmer.bvn"
type="text"
class="form-control"
required
name="bvn"
placeholder="Enter bank verification no"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Crop Cultivation Period</label>
                            <select
v-model="farmer.duration"
class="form-control"
name="duration"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="before harvest period">
                            before harvest period
</option>
                        <option value="same as harvest period">
                            same as harvest period
</option>
                        <option value="after harvest period">
                            after harvest period
</option>
                        
                    </select>
                        </div></div></div>



                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Zowasel Marketplace registered seller</label>
                            <select
v-model="farmer.seller"
class="form-control"
name="seller"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Yes">
                            Yes
</option>
                        <option value="No">
                            No
</option>                    
                    </select>
                        </div>
                    
                        <div class="col">
                            <label for="">Zowasel Crop Seller MOU</label>
                            <select
v-model="farmer.seller_mou"
class="form-control"
name="seller_mou"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="signed">
                            signed
</option>
                        <option value="not signed">
                            not signed
</option>
                        
                        
                    </select>
                        </div></div></div>
                
                <div class="buttons">
                    <div class="form-group">
                        <button
type="submit"
class="btn  btn-lg green-btn btn-success"
>
Submit
</button>
                    </div>
                    
                </div>
            
                
            </form>
        
        </div>
       
    </div>
    </AuthSharedLayout>
</template>

<script>
import { baseUrl } from "@/pages/dashboard/tables/constants.js";
import AuthSharedLayout from "@/layouts/shared/AuthSharedLayout.vue";
import axios from 'axios';
export default {
    name: "Conditions",
    components : {
        AuthSharedLayout
    },
    data(){
        return {
            farmer:  {
        bvn: '',
        duration: '',
        seller: '',
        seller_mou: '',
        error: null,
        message: null,
      },
    };
    },
    mounted() {
                        
    },
  created() {
  },
    methods: {
        addFarmer(payload) {
      //const path = 'http://127.0.0.1:5000/api/5c_conditions/add';
      axios.post(`${baseUrl}/5c_conditions/add`, payload)
        .then(() => {
            
          //this.initForm();
        })
        .catch((error) => {
          // eslint-disable-next-line
          //console.log(error);
        this.farmer.error = error;
        
        return;
        
         // this.getBooks();
        });
    },
    initForm() {
      this.farmer.bvn = '';
      this.farmer.duration = '';
      this.farmer.seller = '';
      this.farmer.seller_mou = '';
    },
    onSubmit(evt) {
      
      const payload = {
        bvn: this.farmer.bvn,
        duration: this.farmer.duration,
        seller: this.farmer.seller,
        seller_mou: this.farmer.seller_mou,
      };
      
    if (!this.farmer.bvn) {
        this.farmer.error = "bvn is required";
        return;
    }
    if (!this.farmer.seller) {
        this.farmer.error = "seller is required";
        return;
    }
    if (this.farmer.bvn && this.farmer.seller) {
      this.addFarmer(payload);
      this.initForm();
      this.farmer.message = "Details added successfully";
      this.farmer.error = null;
      }
      e.preventDefault();
    },
    
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/scss/main.scss";
</style>