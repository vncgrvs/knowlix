<template>
  <div class="flex justify-center pt-10 font-lix w-full antialiased">
    <div class="block w-8/12">
      <p
        class="text-4xl font-bold text-gray-700 justify-center flex border-solid border-b-2 border-lix-third"
      >
        Available Onboarding Decks
      </p>

      <div class="flex flex-col mt-4 " id="tableDownloads">
        <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div
            class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8"
          >
            <div
              class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg"
            >
              <table class="min-w-full divide-y divide-gray-200" id="downloads">
                <thead class="bg-gray-50 font-extrabold">
                  <tr class="">
                    <th
                      scope="col"
                      class="px-3 py-3 text-left w-2/12 text-xs  font-bold text-gray-500 uppercase tracking-wider outline-none"
                    >
                      <div class="flex">
                        <p class="pr-8">Task ID</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update right"
                          @click="sort(0)"
                        >
                          <path
                            d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"
                          />
                        </svg>
                      </div>
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3 text-left text-xs font-bold text-gray-500 uppercase outline-none tracking-wider"
                    >
                      <div class="flex">
                        <p class="w-11/12">Sections</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
                          @click="sort(1)"
                        >
                          <path
                            d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"
                          />
                        </svg>
                      </div>
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3 text-left text-xs font-bold text-gray-500 uppercase outline-none tracking-wider"
                    >
                      <div class="flex">
                        <p class="pr-5">Status</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
                          @click="sort(2)"
                        >
                          <path
                            d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"
                          />
                        </svg>
                      </div>
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3 text-left text-xs font-bold text-gray-500 uppercase outline-none tracking-wider"
                    >
                      <div class="flex">
                        <p class="w-10/12">created</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
                          @click="sort(3)"
                        >
                          <path
                            d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z"
                          />
                        </svg>
                      </div>
                    </th>
                    <th scope="col" class="relative px-6 py-3">
                      <span class="sr-only">Edit</span>
                    </th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr
                    v-for="(task, index) in this.$store.state.taskList"
                    :key="index"
                  >
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center justify-center">
                        <div class="">
                          <div class="text-lg font-bold text-gray-900">
                            {{ index + 1 }}
                          </div>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900"></div>
                      <div class="text-sm text-gray-500">
                        <p v-for="section in task.sections" :key="section.id">
                          {{ section }}
                        </p>
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-800"
                        v-if="task.status === 'STARTED'"
                      >
                        started
                      </span>
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"
                        v-if="task.status === 'SUCCESS'"
                      >
                        done
                      </span>
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"
                        v-if="task.status === 'FAILURE'"
                      >
                        failed
                      </span>
                    </td>
                    <td
                      class="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
                    >
                      {{ task.created }}
                    </td>
                    <td
                      class="px-6 py-4 whitespace-nowrap  flex justify-center items-center h-full"
                    >
                      <a
                        class=" hover:text-white hover:bg-lix-main hover:font-bold text-xs font-bold cursor-pointer inline-flex align-middle rounded-full bg-gray-400 text-white py-1 px-2 "
                        v-if="task.status == 'SUCCESS' && task.downloading == false"
                        @click="getDownload(task.taskID)"
                        >Download</a
                      >
                      
                      <svg
                        class="animate-spin -ml-1 mr-3 h-5 w-5 text-lix flex items-center"
                        v-if="task.downloading == true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                      >
                        <circle
                          class="opacity-25"
                          cx="12"
                          cy="12"
                          r="10"
                          stroke="currentColor"
                          stroke-width="4"
                        ></circle>
                        <path
                          class="opacity-75"
                          fill="currentColor"
                          d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                        ></path>
                      </svg>
                    </td>
                  </tr>

                  <!-- More rows... -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DownloadItem",

  methods: {
    sort: function (id) {
      var table = this.table;

      table.order.listener("#update", id);
    },
    getDownload: function (taskID) {
      this.$store.dispatch("downloadPresentation", taskID);
    },
  },
  created() {
    if (process.browser) {
      this.$store.commit("initialiseStore");
    }
  },
  mounted() {
    var table = $("#downloads").DataTable({
      responsive: false,
      paging: false,
      info: false,
      searching: false,
      keys: false,
    });

    this.table = table;

    // $("th").off();
    $("th").removeAttr("style");

    // $('.dataTables_empty').remove();
  },
};
</script>

<style>
</style>