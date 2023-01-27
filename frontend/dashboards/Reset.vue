<template>
    <DefaultNav>
    <AuthSharedLayout>
    <div class="big-container">
        <img
class="mobile-logo"
src="@/assets/images/logos/zowasel-logo.png"
alt=""
>
        <div class="left-content">
        <h3 class="text-center">
Select Loan Type
</h3><br>
{{ id }}
{{ scorehistory.bvn }}
{{ this.farmerbvn }}
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
                            <label for="">LOAN TYPE</label>
                            <select
v-model="farmer.loan_type"
class="form-control"
required
>
                                <option
value=""
selected
>
click to select
</option>
                                <option
v-for="loan in loans"
:key="loan"
value="loan"
>
{{ loan.loan_type }}
</option>
                            </select>
                            <br><br><br>
                        </div></div></div>
        <button
type="submit"
class="btn  btn-lg green-btn btn-danger"
>
Approve Request
</button>
</form>
        
        </div>
       
    </div>
    </AuthSharedLayout>
</DefaultNav>
</template>

<script>
import { baseUrl } from "@/pages/dashboard/tables/constants.js";
import AuthSharedLayout from "@/layouts/shared/AuthSharedLayout.vue";
import DefaultNav from "@/layouts/DefaultNav.vue";
import axios from 'axios';
export default {
    name: "Transfer",
    props: ["id", "farmerbvn"],
    components : {
        AuthSharedLayout
    },
    data(){
        return {
            //hid: this.$route.id,
            farmer:  {
        bvn: '',gender: '',age: '',owns_a_bank_account: '',
        number_of_land: '',address: '',size_of_farm: '',years_cultivating: '',
        crop: '',owner_caretaker: '',number_of_crops: '',intercropping: '',
        machines: '',estimate_monthly_income: '',is_in_a_cooperative: '',no_of_agronomist_visits: '',
        error: null,
        message: null,
      },
      loans : [],
      scorehistory : '',
    };
    },
    mounted() {
      axios.get(`${baseUrl}/loan/all`).then((response) => {
      this.loans = response.data.loans;

    })
    .catch((error) => {
          console.error(error);
        });

      axios.get(`${baseUrl}/scorehistory/id=${this.id}`).then((response) => {
      this.scorehistory = response.data;

    })
    .catch((error) => {
          console.error(error);
        });      
    },
  created() {
    this.getData();
//    this.getHistory();
  },
    methods: {
      getData() {
      axios.get(`${baseUrl}/loan/all`)
        .then((res) => {
            this.loans = res.data.loans;
        })
        .catch((error) => {
          console.error(error);
        });
    
      axios.get(`${baseUrl}/scorehistory/id=${this.id}`)
        .then((res) => {
            this.scorehistory = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
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