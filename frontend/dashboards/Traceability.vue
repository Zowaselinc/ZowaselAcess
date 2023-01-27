<template>
    <DefaultNav>
        <div class="big-container">

            
                  <h1>Traceability</h1> 
            <!-- buttons group -->
            <div class="bntn-group"> 
<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='crop_info'"
>
Crop_info
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='crop_quality'"
>
Crop_quality
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='inputs_info'"
>
Inputs_info
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='warehouse'"
>
Warehouse
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='shipment'"
>
Shipment
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='recommendation'"
>
Recommendation
</button>

            </div>
            <!--  body -->

            <Crop_info v-if="activeTab == 'crop_info'" />
            <Crop_quality v-if="activeTab == 'crop_quality'" />
            <Inputs_info v-if="activeTab == 'inputs_info'" />
            <Warehouse v-if="activeTab == 'warehouse'" />
            <Shipment v-if="activeTab == 'shipment'" />
            <Recommendation v-if="activeTab == 'recommendation'" />

        </div>
    </DefaultNav>
</template>

<script>
import DefaultNav from "@/layouts/DefaultNav.vue";
import Crop_info from "@/pages/dashboard/forms/Crop_info.vue";
import Crop_quality from "@/pages/dashboard/forms/Crop_quality.vue";
import Inputs_info from "@/pages/dashboard/forms/Inputs_info.vue";
import Warehouse from "@/pages/dashboard/forms/Warehouse.vue";
import Shipment from "@/pages/dashboard/forms/Shipment.vue";
import Recommendation from "@/pages/dashboard/forms/Recommendation.vue";

export default {
    name: "Traceability",
    components: {
        DefaultNav,
        Crop_info,
        Crop_quality,
        Inputs_info,
        Warehouse,
        Shipment,
        Recommendation,
    },
    data(){
        return {
            activeTab : 'recommendation'
            
        };
    },
    mounted() {
            this.activeTab='recommendation';
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