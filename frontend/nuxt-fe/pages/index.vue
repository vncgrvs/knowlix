<template>
  <div class="w-full h-full sortable bg-gray-100">
    <div class="fixed w-full pt-5">
      <alert
        v-for="(alert, id) in this.$store.state.taskAlerts"
        :key="id"
        :pkey="id"
        :alertID="alert.alertID"
        :alertType="alert.alertType"
      />
    </div>
    <Section />
  </div>
</template>

<script>
import Section from "../components/Section";
import alert from "../components/alert";


export default {
  components: {
    Section,
    alert,
  },
  computed: {},

  methods: {
    findTask: function(taskList, taskID){
      var index = taskList.findIndex(x => x.taskID === taskID)

      return index
    }
  },

  data() {
    return {};
  },
  
  mounted() {
    
    this.ws_success = new WebSocket('ws://localhost:3333/tasks') 
    
    
    this.ws_success.onmessage = function(event){
      var data = JSON.parse(event.data)

      var operationType = data.operation
      
      if(operationType == "insert" || operationType == "replace" || operationType == "delete"){

        this.$store.dispatch('getDownloads')

      }

      
    }.bind(this)
    
    
    
  },
  async created() {
    this.$store.dispatch('getSections')
    this.$store.dispatch('getDownloads')
  },
};
</script>

<style>
</style>
