<template>
    <DefaultNav>
        <div class="left-content">

            
                  <h1>5 C's of Credit Scoring</h1> 
            <!-- buttons group -->
            <div class="bntn-group"> 
<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='kyf'"
>
Kyf
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='scorecard'"
>
Scorecard
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='capital'"
>
Capital
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='character'"
>
Character
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='collateral'"
>
Collateral
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='capacity'"
>
Capacity
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='conditions'"
>
Conditions
</button>

            </div>
            <!--  body -->

            <Kyf v-if="activeTab == 'kyf'" />
            <Scorecard v-if="activeTab == 'scorecard'" />
            <Capital v-if="activeTab == 'capital'" />
            <Character v-if="activeTab == 'character'" />
            <Collateral v-if="activeTab == 'collateral'" />
            <Capacity v-if="activeTab == 'capacity'" />
            <Conditions v-if="activeTab == 'conditions'" />

        </div>
    </DefaultNav>
</template>

<script>
import DefaultNav from "@/layouts/DefaultNav.vue";
import Kyf from "@/pages/dashboard/forms/Kyf.vue";
import Scorecard from "@/pages/dashboard/forms/Scorecard.vue";
import Capital from "@/pages/dashboard/forms/Capital.vue";
import Character from "@/pages/dashboard/forms/Character.vue";
import Collateral from "@/pages/dashboard/forms/Collateral.vue";
import Capacity from "@/pages/dashboard/forms/Capacity.vue";
import Conditions from "@/pages/dashboard/forms/Conditions.vue";

export default {
    name: "Farmer",
    components: {
        DefaultNav,
        Kyf,
        Scorecard,
        Capital,
        Character,
        Collateral,
        Capacity,
        Conditions,
    },
    data(){
        return {
            activeTab : 'kyf'
            
        };
    },
    mounted() {
            this.activeTab='kyf';
        },
    methods: {
        
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";

.big-container {
    @include big-container-all;

    h1 {
        @include textStyles(Poppins, 700, 24px, 132%);
        letter-spacing: 0.01em;
        font-feature-settings: 'liga' off;
        color: #4A4754;
    }
}

.bntn-group {
    gap: 11px;

    button.btn-1 {
        @include textStyles(Poppins, 700, 15.5697px, 112%);
        padding: 11.1212px 33.3637px;
        align-items: center;
        background: #FFFFFF;
        border: 1.11212px solid #696671;
        border-radius: 55.6062px;
        letter-spacing: 0.02em;
        font-feature-settings: 'salt' on, 'liga' off;
        color: #696671;
    }

    #kyf-page {
        padding: 11.1212px 33.3637px;
        background: #FFFFFF;
      // background: #05B050;
      //  color: #FFFFFF;
      // border: 0;

    }

}

</style>