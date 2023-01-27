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
Shipment
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
Shipment Details
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
placeholder="Enter tracing_id"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Shipment location</label>
                            <input
v-model="farmer.location"
type="text"
class="form-control"
required
name="location"
placeholder="Enter location"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Loading date</label>
                            <input
v-model="farmer.loading_date"
type="text"
class="form-control"
required
name="loading_date"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Number of people involved in loading</label>
                            <input
v-model="farmer.no_of_people"
type="text"
class="form-control"
required
name="no_of_people"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Type of vehicle & colour</label>
                            <input
v-model="farmer.vehicle_type"
type="text"
class="form-control"
required
name="vehicle_type"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Plate number of vehicle</label>
                            <input
v-model="farmer.plate_no"
type="text"
class="form-control"
required
name="plate_no"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Capacity of vehicle</label>
                            <input
v-model="farmer.vehicle_capacity"
type="text"
class="form-control"
required
name="vehicle_capacity"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Driver's name</label>
                            <input
v-model="farmer.driver_name"
type="text"
class="form-control"
required
name="driver_name"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Driver's phone number</label>
                            <input
v-model="farmer.driver_number"
type="text"
class="form-control"
required
name="driver_number"
placeholder="Enter response"
>
                        </div>
                        
                        <div class="col">
                            <label for="">Goods in Transit insurance</label>
                            <input
v-model="farmer.insurance"
type="text"
class="form-control"
required
name="insurance"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Estimated time to travel to delivery loaction</label>
                            <input
v-model="farmer.delivery_time"
type="text"
class="form-control"
required
name="delivery_time"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Delivery date</label>
                            <input
v-model="farmer.delivery_date"
type="text"
class="form-control"
required
name="delivery_date"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Time of arrival</label>
                            <input
v-model="farmer.arrival_time"
type="text"
class="form-control"
required
name="arrival_time"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Estimated number of Police, Soldiers, Customs, VIO, NDLEA, and FRSC checkpoints encountered</label>
                            <input
v-model="farmer.no_of_police"
type="text"
class="form-control"
required
name="no_of_police"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Cost of Local Government Levy</label>
                            <input
v-model="farmer.local_levy"
type="text"
class="form-control"
required
name="local_levy"
placeholder="Enter response"
>
                        </div></div></div>
                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Cost of State Government Levy</label>
                            <input
v-model="farmer.state_levy"
type="text"
class="form-control"
required
name="state_levy"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Heavy truck levy</label>
                            <input
v-model="farmer.truck_levy"
type="text"
class="form-control"
required
name="truck_levy"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Inter-state levy</label>
                            <input
v-model="farmer.inter_state_levy"
type="text"
class="form-control"
required
name="inter_state_levy"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Number of people involved in offloading</label>
                            <input
v-model="farmer.no_of_offloaders"
type="text"
class="form-control"
required
name="no_of_offloaders"
placeholder="Enter response"
>
                        </div></div></div>
                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Quality check</label>
                            <input
v-model="farmer.quality_check"
type="text"
class="form-control"
required
name="quality_check"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Quality checked; Accept/Reject</label>
                            <input
v-model="farmer.quality_checked"
type="text"
class="form-control"
required
name="quality_checked"
placeholder="Enter response"
>
                        </div></div></div>
                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Quantity Accepted / Accept all</label>
                            <input
v-model="farmer.quality_accepted"
type="text"
class="form-control"
required
name="quality_accepted"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Quantity Rejected / Reject all</label>
                            <input
v-model="farmer.quality_rejected"
type="text"
class="form-control"
required
name="quality_rejected"
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