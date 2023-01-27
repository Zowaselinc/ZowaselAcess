<template>
    <div>
      
      
      <GChart
        type="LineChart"
        :options="options"
        :data="collectionData"
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
        collectionData: [
          ["Day", "Guardians of the Galaxy", "The Avengers", "Transformers"],
          [1,  40.45, 90.5, 42.8],
          [2,  22.5, 68.4, 33.4],
          [3,  36.5, 47, 55.5],
          [4,  12.7, 23.8, 14.5],
          [5,  10.9, 44.5, 10.3],
          [6,   7.8, 14.5,  6.7],
          [7,   8.6, 11.2,  19.6]
        ],
        options: {
          chart: {
            title: "First 7 days movies collection",
            subtitle: "In millions of dollars (USD)"
          },
          width: 1100,
          height: 400
        }
      };
    }
  };
  </script>