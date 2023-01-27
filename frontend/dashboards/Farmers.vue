<template>
    <DefaultNav>
        <div class="big-container">

            <!--  body -->
            <LineChart />
            <BarChart />
            <BubbleChart />
            <PieChart />
        </div>
    </DefaultNav>
</template>

<script>
import DefaultNav from "@/layouts/DefaultNav.vue";
import BarChart from "@/pages/dashboard/tables/BarChart.vue";
import LineChart from "@/pages/dashboard/tables/LineChart.vue";
import BubbleChart from "@/pages/dashboard/tables/BubbleChart.vue";
import PieChart from "@/pages/dashboard/tables/PieChart.vue";

export default {
    name: "Farmers",
    components: {
        DefaultNav,
        BarChart,
        LineChart,
        BubbleChart,
        PieChart
            },
    data(){
        return {
            
            
        };
    },
    mounted() {
            
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
        padding: 1.1212px 3.3637px;
        background: #FFFFFF;
      // background: #05B050;
      //  color: #FFFFFF;
      // border: 0;

    }

    
}

</style>