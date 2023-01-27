<template>
    <div>
      
      <GChart
        type="PieChart"
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
            ['Daily Routine', 'Hours per Day'],
            ['Work',     14],
            ['Eat',      1],
            ['Reading',  2],
            ['Exercise', 2],
            ['Sleep',    5]
        ],
        options: {
          width: 1100,
          height: 400
        }
      };
    }
  };
  </script>