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
Crop_quality
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
                            <label for="">Moisture Content</label>
                            <input
v-model="farmer.moisture_content"
type="text"
class="form-control"
required
name="moisture_content"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Foreign matter</label>
                            <input
v-model="farmer.foreign_matter"
type="text"
class="form-control"
required
name="foreign_matter"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Test Weight</label>
                            <input
v-model="farmer.test_weight"
type="text"
class="form-control"
required
name="test_weight"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Quality Description</label>
                            <input
v-model="farmer.quality"
type="text"
class="form-control"
required
name="quality"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Rotten/ Shriveled</label>
                            <input
v-model="farmer.rotten_shriveled"
type="text"
class="form-control"
required
name="rotten_shriveled"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Hardness</label>
                            <input
v-model="farmer.hardness"
type="text"
class="form-control"
required
name="hardness"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Splits</label>
                            <input
v-model="farmer.splits"
type="text"
class="form-control"
required
name="splits"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Oil Content</label>
                            <input
v-model="farmer.oil_content"
type="text"
class="form-control"
required
name="oil_content"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Infestation</label>
                            <input
v-model="farmer.infestation"
type="text"
class="form-control"
required
name="infestation"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Hectoliter Test Weight</label>
                            <input
v-model="farmer.hectoliter"
type="text"
class="form-control"
required
name="hectoliter"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Total Defects</label>
                            <input
v-model="farmer.total_defects"
type="text"
class="form-control"
required
name="total_defects"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Dockage</label>
                            <input
v-model="farmer.dockage"
type="text"
class="form-control"
required
name="dockage"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Ash Content</label>
                            <input
v-model="farmer.ash_content"
type="text"
class="form-control"
required
name="ash_content"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Acid Insoluble ash</label>
                            <input
v-model="farmer.insoluble_ash"
type="text"
class="form-control"
required
name="insoluble_ash"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Volatile</label>
                            <input
v-model="farmer.volatile"
type="text"
class="form-control"
required
name="volatile"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Mold. % By Weigh</label>
                            <input
v-model="farmer.mold_weight"
type="text"
class="form-control"
required
name="mold_weight"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Drying Process</label>
                            <input
v-model="farmer.drying_process"
type="text"
class="form-control"
required
name="drying_process"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Whole Dead Insects,</label>
                            <input
v-model="farmer.dead_insects"
type="text"
class="form-control"
required
name="dead_insects"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Mammalian excreta</label>
                            <input
v-model="farmer.excreta"
type="text"
class="form-control"
required
name="excreta"
placeholder="Enter response"
>
                        
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Insect Defiled / Infested, by Weigh</label>
                            <input
v-model="farmer.insect_defiled"
type="text"
class="form-control"
required
name="insect_defiled"
placeholder="Enter response"
>
                        </div>                   
                        <div class="col">
                            <label for="">Curcumin Content</label>
                            <input
v-model="farmer.curcumin"
type="text"
class="form-control"
required
name="curcumin"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Extraneous,% by Weight</label>
                            <input
v-model="farmer.extraneous"
type="text"
class="form-control"
required
name="extraneous"
placeholder="Enter response"
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