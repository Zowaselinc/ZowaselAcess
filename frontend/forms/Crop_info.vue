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
Crop_info
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
Farmer Details
</p>
            <div class="lines">
                <div class="line" />
                <p>O</p>
                <div class="line" />
            </div>
            
            
            <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">tracing_id</label>
                            <input
v-model="farmer.tracing_id"
type="text"
class="form-control"
required
name="tracing_id"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Crop type</label>
                            <input
v-model="farmer.crop_type"
type="text"
class="form-control"
required
name="crop_type"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Sourcing location</label>
                            <input
v-model="farmer.sourcing_location"
type="text"
class="form-control"
required
name="sourcing_location"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Crop origin (location where crop is cultivated & harvested)</label>
                            <input
v-model="farmer.crop_origin"
type="text"
class="form-control"
required
name="crop_origin"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Crop quantity:</label>
                            <input
v-model="farmer.crop_qty"
type="text"
class="form-control"
required
name="crop_qty"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Crop variety:</label>
                            <input
v-model="farmer.crop_variety"
type="text"
class="form-control"
required
name="crop_variety"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Cooperative name</label>
                            <input
v-model="farmer.cooperative"
type="text"
class="form-control"
required
name="cooperative"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Number of farmer group</label>
                            <input
v-model="farmer.no_of_farmer_group"
type="text"
class="form-control"
required
name="no_of_farmer_group"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        <div class="col">
                            <label for="">Number of female farmers to men</label>
                            <input
v-model="farmer.female_to_male"
type="text"
class="form-control"
required
name="female_to_male"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Farmer name</label>
                            <input
v-model="farmer.farmer_name"
type="text"
class="form-control"
required
name="farmer_name"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                       
                        
                        <div class="col">
                            <label for="">Gender</label>
                            <select
v-model="farmer.gender"
class="form-control"
name="gender"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Male">
                            Male
</option>
                        <option value="Female">
                            Female
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