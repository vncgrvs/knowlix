<template>
  <div>
    <AppHeader v-if="this.$store.state.currentRoute != 'login'" />
    <Nuxt />
  </div>
</template>


<script>
  import AppHeader from "../components/AppHeader";
 
  export default {
    components:{
      AppHeader
      
    }
  };
</script>

