<template>
  <div>
    
    
    <GChart
      type="ColumnChart"
      :options="options"
      :data="data"
    />    
  </div>
</template>
 
<script>
import { GChart } from "vue-google-charts";
export default {
  name: "App",
  components: {
    GChart
  },
  data() {
    return {
      data: [
         ['Element', 'Density', { role: 'style' }],
         ['Print Media', 9.95, '#6B58E2'],
         ['Social Media', 55.55, '#00B28F'],
         ['Brodcast Media', 52.99, '#F8D12F'],
         ['Outdoor', 30.55, 'color: #e5e4e2' ],
         ['Internet', 45.21, 'color: #4E6973' ]
      ],
      options: {
        width: 1100,
        height: 400
      }
    };
  }
};
</script>