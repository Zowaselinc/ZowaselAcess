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
PLANET
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
placeholder="Enter bank verification no"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Do you plan to expand your farm? </label>
                            <select
v-model="farmer.plantoexpand"
class="form-control"
name="plantoexpand"
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
                            <label for="">What crop do you cultivate?</label>
                            <input
v-model="farmer.crop"
type="text"
class="form-control"
required
name="crop"
placeholder="Enter response"
>
                        </div>

                        <div class="col">
                            <label for="">What variety is it?</label>
                            <input
v-model="farmer.variety"
type="text"
class="form-control"
required
name="variety"
placeholder="Enter response"
>
                        </div>
                                        
                        <div class="col">
                            <label for="">Did you raise/buy it? </label>
                            <select
v-model="farmer.raiseorbuy"
class="form-control"
name="raiseorbuy"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Raise">
                            Raise
</option>
                        <option value="Buy">
                            Buy
</option>                                                
                    </select>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">If bought,  Where do you buy it from? Name</label>
                            <input
v-model="farmer.buywhere"
type="text"
class="form-control"
required
name="buywhere"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">How much per seedling? </label>
                            <input
v-model="farmer.seedlingprice"
type="number"
class="form-control"
required
name="seedlingprice"
placeholder="Enter price"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                            <div class="col">
                            <label for="">What quantity did you buy? </label>
                            <input
v-model="farmer.qtybought"
type="text"
class="form-control"
required
name="qtybought"
placeholder="Enter quantity"
>
                        </div>
                                        
                        <div class="col">
                            <label for="">Do you have degraded land in your community?</label>
                            <select
v-model="farmer.degradedland"
class="form-control"
name="degradedland"
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
                        <label for="">When is your planting season now compared to previous years?</label>
                        <input
v-model="farmer.season"
type="text"
class="form-control"
required
name="season"
placeholder="Enter response"
>
                    </div>
                                    
                    <div class="col">
                        <label for="">Do you practice crop rotations to increase biodiversity?</label>
                        <select
v-model="farmer.croprotation"
class="form-control"
name="croprotation"
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
                        <label for="">Do you experience drought, floods, on your farmland?</label>
                        <select
v-model="farmer.disaster"
class="form-control"
name="disaster"
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
                        <label for="">Do you practice bush burning?</label>
                        <select
v-model="farmer.burning"
class="form-control"
name="burning"
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
                        <label for="">Do you own a mill? </label>
                        <select
v-model="farmer.mill"
class="form-control"
name="mill"
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
                        <label for="">At the mill, what is your energy source for milling your FFB?</label>
                        <input
v-model="farmer.energysource"
type="text"
class="form-control"
required
name="energysource"
placeholder="Enter response"
>
                    </div></div></div>

                    <div class="form-group"><div class="row ">
                        
                        <div class="col">
                        <label for="">How many crop trees have you replaced in the past 3 years?</label>
                        <input
v-model="farmer.replacedtree"
type="number"
class="form-control"
required
name="replacedtree"
placeholder="Enter response"
>
                    </div>
                                    
                    <div class="col">
                        <label for="">How were they placed?</label>
                        <input
v-model="farmer.placement"
type="number"
class="form-control"
required
name="placement"
placeholder="Enter response"
>
                    </div></div></div>

                    <div class="form-group"><div class="row ">
                        
                        <div class="col">
                        <label for="">What is the source of water for your farm?</label>
                        <input
v-model="farmer.sourceofwater"
type="text"
class="form-control"
required
name="sourceofwater"
placeholder="Enter response"
>
                    </div>
                                    
                    <div class="col">
                        <label for="">Do you plant cover crops on your farmlands?</label>
                        <select
v-model="farmer.covercrops"
class="form-control"
name="covercrops"
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
                        <label for="">Do you practice intercropping?</label>
                        <select
v-model="farmer.intercrop"
class="form-control"
name="intercrop"
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
                        <label for="">If yes, what crop do you intercrop on your Oil palm or Cocoa farm?</label>
                        <input
v-model="farmer.cropintercropped"
type="text"
class="form-control"
required
name="cropintercropped"
placeholder="Enter response"
>
                </div></div></div>

                    <div class="form-group"><div class="row ">
                        
                        <div class="col">
                        <label for="">Are you aware of good waste management practices? </label>
                        <select
v-model="farmer.wastemgt"
class="form-control"
name="wastemgt"
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
                        <label for="">How do you dispose of your agricultural waste?</label>
                        <input
v-model="farmer.wastedisposal"
type="text"
class="form-control"
required
name="wastedisposal"
placeholder="Enter response"
>
                    </div></div></div>

                    <div class="form-group"><div class="row ">
                        
                        <div class="col">
                        <label for="">Do you reuse or recycle agricultural waste from your farm?</label>
                        <select
v-model="farmer.recyclewaste"
class="form-control"
name="recyclewaste"
required
>
                    <option value="">
                        click to select
</option>
                    <option value="reuse">
                        reuse
</option>
                    <option value="recycle">
                        recycle
</option>                                         
                </select>
                    </div>
                                    
                    <div class="col">
                        <label for="">Has your farm suffered from drought, floods, etc.?</label>
                        <select
v-model="farmer.suffered"
class="form-control"
name="suffered"
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
                        <label for="">If Yes, when?</label>
                        <input
v-model="farmer.whensuffered"
type="text"
class="form-control"
required
name="whensuffered"
placeholder="Enter response"
>
                    </div>
                                    
                    <div class="col">
                        <label for="">Does your farm generate grey water during agricultural activities?</label>
                        <select
v-model="farmer.greywater"
class="form-control"
name="greywater"
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
                        <label for="">If Yes, do you recycle it?</label>
                        <select
v-model="farmer.recyclegreywater"
class="form-control"
name="recyclegreywater"
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
                        <label for="">Is there any unpleasant odor or dust generated from your farming activities which affects the air quality of workers or your neighborhood?</label>
                        <select
v-model="farmer.pollution"
class="form-control"
name="pollution"
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
                            <label for="">If Yes, how often in 12 Months do you generate this pollution?</label>
                            <input
v-model="farmer.pollutionfreq"
type="text"
class="form-control"
required
name="pollutionfreq"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">What measures are in place to address grievances and reduce impact? </label>
                            <input
v-model="farmer.measures"
type="text"
class="form-control"
required
name="measures"
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