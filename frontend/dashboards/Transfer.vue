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
Transfer ID: {{ id }} <br>
BVN : {{ scorehistory.bvn }} <br>
AMOUNT: {{ scorehistory.applyLoanAmount }}
{{ farmerBvn }}
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
v-model="farmer.type"
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
:value="loan.type"
>
{{ loan.type }}
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
    //props: ["id", "farmerBvn"],
    props: {
      farmerBvn: [Object, Array],
      id: Number
},

    components : {
        AuthSharedLayout
    },
    data(){
        return {
            //hid: this.$route.id,
            farmer:  {
        bvn: '',type: '',amount: '',
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
      axios.post(`${baseUrl}/transfer/add`, payload)
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
      this.farmer.type = ''
    },
    onSubmit(evt) {
      
      const payload = {
        bvn: this.scorehistory.bvn,
        type: this.farmer.type,
        amount: this.scorehistory.applyLoanAmount,
        //repayment_amount: this.scorehistory.applyLoanAmount * (1+(loan["repayment_months"]/1200))
      };
      
    if (!this.farmer.type) {
        this.farmer.error = "type is required";
        return;
    }
    
    if (this.farmer.type) {
      this.addFarmer(payload);
      this.initForm();
      this.farmer.message = "Offer Successful";
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