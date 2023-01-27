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
Crop_card
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
Crop_card
</p>
      <div class="lines">
          <div class="line" />
          <p>O</p>
          <div class="line" />
      </div>
      
      
      <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Full Name</label>
                      <input
v-model="farmer.farmer_name"
type="text"
class="form-control"
required
name="farmer_name"
placeholder="Enter farmer_name"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                                          
                  <div class="col">
                  <label for="">BVN</label>
                  <input
v-model="farmer.bvn"
type="text"
class="form-control"
required
name="bvn"
placeholder="Enter bvn"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Crop Name</label>
                      <input
v-model="farmer.crop_name"
type="text"
class="form-control"
required
name="crop_name"
placeholder="Enter Crop Name"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Fertilizer (Total Cost)</label>
                      <input
v-model="farmer.fertilizer_cost"
type="text"
class="form-control"
required
name="fertilizer_cost"
placeholder="Enter Cost"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Fertilizer (Breakdown)</label>
                      <input
v-model="farmer.fertilizer"
type="text"
class="form-control"
required
name="fertilizer"
placeholder="Enter Breakdown"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Operation/Mechanization (Total Cost)</label>
                      <input
v-model="farmer.mechanization_cost"
type="text"
class="form-control"
required
name="mechanization_cost"
placeholder="Enter Cost"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Operation/Mechanization (Breakdown)</label>
                      <input
v-model="farmer.mechanization"
type="text"
class="form-control"
required
name="mechanization"
placeholder="Enter Breakdown"
>
                  </div></div></div>
                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Labour (Total Cost)</label>
                      <input
v-model="farmer.labour_cost"
type="text"
class="form-control"
required
name="labour_cost"
placeholder="Enter Cost"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Labour (Breakdown)</label>
                      <input
v-model="farmer.labour"
type="text"
class="form-control"
required
name="labour"
placeholder="Enter Breakdown"
>
                  </div></div></div><div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Harvest (Total Cost)</label>
                      <input
v-model="farmer.harvest_cost"
type="text"
class="form-control"
required
name="harvest_cost"
placeholder="Enter Cost"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Harvest (Breakdown)</label>
                      <input
v-model="farmer.harvest"
type="text"
class="form-control"
required
name="harvest"
placeholder="Enter Breakdown"
>
                  </div></div></div><div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Others (Total Cost)</label>
                      <input
v-model="farmer.other_cost"
type="text"
class="form-control"
required
name="other_cost"
placeholder="Enter Cost"
>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Others (Breakdown)</label>
                      <input
v-model="farmer.others"
type="text"
class="form-control"
required
name="others"
placeholder="Enter Breakdown"
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