<template>
    <DefaultNav>
        <div class="big-container">

            
                  <h1>Sustainability</h1> 
            <!-- buttons group -->
            <div class="bntn-group"> 
<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='living'"
>
Living
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='care'"
>
Care
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='planet'"
>
Planet
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='safety'"
>
Safety
</button>

            </div>
            <!--  body -->

            <Living v-if="activeTab == 'living'" />
            <Care v-if="activeTab == 'care'" />
            <Planet v-if="activeTab == 'planet'" />
            <Safety v-if="activeTab == 'safety'" />
            
        </div>
    </DefaultNav>
</template>

<script>
import DefaultNav from "@/layouts/DefaultNav.vue";
import Living from "@/pages/dashboard/forms/Living.vue";
import Care from "@/pages/dashboard/forms/Care.vue";
import Planet from "@/pages/dashboard/forms/Planet.vue";
import Safety from "@/pages/dashboard/forms/Safety.vue";

export default {
    name: "Sustainability",
    components: {
        DefaultNav,
        Living,
        Care,
        Planet,
        Safety
    },
    data(){
        return {
            activeTab : 'living'
            
        };
    },
    mounted() {
            this.activeTab='living';
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