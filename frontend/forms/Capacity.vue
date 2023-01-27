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
CAPACITY
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
                            <label for="">How long have you been farming?</label>
                            <input
type="text"
class="form-control"
required
name="howlongbeenfarming"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">Have you participated in any agricultural training?</label>
                            <select
class="form-control"
name="participatedintraining"
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
                            <label for="">What type of farming do you practice?</label>
                            <input
type="text"
class="form-control"
required
name="farmingpractice"
placeholder="Enter farming practice"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">Apart from crops do you keep animals?</label>
                            <select
class="form-control"
name="keepsanimals"
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
                            <label for="">Are you a member of any group (farmers’ cooperative)?</label>
                            <select
class="form-control"
name="hascooperative"
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
                            <label for="">If yes, name of the group</label>
                            <input
type="text"
class="form-control"
name="cooperativename"
placeholder="Enter response"
>
                        </div>

                        <div class="col">
                            <label for="">Educational level of the farmer</label>
                            <input
type="text"
class="form-control"
required
name="educationlevel"
placeholder="Enter response"
>
                        </div></div></div>





                        <br><h2 class="text-center">
FARMING PRACTICE
</h2> <br>

            <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">What is the size of your farm?</label>
                            <input
type="text"
class="form-control"
required
name="SizeOfFarm"
placeholder="Enter farm size"
>
                        </div>

                        <div class="col">
                            <label for="">The farmland you are cultivating is it rented or leased</label>
                            <input
type="text"
class="form-control"
required
name="farmisrentedorleased"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">If rented or lease for how many years?</label>
                            <input
type="text"
class="form-control"
required
name="noofyearsleased"
placeholder="Enter years"
>
                        </div>

                        <div class="col">
                            <label for="">Do you use machines (tractor, harvester, planter) on your farm?</label>
                            <input
type="text"
class="form-control"
required
name="usesmachines"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">Do you rotate crops?</label>
                            <input
type="text"
class="form-control"
required
name="rotatescrops"
placeholder="Enter response"
>
                        </div>

                        <div class="col">
                            <label for="">How many hectares can you cultivate/produce each year?</label>
                            <input
type="text"
class="form-control"
required
name="noOfhectaresproducedyearly"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">How many times of fertilizer applications are in one cropping cycle?</label>
                            <input
type="text"
class="form-control"
required
name="nooffertlizerapplications"
placeholder="Enter response"
>
                        </div>

                        <div class="col">
                            <label for="">What is the approximate fertilizer use?</label>
                            <input
type="text"
class="form-control"
required
name="approxfertilizeruse"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">How the decision for spraying is made for pest/disease?</label>
                            <input
type="text"
class="form-control"
required
name="decisionforspraying"
placeholder="Enter response"
>
                        </div>

                        <div class="col">
                            <label for="">What method of weed control do you practice?</label>
                            <input
type="text"
class="form-control"
required
name="weedcontrolpractice"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        <div class="col">
                            <label for="">What is your estimated income per crop in harvest per season?</label>
                            <input
type="text"
class="form-control"
required
name="estimatedincomepercrop"
placeholder="Enter amount"
>
                        </div>

                        <div class="col">
                            <label for="">Which crop can be well sold if production increases?</label>
                            <input
type="text"
class="form-control"
required
name="cropthatcansellwell"
placeholder="Enter response"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">               
                        

                        <div class="col">
                            <label for="">Do you have a plan or a project for your farm?</label>
                            <input
type="text"
class="form-control"
required
name="hasfarmplanorproject"
placeholder="Enter response"
>
                        </div>
                    
                        <div class="col">
                            <label for="">If yes, which project</label>
                            <input
type="text"
class="form-control"
required
name="FarmProjectInfo"
placeholder="Enter response"
>
                        </div></div></div>


                        <br><h2 class="text-center">
MECHANIZATION
</h2> <br>

            <div class="form-group">
                    <label for="">Which machines are you using on your farm land</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="machinesused"
required
placeholder="List machines"
>
                </div>

                <div class="form-group">
                    <label for="">Has the machine been of advantage to you this planting season compared to last season?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="machinehashelped"
required
placeholder="Enter response"
>
                </div>

                <div class="form-group">
                    <label for="">Would you advise other farmers to use machines instead of hired labour?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="advisemachineorlabour"
required
placeholder="Enter advise"
>
                </div>

                <div class="form-group">
                    <label for="">What other machines would you find needful apart from the ones you have access to presently?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="othermachinesneeded"
required
placeholder="Enter response"
>
                </div>

                <div class="form-group">
                    <label for="">With the use of machines are you encouraged to acquire more farm lands for farming?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="canacquiremorelands"
required
placeholder="Enter response"
>
                </div>

                <div class="form-group">
                    <label for="">What is the percentage of cost saved from labour with the use of machine?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="percentcostsaved"
required
placeholder="Enter response"
>
                </div>






                <br><h2 class="text-center">
CULTIVATION
</h2> <br>

            <div class="form-group"><div class="row">
<div class="col">
                        <label for="">Do you have permanent, temporary or seasonal labor?</label>
                        <select
class="form-control"
name="type_of_labor"
required
>
                        <option value="">
click to select
</option>
                        <option value="permanent">
                            permanent
</option>
                        <option value="temporary">
                            temporary
</option>               
                        <option value="seasonal">
                            seasonal
</option>
                        
                    </select>
                    </div>
                    
                    <div class="col">
                        <label for="">Which do you pay for or hire as labor?</label>
                        <input
type="text"
class="form-control"
required
name="pay_for_labor"
placeholder="Enter response"
>
                    </div></div> </div>

                    <div class="form-group"><div class="row">
<div class="col">
                        <label for="">If you use household labor, how many children do help you on your farm?</label>
                        <input
type="number"
class="form-control"
required
name="how_many_housechildren_help"
placeholder="Enter number"
>
                    </div>
                    
                    <div class="col">
                        <label for="">What season do children help in the farm?</label>
                        <input
type="text"
class="form-control"
required
name="season_children_help"
placeholder="Enter response"
>
                    </div></div> </div> 

                    <div class="form-group">
                    <label for="">What do they do?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="labor_children_do"
required
placeholder="Enter details"
>
                </div>

                <div class="form-group">
                    <label for="">What is the equivalent cost of household labor compared to hire labor?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="household_vs_hire_cost"
required
placeholder="Enter response"
>
                </div>

                <div class="form-group">
                    <label for="">What do women do in the farm?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="labor_women_do"
required
placeholder="Enter details"
>
                </div>

                <div class="form-group">
                    <label for="">What is the percentage of Female hire labor with Male?</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="percent_female_hired"
required
placeholder="Enter response"
>
                </div>

                <br><h2 class="text-center">
HARVEST
</h2> <br>
            <div class="form-group">
                    <label for="">When is harvest season for your crop? </label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="when_is_harvest_season"
required
placeholder="Enter response"
>
                </div>

                <div class="form-group"><div class="row">
<div class="col">
                        <label for="">How many people do harvesting on your farm? (Hired - ) </label>
                        <input
type="number"
class="form-control"
required
name="no_of_hired_workers"
placeholder="Enter number"
>
                    </div>
                    
                    <div class="col">
                        <label for="">How many people do harvesting on your farm? (Family - ) </label>
                        <input
type="number"
class="form-control"
required
name="no_of_family_workers"
placeholder="Enter number"
>
                    </div></div> </div> 

                    <div class="form-group"><div class="row">
<div class="col">
                        <label for="">How many people do harvesting on your farm? (Permanent labour - )</label>
                        <input
type="number"
class="form-control"
required
name="no_of_permanent_workers"
placeholder="Enter number"
>
                    </div>
                    
                    <div class="col">
                        <label for="">How many hired labour have you worked with during the year constantly?</label>
                        <input
type="number"
class="form-control"
name="no_hired_constantly"
placeholder="Enter number"
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
    name: "Capacity",
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