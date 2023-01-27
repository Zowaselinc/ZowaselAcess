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
LIVING
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
                            <label for="">What is the ownership status of the house that you live in?</label>
                            <select
v-model="farmer.houseowned"
class="form-control"
name="houseowned"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Owner">
                            Owner
</option>
                        <option value="Caretaker">
                            Not Owner
</option>
                        
                        
                    </select>
                        </div></div></div>



                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">If Owner, do you or your family own any other houses other than this that you are living in?</label>
                            <select
v-model="farmer.stayswithfamily"
class="form-control"
name="stayswithfamily"
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
                            <label for="">If a caretaker or inherited, what is your relationship with the owner?</label>
                            <select
v-model="farmer.relationshipwithowner"
class="form-control"
name="relationshipwithowner"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Relative">
                            Relative
</option>
                        <option value="In-Law">
                            In-Law
</option>               
                        <option value="Child">
                            Child
</option>
                        <option value="Friend">
                            Friend
</option>   
                        <option value="Others">
                            Others
</option>   
                        
                    </select>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">How many people are currently living in your household eats from the same pot? </label>
                            <input
v-model="farmer.householdeats"
type="number"
class="form-control"
required
name="householdeats"
placeholder="Enter number"
>
                        </div></div></div>

                        <div class="form-group">
                        <label for="">How many adult males, how many adult females, and how many children under the age of 16 live in your household?</label>
                        <div class="row ">
                        
                        <div class="col">
                            <label for="">Male Under 16</label>
                            <input
v-model="farmer.maleunderage"
type="text"
class="form-control"
required
name="maleunderage"
placeholder="Enter number"
>
                        </div>
                        <div class="col">
                            <label for="">Female Under 16</label>
                            <input
v-model="farmer.femaleunderage"
type="text"
class="form-control"
required
name="femaleunderage"
placeholder="Enter number"
>
                        </div>
                        <div class="col">
                            <label for="">Children Under 16</label>
                            <input
v-model="farmer.childrenunderage"
type="text"
class="form-control"
required
name="childrenunderage"
placeholder="Enter number"
>
                        </div></div></div>

                        <div class="form-group">
                        <label for="">How many adult males, how many adult females, and how many children above the age of 16 live in your household?</label>
                        <div class="row ">
                        
                        <div class="col">
                            <label for="">Male Above 16</label>
                            <input
v-model="farmer.maleaboveage"
type="text"
class="form-control"
required
name="maleaboveage"
placeholder="Enter number"
>
                        </div>
                        <div class="col">
                            <label for="">Female Above 16</label>
                            <input
v-model="farmer.femaleaboveage"
type="text"
class="form-control"
required
name="femaleaboveage"
placeholder="Enter number"
>
                        </div>
                        <div class="col">
                            <label for="">Children Above 16</label>
                            <input
v-model="farmer.childrenaboveage"
type="text"
class="form-control"
required
name="childrenaboveage"
placeholder="Enter number"
>
                        </div></div></div>

                        <div class="form-group">   
                        <div
class="row radios-container"
>
<div class="col-3 radios">

    <label for="">Which of the following people, if any, currently live with you in your household?</label>
</div>

    <div class="col-3 radios">
                            <input
v-model="farmer.liveswith"
type="radio"
value="My partner/spouse"
>
                            <label for="">My partner/spouse</label>
                        </div>

                        <div class="col-3 radios">
                            <input
v-model="farmer.liveswith"
type="radio"
value="My children"
>
                            <label for="">My children</label>
                        </div>

                        <div class="col-3 radios">
                            <input
v-model="farmer.liveswith"
type="radio"
value="My parents"
>
                            <label for="">My parents</label>
                        </div>

                        <div class="col-3 radios">
                            <input
v-model="farmer.liveswith"
type="radio"
value="My grandchildren"
>
                            <label for="">My grandchildren</label>
                        </div>

                        <div class="col-3 radios">
                            <input
v-model="farmer.liveswith"
type="radio"
value="My neices/nephews"
>
                            <label for="">My neices/nephews</label>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Do you or your family own other plots of land other than this that you are living on?</label>
                            <select
v-model="farmer.ownotherlands"
class="form-control"
name="ownotherlands"
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
                            <label for=""> Compared to the general standard of living in Nigeria, how would you describe your standard of living?</label>
                            <select
v-model="farmer.standardofliving"
class="form-control"
name="standardofliving"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Significantly below average">
                            Significantly below average
</option>
                        <option value="Below average">
                            Below average
</option>               
                        <option value="Average">
                            Average
</option>
                        <option value="Above average">
                            Above average
</option>   
                        <option value="Significantly above average">
                            Significantly above average
</option>   
                        
                    </select>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What is your main water source for drinking? And for cooking? And for bathing, laundry, and cleaning?</label>
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
                            <label for="">Do you get water from a source every time you need to use it? </label>
                            <select
v-model="farmer.sourceeverytime"
class="form-control"
name="sourceeverytime"
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
                            <label for="">What is your main cooking method at home?</label>
                            <input
v-model="farmer.cookingmethod"
type="text"
class="form-control"
required
name="cookingmethod"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Do you have electricity where you live?</label>
                            <select
v-model="farmer.haveelectricity"
class="form-control"
name="haveelectricity"
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
                            <label for="">How do you pay for your Government power line usage?</label>
                            <input
v-model="farmer.powerpayment"
type="text"
class="form-control"
required
name="powerpayment"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">What type of toilet do you have in your home?</label>
                            <input
v-model="farmer.typeoftoilet"
type="text"
class="form-control"
required
name="typeoftoilet"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">                        
                        <div class="col">
                            <label for="">Do you have Kitchen Sink in your household? </label>
                            <select
v-model="farmer.kitchensink"
class="form-control"
name="kitchensink"
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
                            <label for="">Are you a member of any cooperative?</label>
                            <select
v-model="farmer.hasgroup"
class="form-control"
name="hasgroup"
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
                            <label for="">Name of Cooperative Society, Association, or Cluster</label>
                            <input
v-model="farmer.group"
type="text"
class="form-control"
required
name="group"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">position in cooperative society.</label>
                            <input
v-model="farmer.position"
type="text"
class="form-control"
required
name="position"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group">Have you accessed any input/loan from the cooperative?<div class="row ">                                                       
                        <div class="col">
                            <label for="" />
                            <select
v-model="farmer.hasaccessedInput"
class="form-control"
name="hasaccessedInput"
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
                            <label for="">If yes, what input?</label>
                            <input
v-model="farmer.input"
type="text"
class="form-control"
required
name="input"
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