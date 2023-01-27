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
CARE
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
                            <label for="">BVN</label>
                            <input
v-model="farmer.bvn"
type="text"
class="form-control"
required
name="bvn"
placeholder="Enter BVN"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Where is the health centre located?</label>
                            <input
v-model="farmer.healthcentloc"
type="text"
class="form-control"
required
name="healthcentloc"
placeholder="Enter response"
>
                        </div>
                        <div class="col">
                            <label for="">What is the distance from the health centre?</label>
                            <input
v-model="farmer.healthcentdistance"
type="text"
class="form-control"
required
name="healthcentdistance"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">How many healthcare centres are in the community?</label>
                            <input
v-model="farmer.healthcentcount"
type="number"
class="form-control"
required
name="healthcentcount"
placeholder="Enter number"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Are they all functional?</label>
                            <select
v-model="farmer.healthcentfunctional"
class="form-control"
name="healthcentfunctional"
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
                        <option value="Maybe">
                            Maybe
</option>
                    </select>
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Can you afford medical care for members of your household? </label>
                            <select
v-model="farmer.affordable"
class="form-control"
name="affordable"
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
                        <option value="Maybe">
                            Maybe
</option>
                    </select>
                        </div>
                    
                        <div class="col">
                            <label for="" />
                            <select
v-model="farmer.duration"
class="form-control"
name="duration"
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
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">What is the distance from your farm to the health center?  Specify</label>
                            <input
v-model="farmer.farmdistance"
type="text"
class="form-control"
required
name="farmdistance"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">In the event of Injuries at the farm, what do you do? </label>
                            <input
v-model="farmer.injuryevent"
type="text"
class="form-control"
required
name="injuryevent"
placeholder="Enter response"
>
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Do you have access to a First aid box?</label>
                            <select
v-model="farmer.firstaid"
class="form-control"
name="firstaid"
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
                            <label for="">When was the last time you checked your blood pressure and blood sugar level?</label>
                            <input
v-model="farmer.lastcheck"
type="text"
class="form-control"
required
name="lastcheck"
placeholder="Enter response"
>
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">How many children from 5-18years  in your household are in school?</label>
                            <input
v-model="farmer.inschool"
type="number"
class="form-control"
required
name="inschool"
placeholder="Enter number"
>
                        </div>
                    
                        <div class="col">
                            <label for="">What level of education are they?</label>
                            <input
v-model="farmer.level"
type="text"
class="form-control"
required
name="level"
placeholder="Enter response"
>
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">How many schools are there in the community?</label>
                            <input
v-model="farmer.schoolcount"
type="number"
class="form-control"
required
name="schoolcount"
placeholder="Enter number"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Are they functional?</label>
                            <select
v-model="farmer.schoolfunctional"
class="form-control"
name="schoolfunctional"
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
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">What is your highest level of education</label>
                            <input
v-model="farmer.qualification"
type="text"
class="form-control"
required
name="qualification"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">If studying presently, are you studying full-time or part-time?</label>
                            <select
v-model="farmer.studytime"
class="form-control"
name="studytime"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Full-Time">
                            Full-Time
</option>
                        <option value="Part-Time">
                            Part-Time
</option>
                    </select>
                        </div></div></div>


                        <div class="form-group"><div class="row ">                      
                        <div class="col">
                            <label for="">Where did you study?</label>
                            <input
v-model="farmer.studywhere"
type="text"
class="form-control"
required
name="studywhere"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Do you have alternative sources of income?</label>
                            <select
v-model="farmer.altIncomesource"
class="form-control"
name="altIncomesource"
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