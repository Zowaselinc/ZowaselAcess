<template>
    <AuthSharedLayout>
    <div class="big-container">
        <img
class="mobile-logo"
src="@/assets/images/logos/zowasel-logo.png"
alt=""
>
        <div class="left-content">

      <form
id="register-form"
action="javascript:void()"
@submit="submitForm($event)"
>

<h2 class="text-center">
CREDIT HISTORY
</h2><br>

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
                            <label for="">Have you taken a loan before?</label>
                            <select
class="form-control"
name="hastakenloanbefore"
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
                            <label for="">Where did you get it?</label>
                            <input
type="text"
class="form-control"
required
name="sourceofloan"
placeholder="Enter source of loan"
>
                        </div>

                        <div class="col">
                            <label for="">What was the amount?</label>
                            <input
type="number"
class="form-control"
required
name="pastloanamount"
placeholder="Enter past loan amount"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">              
                        <div class="col">
                            <label for="">How did you manage to pay back/reimburse?</label>
                            <input
type="text"
class="form-control"
required
name="howloanwasrepaid"
placeholder="Enter how loan was repaid"
>
                        </div>

                        <div class="col">
                            <label for="">Would you be ready to pay any interest if given a loan?</label>
                            <select
class="form-control"
name="isreadytopayinterest"
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
                            <label for="">Would you be ready and able, to provide any collateral?</label>
                            <select
class="form-control"
name="canprovidecollateral"
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
                            <label for="">If not, why?</label>
                            <input
type="text"
class="form-control"
required
name="whynocollateral"
placeholder="Enter reason"
>
                        </div></div></div>




                       <br> <h2 class="text-center">
PRODUCTIVITY
</h2><br>
            

            <div class="form-group">
                    <label for="">What crop(s) do you cultivate? </label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="cropscultivated"
required
placeholder="Enter crops cultivated"
>
                </div>


                <div class="form-group"><div class="row ">              
                        <div class="col">
                            <label for="">Do you grow or raise your crop? </label>
                            <input
type="text"
class="form-control"
required
name="growscrops"
placeholder="Enter response"
>
                        </div>

                        <div class="col">
                            <label for="">Type of fertilizers used for your oil palm?</label>
                            <input
type="text"
class="form-control"
required
name="oilpalmfertilizers"
placeholder="Enter Oil Palm fertilizers"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Type of fertilizers used for your cocoa? </label>
                            <input
type="text"
class="form-control"
required
name="cocoafertilizers"
placeholder="Enter response"
>
                        </div></div></div>


                        <div class="form-group">              
                       <label for="">How many times in 12 months do you fertilize your crop? State for each crop</label>
                            <input
type="text"
class="form-control"
required
name="fertilizerfrequency"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">What do you use for pests, fungi and disease management? Name of Pesticide/Brand, Name of Fungicide/Brand, Name of Herbicide/Brand</label>
                            <input
type="text"
class="form-control"
required
name="pestfungherbicides"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">At what stages from cultivation to Harverst do you apply agrochemicals in 12 months on your farmland?</label>
                            <input
type="text"
class="form-control"
required
name="stagechemicalapplied"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">How many drums of oil do you get from your farm both season and off season from your oil palm farm?March - June; August  - December:</label>
                            <input
type="text"
class="form-control"
required
name="noofoildrums"
placeholder="Oil Drums"
>
                      </div>

                      <div class="form-group">              
                       <label for="">How many bags of crops do you get from your farm both in season and off season? Please state for each</label>
                         
                       <div class="row ">              
                        <div class="col">
                            <label for="">i) Sesame</label>
                            <input
type="text"
class="form-control"
required
name="noofbagssesame"
placeholder="Sesame"
>
                        </div>

                        <div class="col">
                            <label for="">ii) Soya beans</label>
                            <input
type="text"
class="form-control"
required
name="NoOfBagsSoyaBeans"
placeholder="Soya beans"
>
                        </div>

                        <div class="col">
                            <label for="">iii) Maize</label>
                            <input
type="text"
class="form-control"
required
name="noofbagsmaize"
placeholder="Maize"
>
                        </div>

                        <div class="col">
                            <label for="">iv) Sorghum</label>
                            <input
type="text"
class="form-control"
required
name="noofbagssorghum"
placeholder="Sorghum"
>
                        </div>
                    
                        <div class="col">
                            <label for="">v) Cocoa beans</label>
                            <input
type="text"
class="form-control"
required
name="noofbagscocoabeans"
placeholder="Cocoa beans"
>
                        </div></div></div>

                        <div class="form-group">              
                       <label for="">For which crop have you been trained best management practice?</label>
                            <input
type="text"
class="form-control"
required
name="croptrainedon"
placeholder="Enter crops trained on"
>
                      </div>

                      <div class="form-group">              
                       <label for="">If any, when, where and by whom?</label>
                            <input
type="text"
class="form-control"
required
name="wherewhenwhotrained"
placeholder="Enter details"
>
                      </div>

                      <div class="form-group">              
                       <label for="">How many times trained in 12 months?</label>
                            <input
type="text"
class="form-control"
required
name="nooftraining"
placeholder="No of timed trained"
>
                      </div>

                      <div class="form-group">              
                       <label for="">How many times do you prune your crop in 12 Month? Oil Palm: Cocoa:</label>
                            <input
type="text"
class="form-control"
required
name="pruningfrequency"
placeholder="No of timed pruned"
>
                      </div>

                      <div class="form-group">              
                       <label for="">In connection with your crop(s), what are the problems you have had in the past 12months?</label>
                            <input
type="text"
class="form-control"
required
name="cropbasedproblems"
placeholder="Enter problems had"
>
                      </div>

                      <div class="form-group">              
                       <label for="">Do you have any crop too young to produce?</label>
                       <select
class="form-control"
name="tooyoungcrops"
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

                      <div class="form-group">              
                       <label for=""> If Yes, what crop and what is their stage now?</label>
                            <input
type="text"
class="form-control"
name="youngcropsandstage"
placeholder="Enter crops and stage"
>
                      </div>

                      <div class="form-group">              
                       <label for=""> When did you start cultivating this crop?</label>
                            <input
type="text"
class="form-control"
name="cultivationstartdate"
placeholder="MM/DD/YYYY"
>
                      </div>

                      <div class="form-group">              
                       <label for="">Do you practice intensive farming?</label>
                       <select
class="form-control"
name="isintensivefarmingpractised"
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

                      <div class="form-group">              
                       <label for="">What economy activity can you point out in your community as a result of your farming activities?</label>
                            <input
type="text"
class="form-control"
name="economicactivities"
placeholder="Enter response"
>
                      </div>


                      <br> <h2 class="text-center">
AGRONOMY
</h2><br>

            <div class="form-group">              
                       <label for="">Do you now know agricultural processes to apply in order to attain better agricultural products</label>
                       <select
class="form-control"
name="knowsagriprocessed"
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

                      <div class="form-group">              
                       <label for="">Which of our agronomist trained you?</label>
                            <input
type="text"
class="form-control"
name="agronomistthattrainedyou"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">Can you farm and manage ecosystems to develop better land and soil texture?</label>
                            <input
type="text"
class="form-control"
name="canmanageecosystem"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">If Yes, how?</label>
                            <input
type="text"
class="form-control"
name="howtomanageecosystem"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">Has several trainning from Zowasel being beneficial to you on the use of fertilizers, and pesticides on your crop(s)?</label>
                       <select
class="form-control"
name="istrainingbeneficial"
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

                      <div class="form-group">              
                       <label for="">From land management to crop storage, can you simplify the farming techniques and field routines to your fellow smallholder farmers base on crop requirement?</label>
                            <input
type="text"
class="form-control"
name="fieldroutines"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">In your harvesting steps of farming practices, what is the difference in yield now compared to previous harvests?</label>
                            <input
type="text"
class="form-control"
name="harvestingchanges"
placeholder="Enter difference"
>
                      </div>

                      <div class="form-group">              
                       <label for="">Has provision and usage of crop calender to track dates and frequency of weeding being of benerits to you?</label>
                       <select
class="form-control"
name="iscropcalendarbeneficial"
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

                      <div class="form-group">              
                       <label for="">If yes, how?</label>
                            <input
type="text"
class="form-control"
name="cropcalendarbenefits"
placeholder="Enter response"
>
                      </div>

                      <div class="form-group">              
                       <label for="">State the benefits of having farm record book and keeping farm record.</label>
                            <input
type="text"
class="form-control"
name="recordkeepingbenefits"
placeholder="Enter response"
>
                      </div>

                      <br> <h2 class="text-center">
PSYCHOMETRICS
</h2><br>

            <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Fluid Intelligence: Remember this number for 5 seconds:</label>
                        <input
type="text"
class="form-control"
required
name="fluidintelligence"
placeholder="59703333"
>
                    </div>
                    

                    <div class="col">
                        <label for="">Attitudes and Beliefs: A big part of success is luck</label>
                        <select
class="form-control"
name="attitudesandbeliefs"
required
>
                        <option value="">
click to select
</option>
                        <option value="True">
                            True
</option>
                        <option value="False">
                            False
</option>
                        
                    </select>
                    </div></div> </div> 

                    <div class="form-group">
                    <label for="">Agribusiness Skills: Which of the following should you take into account when calculating your EOP costs?</label>
                    <input
id="formGroupExampleInput2"
type="text"
class="form-control"
name="agribusinessskills"
required
placeholder="Inventory/Rent"
>
                </div>

                <div class="form-group">
                    <label for="">Ethics and Honesty: What percentage of people are likely to steal in your community?</label>
                    <input
id="formGroupExampleInput2"
type="number"
class="form-control"
name="ethicsandhonesty"
required
placeholder="%"
>
                </div>

                <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Are your neighbors lazy?</label>
                        <select
class="form-control"
name="haslazyneighbors"
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
                        <label for="">Do you save enough?</label>
                        <select
class="form-control"
name="savesenough"
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
                    </div></div> </div> 



                    <br> <h2 class="text-center">
MOBILE DATA
</h2><br>

            <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Type of mobile phone</label>
                        <input
type="text"
class="form-control"
required
name="mobilephonetype"
placeholder="mobile phone"
>
                    </div>
                    
                    <div class="col">
                        <label for="">Av. weekly phone use</label>
                        <input
type="text"
class="form-control"
name="avweeklyphoneuse"
placeholder="Enter response"
>
                    </div>

                    <div class="col">
                        <label for="">Calls out, number</label>
                        <input
type="number"
class="form-control"
required
name="callsoutnumber"
placeholder="Enter number"
>
                    </div></div> </div> 

                    <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Calls out, minutes</label>
                        <input
type="number"
class="form-control"
required
name="callsoutminutes"
placeholder="Enter minutes"
>
                    </div>
                    
                    <div class="col">
                        <label for="">Calls in, number</label>
                        <input
type="text"
class="form-control"
name="callsinnumber"
placeholder="Enter number"
>
                    </div>

                    <div class="col">
                        <label for="">Call in, minutes</label>
                        <input
type="number"
class="form-control"
required
name="callinminutes"
placeholder="Enter minutes"
>
                    </div></div> </div> 

                    <div class="form-group"><div class="row">
<div class="col">
                        <label for="">SMS sent</label>
                        <input
type="number"
class="form-control"
required
name="SMSsent"
placeholder="Enter number"
>
                    </div>
                    
                    <div class="col">
                        <label for="">Bill payment history</label>
                        <input
type="text"
class="form-control"
name="billpaymenthistory"
placeholder="Enter response"
>
                    </div>

                    <div class="col">
                        <label for="">Data preceding plan switch</label>
                        <input
type="text"
class="form-control"
required
name="dataprecedingplanswitch"
placeholder="Enter megabytes"
>
                    </div></div> </div> 

                    <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Av. weekly data refill</label>
                        <input
type="text"
class="form-control"
required
name="avweeklydatarefill"
placeholder="Enter megabytes"
>
                    </div>
                    
                    <div class="col">
                        <label for="">Number of mobile apps</label>
                        <input
type="number"
class="form-control"
name="noOfmobileapps"
placeholder="Enter number"
>
                    </div>

                    <div class="col">
                        <label for="">Av. time app time spent</label>
                        <input
type="text"
class="form-control"
required
name="avtimespentonapp"
placeholder="Enter minutes"
>
                    </div></div> </div> 

                    <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Kinds of mobile apps</label>
                        <input
type="text"
class="form-control"
required
name="mobileappkinds"
placeholder="Enter mobile apps"
>
                    </div>
                    
                    <div class="col">
                        <label for="">App delete rates</label>
                        <input
type="text"
class="form-control"
required
name="appdeleterate"
placeholder="Enter response"
>
                    </div></div> </div> 
                
                
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
    name: "Character",
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