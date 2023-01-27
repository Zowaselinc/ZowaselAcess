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
KYF
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

            


            
<div class="form-group"><div class="row">
<div class="col">
                        <label for="">First Name</label>
                        <input
v-model="farmer.firstname"
type="text"
class="form-control"
required
>
                    </div>
                    
                    <div class="col">
                        <label for="">Middle Name</label>
                        <input
v-model="farmer.middlename"
type="text"
class="form-control"
>
                    </div>

                    <div class="col">
                        <label for="">Surname</label>
                        <input
v-model="farmer.surname"
type="text"
class="form-control"
required
>
                    </div></div> </div> 
                
                
                <div class="form-group"><div class="row ">
                        <div class="col">
                            <label for="">Email Address</label>
                            <input
v-model="farmer.email"
type="text"
class="form-control"
required
>
                        </div>
                        <div class="col">
                            <label for="">Phone Number</label>
                            <input
v-model="farmer.telephone"
type="text"
class="form-control"
required
>
                        </div>
                        <div class="col">
                            <label for="">Language</label>
                            <input
v-model="farmer.language"
type="text"
class="form-control"
required
>
                        </div></div></div>
                    
                        <div class="form-group">   
                            <div
class="row radios-container"
>
<div class="col-3 radios">

    <label for="">gender</label>
</div>

    <div class="col-3 radios">
                            <input
v-model="farmer.gender"
type="radio"
value="Male"
>
                            <label for="">Male</label>
                        </div>
                        <div class="col-3 radios">
                            <input
v-model="farmer.gender"
type="radio"
value="Female"
>
                            <label for="">Female</label>
                        </div>
                    
                    </div>
                    </div>



                   
                <div class="form-group">
                    <label for="">age</label>

                    <select
v-model="farmer.age"
class="form-control"
required
>
                        <option value="below-24">
below-24
</option>
                        <option value="25-34">
25-34
</option>
                        <option value="35-44">
35-44
</option>
                        <option value="45-above">
45-above
</option>
                    </select>


                </div>
                

                <div class="form-group">   
                            <div
class="row radios-container"
>
<div class="col-3 radios">

    <label for="">Marital Status</label>
</div>

    <div class="col-3 radios">
                            <input
v-model="farmer.maritalstatus"
type="radio"
value="Single"
>
                            <label for="">Single</label>
                        </div>
                        <div class="col-3 radios">
                            <input
v-model="farmer.maritalstatus"
type="radio"
value="Married"
>
                            <label for="">Married</label>
                        </div>

                        <div class="col-3 radios">
                            <input
v-model="farmer.maritalstatus"
type="radio"
value="Divorced"
>
                            <label for="">Divorced</label>
                        </div>
                    
                    </div>
                    </div>

                    <div class="form-group">
                    <div class="row">
                        <div class="col">
                            <label for="">State of Origin</label>
                            <select
v-model="farmer.stateoforigin"
class="form-control"
required
>
                
                                <option
v-for="state in states"
:key="state"
:value="state"
>
{{ state }}
</option>
                            </select>
                        </div>
                        <div class="col">
                            <label for="">NIN</label>
                            <input
v-model="nin"
type="text"
class="form-control"
required
>
                        </div>
                    </div>
                </div>

                <div class="form-group">
                    <label for="">Bank Name</label>
                    <select
v-model="farmer.bankname"
class="form-control"
required
>
                                
                                <option
v-for="bank in banks"
:key="bank"
:value="bank"
>
{{ bank }}
</option>
                            </select>
                </div>

                <div class="form-group"><div class="row ">
                        <div class="col">
                            <label for="">Account Number</label>
                            <input
v-model="farmer.accountno"
type="text"
class="form-control"
required
>
                        </div>
                        <div class="col">
                            <label for="">BVN</label>
                            <input
v-model="farmer.bvn"
type="text"
class="form-control"
required
>
                        </div></div></div>

                        <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Means of identification</label>

                    <select
v-model="farmer.meansofid"
class="form-control"
required
>
                        <option value="National ID card">
                            National ID card
</option>
                        <option value="International Passport">
                            International Passport
</option>
                        <option value="Drivers License">
                            Driver License
</option>
                        <option value="Voters Card">
                            Voters Card
</option>
                    </select>
                    </div>
                    

                    <div class="col">
                        <label for="">Issue Date</label>
                        <input
v-model="issuedate"
type="text"
class="form-control"
required
placeholder="MM/DD/YYYY"
>
                    </div>

                    <div class="col">
                        <label for="">Expiry Date</label>
                        <input
v-model="expirydate"
type="text"
class="form-control"
required
placeholder="MM/DD/YYYY"
>
        
                    </div>

                </div> </div> 
                    
               
                <div class="form-group">
                    <label for="">Permanent address</label>
                    <input
id="formGroupExampleInput"
v-model="farmer.permanentaddress"
type="text"
class="form-control"
required
>
                </div>
                <div class="form-group">
                    <label for="">Nearest market or church/mosque townhall</label>
                    <input
id="formGroupExampleInput2"
v-model="farmer.landmark"
type="text"
class="form-control"
required
>
                </div>
                <div class="form-group">
                    <div class="row">
                        <div class="col">
                            <label for="">In a Farmers group/Cooperative?</label>
                            <select
v-model="farmer.isinagroup"
class="form-control"
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
                            <label for="">If No, Reason for not being in one</label>
                            <input
v-model="farmer.reasonnogroup"
type="text"
class="form-control"
required
>
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <div class="row">
                        <div class="col">
                            <label for="">What is the name of your farmer group/Cooperative?</label>
                            <input
v-model="farmer.group"
type="email"
required
class="form-control"
>
                        </div>
                        <div class="col">
                            <label for="">Number of Members</label>
                            <select
v-model="farmer.numberofmembers"
class="form-control"
required
>
                        <option value="0-9">
0-9
</option>
                        <option value="10-99">
10-99
</option>
                        <option value="100-999">
100-999
</option>
                        <option value="1000-above">
1000-above
</option>
                    </select>

                        </div>
                        
                    
                    </div>
                </div>
                <br>
                <h2 class="text-center">
NEXT OF KIN
</h2><br>
                


            <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Next of Kin First Name</label>
                        <input
v-model="farmer.firstnamenok"
type="text"
class="form-control"
required
>
                    </div>
                    

                    <div class="col">
                        <label for="">Next of Kin Middle Name</label>
                        <input
v-model="farmer.middlenamenok"
type="text"
class="form-control"
>
                    </div>

                    <div class="col">
                        <label for="">Next of Kin surname</label>
                        <input
v-model="farmer.surnamenok"
type="text"
class="form-control"
required
>
                    </div>

                </div> </div> 

                <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Relationship with Next of Kin</label>
                        <select
v-model="farmer.relationshipnok"
class="form-control"
required
>
                        <option value="Child">
                            Child
</option>
                        <option value="Spouse">
                            Spouse
</option>
                        <option value="Parent">
                            Parent
</option>
                        <option value="Sibling">
                            Sibling
</option>
                        <option value="Other">
                            Other
</option>
                    </select>

                    </div>
                    

                    <div class="col">
                        <label for="">Next of Kin Occupation</label>
                        <input
v-model="farmer.occupationnok"
type="text"
class="form-control"
required
>
                    </div>

                </div> </div> 

                <div class="form-group"><div class="row">

            <div class="col">
                        <label for="">Next of Kin telephone</label>
                        <input
v-model="telephonenok"
type="text"
class="form-control"
required
>
                    </div>
                
                    <div class="col">
                        <label for="">Next of Kin NIN</label>
                        <input
v-model="ninnok"
type="text"
class="form-control"
required
>
                    </div>


                </div> </div> 
                
                <div class="form-group">
                    <label for="">Permanent address</label>
                    <input
id="formGroupExampleInput"
v-model="permanentaddressnok"
type="text"
class="form-control"
required
>
                </div>
                <div class="form-group">
                    <label for="">Nearest market or church/mosque townhall</label>
                    <input
id="formGroupExampleInput2"
v-model="landmarknok"
type="text"
class="form-control"
required
>
                </div>            
                        
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
import states from "@/data/states";
import banks from "@/data/banks";
import axios from 'axios';
export default {
    
    name: "Kyf",
    components : {
    AuthSharedLayout
        
    },
    data(){
        return {
            farmer:  {
        firstname:'',surname:'',middlename:'',email:'',telephone:'',age:'',
        gender:'',language:'',maritalstatus:'',bankname:'',accountno:'',bvn:'',
        meansofid:'',issuedate:'',expirydate:'',
        nin:'',permanentaddress:'',landmark:'',
        stateoforigin:'',isinagroup:'',reasonnogroup:'',group:'',
        numberofmembers:'',firstnamenok:'',surnamenok:'',middlenamenok:'', 
        relationshipnok:'',occupationnok:'',telephonenok:'',permanentaddressnok:'',
        landmarknok:'',ninnok:'',
        error: null,message: null,
      },
                banks : banks,
                states : states,
                
            };
    },
    mounted() {
    },
    methods: {
        addFarmer(payload) {
      //const path = 'http://127.0.0.1:5000/api/farmer/add';
      axios.post(`${baseUrl}/farmer/add`, payload)
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
      this.farmer.firstname = '';this.farmer.surname = '';this.farmer.middlename = '';
      this.farmer.email = '';this.farmer.telephone = '';this.farmer.age = '';
      this.farmer.gender = '';this.farmer.language = '';this.farmer.maritalstatus = '';
      this.farmer.bankname = '';this.farmer.accountno = '';this.farmer.bvn = '';
      this.farmer.meansofid = '';this.farmer.issuedate = '';this.farmer.expirydate = '';
      this.farmer.nin = '';this.farmer.permanentaddress = '';this.farmer.landmark = '';
      this.farmer.stateoforigin = '';this.farmer.isinagroup = '';this.farmer.reasonnogroup = '';
      this.farmer.group = '';this.farmer.numberofmembers = '';this.farmer.firstnamenok = '';
      this.farmer.surnamenok = '';this.farmer.middlenamenok = '';this.farmer.relationshipnok = '';
      this.farmer.occupationnok = '';this.farmer.telephonenok = '';this.farmer.permanentaddressnok = '';
      this.farmer.landmarknok = '';this.farmer.ninnok = '';
    },
    onSubmit(evt) {
      
      const payload = {
        firstname: this.farmer.firstname,surname: this.farmer.surname,middlename: this.farmer.middlename,
        email: this.farmer.email,telephone: this.farmer.telephone,age: this.farmer.age,
        gender: this.farmer.gender,language: this.farmer.language,maritalstatus: this.farmer.maritalstatus,
        bankname: this.farmer.bankname,accountno: this.farmer.accountno,bvn: this.farmer.bvn,
        meansofid: this.farmer.meansofid,issuedate: this.farmer.issuedate,expirydate: this.farmer.expirydate,
        nin: this.farmer.nin,permanentaddress: this.farmer.permanentaddress,landmark: this.farmer.landmark,
        stateoforigin: this.farmer.stateoforigin,isinagroup: this.farmer.isinagroup,reasonnogroup: this.farmer.reasonnogroup,
        group: this.farmer.group,numberofmembers: this.farmer.numberofmembers,firstnamenok: this.farmer.firstnamenok,
        surnamenok: this.farmer.surnamenok,middlenamenok: this.farmer.middlenamenok,relationshipnok: this.farmer.relationshipnok,
        occupationnok: this.farmer.occupationnok,telephonenok: this.farmer.telephonenok,permanentaddressnok: this.farmer.permanentaddressnok,
        landmarknok: this.farmer.landmarknok,ninnok: this.farmer.ninnok,
      };
      this.addFarmer(payload);
      this.initForm();
      this.farmer.message = "Details added successfully";
      e.preventDefault();
    },
    
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";
</style>