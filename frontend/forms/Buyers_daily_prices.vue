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
Prices
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

            <p
id="emailHelp"
class="form-text text-muted text-center"
>
Prices
</p>
            <div class="lines">
                <div class="line" />
                <p>O</p>
                <div class="line" />
            </div>
            
            
            <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Crop</label>
                            <input
v-model="farmer.crop"
type="text"
class="form-control"
required
name="crop"
placeholder="Enter Crop"
>
                        </div>                    
                        <div class="col">
                        <label for="">location</label>
                        <input
v-model="farmer.location"
type="text"
class="form-control"
required
name="location"
placeholder="Enter location"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Classification</label>
                            <input
v-model="farmer.classification"
type="text"
class="form-control"
required
name="classification"
placeholder="Enter classification"
>
                        </div>                    
                        <div class="col">
                        <label for="">Min Price
</label>
                        <input
v-model="farmer.min_price"
type="text"
class="form-control"
required
name="min_price"
placeholder="Enter min_price"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Ave Price</label>
                            <input
v-model="farmer.ave_price"
type="text"
class="form-control"
required
name="ave_price"
placeholder="Enter ave_price"
>
                        </div>                    
                        <div class="col">
                        <label for="">Max Price</label>
                        <input
v-model="farmer.max_price"
type="text"
class="form-control"
required
name="max_price"
placeholder="Enter max_price"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Quality Specifications</label>
                            <input
v-model="farmer.quality_spec"
type="text"
class="form-control"
required
name="quality_spec"
placeholder="Enter quality_spec"
>
                        </div>                    
                        <div class="col">
                        <label for="">Date</label>
                        <input
v-model="farmer.date_filled"
type="text"
class="form-control"
required
name="date_filled"
placeholder="Enter date_filled"
>
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