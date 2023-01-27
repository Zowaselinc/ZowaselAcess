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
SAFETY
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
placeholder="Enter bvn"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">Do you ferment your Cocoa Beans?</label>
                            <select
v-model="farmer.ferment"
class="form-control"
name="ferment"
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
                            <label for="">If yes, how many days?</label>
                            <input
v-model="farmer.fermentdays"
type="text"
class="form-control"
required
name="fermentdays"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">If No, why?</label>
                            <input
v-model="farmer.fermentreason"
type="text"
class="form-control"
required
name="fermentreason"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What quantity of broken cocoa beans do you get after harvest?</label>
                            <input
v-model="farmer.brokenqty"
type="text"
class="form-control"
required
name="brokenqty"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">What do you do with them?</label>
                            <input
v-model="farmer.dowithbroken"
type="text"
class="form-control"
required
name="dowithbroken"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What quanity of unripe/rotten oil palm FFB do you get after harvest? </label>
                            <input
v-model="farmer.unripeqty"
type="text"
class="form-control"
required
name="unripeqty"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">What do you do with them?</label>
                            <input
v-model="farmer.dowithunripe"
type="text"
class="form-control"
required
name="dowithunripe"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Where do you store your cocoa after harvest?</label>
                            <input
v-model="farmer.ffbstore"
type="text"
class="form-control"
required
name="ffbstore"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">Where do you store your FFB after harvest?</label>
                            <input
v-model="farmer.cocoastore"
type="text"
class="form-control"
required
name="cocoastore"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What pre-emergence and post emergence herbicide do you use in your farmland? Name:</label>
                            <input
v-model="farmer.herbicide"
type="text"
class="form-control"
required
name="herbicide"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">Where do you store your fertilizers, pesticides, fungicides and herbicides?</label>
                            <input
v-model="farmer.herbicidestore"
type="text"
class="form-control"
required
name="herbicidestore"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Where do you buy your agro chemicals from?</label>
                            <input
v-model="farmer.agrochemsource"
type="text"
class="form-control"
required
name="agrochemsource"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">What  do you use to harvest your Oil Palm bunches?</label>
                            <input
v-model="farmer.harvesttool"
type="text"
class="form-control"
required
name="harvesttool"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What do you wear when applying agro chemicals?</label>
                            <input
v-model="farmer.wear"
type="text"
class="form-control"
required
name="wear"
placeholder="Enter response"
>
                        </div>
                                 
                        <div class="col">
                            <label for="">How do you dispose off the chemical containers?</label>
                            <input
v-model="farmer.disposal"
type="text"
class="form-control"
required
name="disposal"
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