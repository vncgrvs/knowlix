<template>
  <div class="overflow-hidden">
    <AppHeader v-if="this.$store.state.currentRoute != 'login'" />
    <div
      class=""
      :class="{
        'bg-gray-800 ': this.$store.state.isDropdownVisible,
        'bg-opacity-50': this.$store.state.isDropdownVisible,
        'fixed':this.$store.state.isDropdownVisible,
        'w-full':this.$store.state.isDropdownVisible,
        'h-full':this.$store.state.isDropdownVisible
      }"
    ></div>
    <Nuxt />
  </div>
</template>


<script>
import AppHeader from "../components/AppHeader";

export default {
  components: {
    AppHeader,
  },
};
</script>

