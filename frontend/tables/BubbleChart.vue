<template>
    <div>
      
      
      <GChart
        type="BubbleChart"
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
          ['Country', 'Car Sales', 'Brand Marketing', 'State',        'Higher Sales'],
          ['Australia',  90.55,              1.67,     'Canberra',    24628000],
          ['Canada',    85.23,              1.36,      'Ottawa',      64901307],
          ['Denmark',   77.32,              1.84,      'Copenhagen',  6421084],
          ['Egypt',     66.12,              2.78,      'Cairo',       78825112],
          ['Finland',   75.09,              2,         'Helsinki',    11712681],
          ['Greece',    60.21,              1.7,       'Athens',      83137148]
        ],
        options: {
          width: 1100,
          height: 500
        }
      };
    }
  };
  </script>