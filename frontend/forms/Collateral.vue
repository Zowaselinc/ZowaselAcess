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
FARMLAND
</h2> <br>
      <form
id="register-form"
action="javascript:void()"
@submit="submitForm($event)"
>

            <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">BVN</label>
                            <input
type="text"
class="form-control"
required
name="bvn"
placeholder="Enter bank verification no"
>
                        </div>



                        <div class="col">
                            <label for="">How many farmlands do you have?</label>
                            <input
type="number"
class="form-control"
required
name="nooffarmlands"
placeholder="Enter main source of income"
>
                        </div></div></div>


                        <div class="form-group">   
                            <div
class="row radios-container"
>
<div class="col-3 radios">

    <label for="">Are you the owner of your farms or a caretaker?</label>
</div>

    <div class="col-3 radios">
                            <input
type="radio"
name="ownerorcaretaker"
value="Owner"
>
                            <label for="">Owner</label>
                        </div>
                        <div class="col-3 radios">
                            <input
type="radio"
name="ownerorcaretaker"
value="Caretaker"
>
                            <label for="">Caretaker</label>
                        </div>

                        <div class="col-3 radios">
                            <input
type="radio"
name="ownerorcaretaker"
value="Inherited"
>
                            <label for="">Inherited</label>
                        
                        </div></div></div>

                        <div class="form-group">
                    <label for="">If Caretaker, what is the name of the farm owner?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="farmownername"
placeholder="Enter Farm Owner Name"
>
                </div>

                <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Farm owner's Phone Number</label>
                            <input
type="text"
class="form-control"
required
name="FarmOwnerPhoneNo"
placeholder="Enter Farm Owner Phone No"
>
                        </div>



                        <div class="col">
                            <label for="">What is your relationship with them?</label>
                            <input
type="text"
class="form-control"
required
name="relationshipwithowner"
placeholder="Enter Relationship With Owner"
>
                        </div></div></div>

                        <div class="form-group">
                    <label for="">If Inherited, from whom did you inherit the farmland?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="inheritedfrom"
placeholder="Enter Who you inherited from"
>
                </div>

                <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What is the size of your farm(s)?</label>
                            <input
type="text"
class="form-control"
required
name="sizeoffarm"
placeholder="Enter Size of Farm"
>
                        </div>



                        <div class="col">
                            <label for="">Where is your farm(s) located? (Take coordinates of farm)</label>
                            <input
type="text"
class="form-control"
required
name="farmcoordinates"
placeholder="Enter Farm Coordinates"
>
                        </div></div></div>

                        <div class="form-group">
                    <label for="">Farm Location/Address</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="farmaddress"
required
placeholder="Enter your farm address"
>
                </div>


                <div class="form-group">   
                            <div
class="row radios-container"
>
<div class="col-3 radios">

    <label for="">Apart from crop cultivation, do you keep animals?</label>
</div>

    <div class="col-3 radios">
                            <input
type="radio"
name="keepsanimals"
value="Yes"
>
                            <label for="">Yes</label>
                        </div>
                        <div class="col-3 radios">
                            <input
type="radio"
name="keepsanimals"
value="No"
>
                            <label for="">No</label>
                        </div>
                    
                    </div>
                    </div>


                    <div class="form-group">
                    <label for="">If Yes, what do your animals eat and where do they live?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="animalsfeedon"
placeholder="Enter your answer"
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
//import OptionList from './components/OptionList.vue';
import AuthSharedLayout from "@/layouts/shared/AuthSharedLayout.vue";
export default {
    name: "Collateral",
    components : {
        AuthSharedLayout
    },
    data(){
        
    },
    mounted() {
    },
    methods: {
        
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";
</style>