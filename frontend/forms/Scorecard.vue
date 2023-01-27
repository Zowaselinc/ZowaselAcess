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
SCORECARD
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
>
                  </div>
                
                  <div class="col">
                      <label for="">Gender</label>
                      <select
v-model="farmer.gender"
class="form-control"
name="gender"
required
>
                        <option value="Male">
                            Male
</option>
                        <option value="Female">
                            Female
</option>                    
                    </select>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Age</label>
                      <select
v-model="farmer.age"
class="form-control"
name="age"
required
>
                        <option value="25 or less">
                            25 or less
</option>
                        <option value="25-34">
                            25-34
</option>               
                        <option value="35 to 45">
                            35 to 45
</option>
                        <option value="45 or more">
                            45 or more
</option>
                    </select>
                  </div>
                
                  <div class="col">
                    <label for="">Owns a bank account</label>
                      <select
v-model="farmer.owns_a_bank_account"
class="form-control"
name="owns_a_bank_account"
required
>
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
                      <label for="">How many farmlands do you have?</label>
                      <select
v-model="farmer.number_of_land"
class="form-control"
name="number_of_land"
required
>
                        
                        <option value="Less than 3 farms">
                            Less than 3 farms
</option>
                        <option value="More than 3 farms">
                            More than 3 farms
</option>                    
                    </select>
                    </div>
                
                    <div class="col">
                      <label for="">Farm address</label>
                      <select
v-model="farmer.address"
class="form-control"
name="address"
required
>
                        <option value="Located in one area">
                            Located in one area
</option>
                        <option value="Located in different area">
                            Located in different area
</option>                    
                    </select>
                  </div></div></div>

                  
                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Size of farm</label>
                      <select
v-model="farmer.size_of_farm"
class="form-control"
name="size_of_farm"
required
>
                        <option value="below 25 hectars">
                            below 25 hectars
</option>
                        <option value="25 hectars and more">
                            25 hectars and more
</option>                    
                    </select>
                  </div>
                
                  <div class="col">
                      <label for="">Age of farm</label>
                      <select
v-model="farmer.years_cultivating"
class="form-control"
name="years_cultivating"
required
>
                        
                        <option value="Less than 5 years">
                            Less than 5 years
</option>
                        <option value="5 to 10 years">
                            5 to 10 years
</option>                
                        <option value="10 to 15 years">
                            10 to 15 years
</option>                
                        <option value="15 to 20 years">
                            15 to 20 years
</option>               
                        <option value="20 to 25 years">
                            20 to 25 years
</option>               
                        <option value="25 years and more">
                            25 years and more
</option>                    
                    </select>
                </div></div></div>

                
                <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Type of crop</label>
                      <select
v-model="farmer.crop"
class="form-control"
name="crop"
required
>
                        
                        <option value="Food crops">
                            Food crops
</option>
                        <option value="Cash crops">
                            Cash crops
</option>                    
                    </select>
                  </div>
                
                  <div class="col">
                      <label for="">Are you the owner of your farms or a caretaker?</label>
                      <select
v-model="farmer.owner_caretaker"
class="form-control"
name="owner_caretaker"
required
>
                        
                        <option value="Owner">
                            Owner
</option>
                        <option value="Rental">
                            Rental
</option>              
                        <option value="Lease">
                            Lease
</option>              
                        <option value="Inherited">
                            Inherited
</option>
                        <option value="Caretaker">
                            Caretaker
</option>                     
                    </select>
                  </div></div></div>
                  
                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Do you grow more than one crop?</label>
                      <select
v-model="farmer.number_of_crops"
class="form-control"
name="number_of_crops"
required
>
                        <option value="Yes">
                            Yes
</option>
                        <option value="No">
                            No
</option>                    
                    </select>
                  </div>
                
                  <div class="col">
                      <label for="">Cropping practise</label>

                      <select
v-model="farmer.intercropping"
class="form-control"
name="intercropping"
required
>
                        <option value="Mixed cropping">
                            Mixed cropping
</option>
                        <option value="Intercropping">
                            Intercropping
</option>                    

                    </select>
                  </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Use of farm machinery (tractor, harvester, planter e.g.) planting and harvesting practise</label>
                      <select
v-model="farmer.machines"
class="form-control"
name="machines"
required
>
                        <option value="Yes">
                            Yes
</option>
                        <option value="No">
                            No
</option>                    
                    </select>
                 </div>
                
                 <div class="col">
                      <label for="">What is the estimate of your monthly income after harvest and sales of your farm produce?</label>
                      <select
v-model="farmer.estimate_monthly_income"
class="form-control"
name="estimate_monthly_income"
required
>
                        <option value="Less than 500,000">
                            Less than 500,000
</option>
                        <option value="500,000 to 1,000,000">
                            500,000 to 1,000,000
</option>              
                    <option value="1,000,000 and more">
                        1,000,000 and more
</option>   
                    </select>
                    </div></div></div>

                  <div class="form-group"><div class="row ">                       
                  <div class="col">
                      <label for="">Are you a member of a farmers cooperative?</label>
                      <select
v-model="farmer.is_in_a_cooperative"
class="form-control"
name="is_in_a_cooperative"
required
>
                        <option value="Yes">
                            Yes
</option>
                        <option value="No">
                            No
</option>                    
                    </select>
                  </div>
                
                  <div class="col">
                      <label for="">How many times have agronomist visited your farm</label>
                      <select
v-model="farmer.no_of_agronomist_visits"
class="form-control"
name="no_of_agronomist_visits"
required
>
                        <option value="Less than once a month">
                            Less than once a month
</option>
                        <option value="More than once a month">
                            More than once a month
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
    name: "Scorecard",
    components : {
        AuthSharedLayout
    },
    data(){
        return {
            farmer:  {
        bvn: '',gender: '',age: '',owns_a_bank_account: '',
        number_of_land: '',address: '',size_of_farm: '',years_cultivating: '',
        crop: '',owner_caretaker: '',number_of_crops: '',intercropping: '',
        machines: '',estimate_monthly_income: '',is_in_a_cooperative: '',no_of_agronomist_visits: '',
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
      //const path = 'http://127.0.0.1:5000/api/scorecard/add';
      axios.post(`${baseUrl}/scorecard/add`, payload)
        .then(() => {
           // this.farmer.error = response.data.message;
           // this.farmer.message = response.data.message;
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
      this.farmer.bvn = '';this.farmer.gender = '';this.farmer.age = '';
      this.farmer.owns_a_bank_account = '';this.farmer.number_of_land = '';this.farmer.address = '';
      this.farmer.size_of_farm = '';this.farmer.years_cultivating = '';this.farmer.crop = '';
      this.farmer.owner_caretaker = '';this.farmer.number_of_crops = '';this.farmer.intercropping = '';
      this.farmer.machines = '';this.farmer.is_in_a_cooperative = '';this.farmer.no_of_agronomist_visits = '';
      this.farmer.estimate_monthly_income = '';
    },
    onSubmit(evt) {
      
      const payload = {
        bvn: this.farmer.bvn,gender: this.farmer.gender,age: this.farmer.age,
        owns_a_bank_account: this.farmer.owns_a_bank_account,number_of_land: this.farmer.number_of_land,address: this.farmer.address,
        size_of_farm: this.farmer.size_of_farm,years_cultivating: this.farmer.years_cultivating,crop: this.farmer.crop,
        owner_caretaker: this.farmer.owner_caretaker,number_of_crops: this.farmer.number_of_crops,intercropping: this.farmer.intercropping,
        machines: this.farmer.machines,is_in_a_cooperative: this.farmer.is_in_a_cooperative,no_of_agronomist_visits: this.farmer.no_of_agronomist_visits,
        estimate_monthly_income: this.farmer.estimate_monthly_income
      };
      
    if (!this.farmer.owns_a_bank_account) {
        this.farmer.error = "owns_a_bank_account is required";
        return;
    }
    if (!this.farmer.number_of_land) {
        this.farmer.error = "number_of_land is required";
        return;
    }
    if (!this.farmer.size_of_farm) {
        this.farmer.error = "size_of_farm is required";
        return;
    }
    if (!this.farmer.years_cultivating) {
        this.farmer.error = "years_cultivating is required";
        return;
    }
    if (!this.farmer.gender) {
        this.farmer.error = "gender is required";
        return;
    }
    if (!this.farmer.age) {
        this.farmer.error = "age is required";
        return;
    }
    if (!this.farmer.bvn) {
        this.farmer.error = "bvn is required";
        return;
    }
    if (!this.farmer.estimate_monthly_income) {
        this.farmer.error = "estimate_monthly_income is required";
        return;
    }
    if (this.farmer.bvn && this.farmer.estimate_monthly_income) {
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