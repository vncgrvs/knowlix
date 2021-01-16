<template>
  <div class="h-full w-full">
    <div
      class="fixed z-0 w-5/12 pt-3 right-0"
      v-if="this.$store.state.taskAlerts.length != 0"
    >
      <alert
        v-for="(alert, id) in this.$store.state.taskAlerts"
        :key="id"
        :pkey="id"
        :alertID="alert.alertID"
        :alertType="alert.alertType"
        :alertColor="alert.alertColor"
      />
    </div>
    <DownloadItem />
  </div>
</template>

<script>
import DownloadItem from "../../components/DownloadItem";

export default {
  components: {
    DownloadItem,
  },
  middleware: 'auth',
};
</script>

<style>
</style>