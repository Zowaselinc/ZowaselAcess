<template>
  <DefaultNav>
    <AuthSharedLayout>
    <div class="big-container">
        <img
class="mobile-logo"
src="@/assets/images/logos/zowasel-logo.png"

alt=""
>       <div class="left-content">
        
  <div class="container">

        <h1>Loans</h1>
        <hr><br><br>
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
                            <input
v-model="farmer.type"
type="text"
class="form-control"
required
name="type"
>
                          <label for="">COMPANY NAME</label>
                            <input
v-model="farmer.company"
type="text"
class="form-control"
required
name="company"
>
                            <label for="">REPAYMENT MONTHS</label>
                            <input
v-model="farmer.repayment_months"
type="number"
class="form-control"
required
name="repayment_months"
>
                            <label for="">INTEREST RATE PER ANNUM (%)</label>
                            <input
v-model="farmer.interest_rate_per_annum"
type="number"
class="form-control"
required
name="interest_rate_per_annum"
>
                        </div></div></div>
        <button
type="submit"
class="btn  btn-lg green-btn btn-success"
>
Add Loan
</button>
</form>
        <br><br>
        <div
class="table-responsive"
width="100%"
>
        <table
id="datatable"
class="table table-hover"
cellspacing="0"
>
          <thead>
            <tr>
              <th scope="col">
                ID
</th>
              <th scope="col">
                TYPE
</th>
              <th scope="col">
                COMPANY
</th>
              <th scope="col">
                REPAYMENT MONTHS
</th>
              <th scope="col">
                INTEREST RATE PER ANNUM
</th>
              <th scope="col">
                DATE CREATED
</th>
              
            </tr>
          </thead>
          <tbody>
            <tr
v-for="(loan, index) in loans"
:key="index"
>
              <td>{{ loan.id }}</td>
              <td>{{ loan.type }}</td>
              <td>{{ loan.company }}</td>
              <td>{{ loan.repayment_months }}</td>
              <td>{{ loan.interest_rate_per_annum }}</td>
              <td>{{ loan.date_created }}</td>    
          
            </tr>
          </tbody>
        </table>
    </div>
  </div> 
</div>      
    </div>
    </AuthSharedLayout>
  </DefaultNav>
</template>

<script>
import "jquery/dist/jquery.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";
import {baseUrl} from "@/pages/dashboard/tables/constants.js";
import AuthSharedLayout from "@/layouts/shared/AuthSharedLayout.vue";
import DefaultNav from "@/layouts/DefaultNav.vue";
import axios from 'axios';
export default {
    
    name: "Loans",
    components : {
      DefaultNav,
        AuthSharedLayout
    },
    data(){
        return {
          loans: [],
      farmer:  {
        type: '',
        company: '',
        repayment_months: '',
        interest_rate_per_annum: '',
        error: null,
        message: null,
      },
    };
    },
    mounted() {
      axios.get(`${baseUrl}/loan/all`).then((response) => {
      this.loans = response.data.loans;
      $("#datatable").DataTable();
    })
    .catch((error) => {
          console.error(error);
        });
    },

  // Fetch the todos on load
  created() {
    this.getFarmers();
    },
    methods: {
        getFarmers() {
      axios.get(`${baseUrl}/loan/all`)
        .then((res) => {
            this.loans = res.data.loans;
        //    $("#datatable").DataTable();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

            addFarmer(payload) {
      //const path = 'http://127.0.0.1:5000/api/loan/add';
      axios.post(`${baseUrl}/loan/add`, payload)
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
      this.farmer.type = '';
      this.farmer.company = '';
      this.farmer.repayment_months = '';
      this.farmer.interest_rate_per_annum = '';
    },
    onSubmit(evt) {
      
      const payload = {
        type: this.farmer.type,
        company: this.farmer.company,
        repayment_months: this.farmer.repayment_months,
        interest_rate_per_annum: this.farmer.interest_rate_per_annum,
      };
      
    if (!this.farmer.type) {
        this.farmer.error = "type is required";
        return;
    }
    if (!this.farmer.company) {
        this.farmer.error = "company is required";
        return;
    }
    if (!this.farmer.repayment_months) {
        this.farmer.error = "repayment_months is required";
        return;
    }
    if (!this.farmer.interest_rate_per_annum) {
        this.farmer.error = "interest_rate_per_annum is required";
        return;
    }
    if (this.farmer.type && this.farmer.repayment_months) {
      this.addFarmer(payload);
      this.initForm();
      this.farmer.message = "Loan added successfully";
      this.farmer.error = null;
      }
      e.preventDefault();
    },
    
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";
</style>