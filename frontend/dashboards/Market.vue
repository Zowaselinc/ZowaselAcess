<template>
    <DefaultNav>
        <div class="big-container">

            
                  <h1>Market</h1> 
            <!-- buttons group -->
            <div class="bntn-group"> 
<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='crop_card'"
>
Cropcard
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='market_price'"
>
Marketprice
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='buyers_offers'"
>
Buyers Offers
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='farmgate_prices'"
>
Farmgate Prices
</button>

<button
id="kyf-page"
type="button"
class="btn btn-1"
@click="activeTab='buyers_daily_prices'"
>
Buyers Daily Prices
</button>

            </div>
            <!--  body -->

            <Market_price v-if="activeTab == 'market_price'" />
            <Crop_card v-if="activeTab == 'crop_card'" />
            <Buyers_offers v-if="activeTab == 'buyers_offers'" />
            <Farmgate_prices v-if="activeTab == 'farmgate_prices'" />
            <Buyers_daily_prices v-if="activeTab == 'buyers_daily_prices'" />
        </div>
    </DefaultNav>
</template>

<script>
import DefaultNav from "@/layouts/DefaultNav.vue";
import Market_price from "@/pages/dashboard/forms/Market_price.vue";
import Crop_card from "@/pages/dashboard/forms/Crop_card.vue";
import Buyers_offers from "@/pages/dashboard/forms/Buyers_offers.vue";
import Farmgate_prices from "@/pages/dashboard/forms/Farmgate_prices.vue";
import Buyers_daily_prices from "@/pages/dashboard/forms/Buyers_daily_prices.vue";

export default {
    name: "Market",
    components: {
        DefaultNav,
        Market_price,
        Crop_card,
        Buyers_offers,
        Farmgate_prices,
        Buyers_daily_prices
    },
    data(){
        return {
            activeTab : 'market_price'
            
        };
    },
    mounted() {
            this.activeTab='market_price';
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