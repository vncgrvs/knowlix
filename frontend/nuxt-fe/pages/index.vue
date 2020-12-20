<template>
  <div class="w-full h-full sortable bg-gray-100">
    <div class="fixed w-full pt-5">
      <alert
        v-for="(alert, id) in this.$store.state.tasksAlerts"
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
      
      
      var taskID = data.data.kwargs.customID
      var status = data.data.status
      var tList = this.$store.state.taskList
      

      var index = this.findTask(tList, taskID)

      var payload = {
        index: index,
        status: status
      }
        
      
      this.$store.dispatch('updateTask', payload)
      
      
    }.bind(this)
    
    
    
  },
  async created() {
    const res = await this.$axios.$get("/v1/sections").then((response) => {
      this.$store.commit("updateList", response.data);
    });
  },
};
</script>

<style>
</style>
