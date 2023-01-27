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
CAPITAL
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
                            <label for="">What is the main source of income?</label>
                            <input
type="text"
class="form-control"
required
name="mainincomesource"
placeholder="Enter main source of income"
>
                        </div></div></div>

                        <div class="form-group">

                    <label for="">What are your sources of income other than farming</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="otherincomesource"
required
placeholder="Enter other sources of income"
>
                </div>

                <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What is your first option for getting the necessary money?</label>
                            <input
type="text"
class="form-control"
required
name="firstfundingoption"
placeholder="Enter first funding option"
>
                        </div>
                    
                        <div class="col">
                            <label for="">What is the number of people providing regular income to the household?</label>
                            <input
type="number"
class="form-control"
required
name="noofincomeearners"
placeholder="Enter no of income earners"
>
                        </div></div></div>



                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">Do you have an account with any commercial bank?</label>
                            <select
class="form-control"
name="hasbankaccount"
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
                            <label for="">Would you prefer to find money or need a loan?</label>
                            <select
class="form-control"
name="needsaloan"
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
                            <label for="">How many months would you need to pay back?</label>
                            <input
type="number"
class="form-control"
required
name="paybackmonths"
placeholder="Enter Pay Back Months"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Did the quantity of your harvest change?</label>
                            <select
class="form-control"
name="harvestqtychanged"
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
                            <label for="">Did your expense in pest control change?</label>
                            <select
class="form-control"
name="pestexpensechanged"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="Increased">
                            Increased
</option>
                        <option value="Same">
                            Same
</option>
                        <option value="Decreased">
                            Decreased
</option>
                        
                        
                    </select>
                        </div></div></div>


                        <br>  <h2 class="text-center">
CREDIT ACCESS
</h2> <br>



            <div class="form-group">
                    <label for="">Have you served as a treasurer in your farmer group or any other group in the past or presently? Specify group please</label>
                    <input
id="formGroupExampleInput"
type="text"
class="form-control"
name="hasservedastreasurer"
required
placeholder="Enter your answer"
>
                </div>



                <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">If yes, how many months have served in this capacity?</label>
                            <input
type="number"
class="form-control"
name="durationastreasurer"
placeholder="Enter Duration as Treasurer"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Do you do saving in your farmer group monthly?</label>
                            <select
class="form-control"
name="savesmoneymonthly"
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
                            <label for="">If yes, how much do you set aside monthly?</label>
                            <input
type="number"
class="form-control"
name="savingsamount"
placeholder="Enter monthly savings"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Have you had difficulty to pay up loans on time in the past 4 years?</label>
                            <select
class="form-control"
name="haddifficultyrepaying"
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
                            <label for="">If yes, how much </label>
                            <input
type="number"
class="form-control"
name="difficultloanamount"
placeholder="Enter amount"
>
                        </div>
                    
                        <div class="col">
                            <label for="">If yes, why?</label>
                            <input
type="text"
class="form-control"
name="difficultyreason"
placeholder="Enter reason"
>
                        </div></div></div>


                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">How many loans have you had difficulty to pay back in the past 4 years?</label>
                            <input
type="number"
class="form-control"
name="noofdifficultloans"
placeholder="Enter number"
>
                        </div>
                    
                        <div class="col">
                            <label for="">How many loans have you have you paid back in the past 4 years?</label>
                            <input
type="number"
class="form-control"
name="noofrepaidloans"
placeholder="Enter number"
>
                        </div></div></div>

                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">How many have you paid on or before due date?</label>
                            <input
type="number"
class="form-control"
name="noofloansontime"
placeholder="Enter number"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Estimate monthly income after harvest & sales of your farm produce?</label>
                            <input
type="number"
class="form-control"
name="estmonthlyincome"
placeholder="Enter monthly income"
>
                        </div></div></div>


                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">What is your cost of cultivation in this planting season?</label>
                            <input
type="number"
class="form-control"
name="costofcultivation"
placeholder="Enter amount"
>
                        </div>
                    
                        <div class="col">
                            <label for="">Have you exchanged your farm produce to pay up for loans in the past?</label>
                            <select
class="form-control"
name="farmproduceexchanged"
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
                            <label for="">If yes, how many times have you exchanged in the past 4 years?</label>
                            <input
type="number"
class="form-control"
name="nooftimesexchanged"
placeholder="Enter number"
>
                        </div>

                        <div class="col">

                            <label for="">If no, what other collateral do you use or loans in the past 4 years?</label>
                            <input
type="text"
class="form-control"
name="collateral"
placeholder="Enter collateral"
>
                            
                        </div></div></div>


                        <div class="form-group"><div class="row ">
                        
                        <div class="col">
                            <label for="">How much do you want for a loan?</label>
                            <input
type="number"
class="form-control"
required
name="applyloanamount"
placeholder="Enter amount"
>
                        </div>
                    
                        <div class="col">
                            <label for="">How many years have you being cultivating for?</label>
                            <select
class="form-control"
name="yearsofcultivating"
required
>
                        <option value="">
                            click to select
</option>
                        <option value="1-5">
                            1-5
</option>
                        <option value="6-10">
                            6-10
</option>                 <option value="11-20">
                            11-20
</option>                    <option value="21-30">
                            21-30
</option>                 <option value="31-40">
                            31-40
</option>                 <option value="41-Above">
                            41-Above
</option>                 
                    </select>
                        </div>
                    
                        <div class="col">
                            <label for="">What is your turnover for a year?</label>
                            <input
type="number"
class="form-control"
required
name="annualturnover"
placeholder="Enter amount"
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
//import OptionList from './components/OptionList.vue';
import AuthSharedLayout from "@/layouts/shared/AuthSharedLayout.vue";
export default {
    name: "Capital",
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