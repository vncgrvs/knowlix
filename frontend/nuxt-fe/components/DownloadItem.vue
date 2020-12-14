<template>
  <div class="flex justify-center pt-10 font-lix w-full antialiased">
    <div class="block w-7/12">
      <p
        class="text-4xl font-bold text-gray-700 justify-center flex border-solid border-b-2 border-lix-third"
      >
        Available Onboarding Decks
      </p>

      <div class="flex flex-col mt-4" id="tableDownloads">
        <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div
            class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8"
          >
            <div
              class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg"
            >
              <table class="min-w-full divide-y divide-gray-200" id="downloads">
                <thead class="bg-gray-50">
                  <tr class="">
                    <th
                      scope="col"
                      class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider outline-none"
                    >
                      <div class="flex">
                        <p class="w-11/12">Task ID</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
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
                      class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase outline-none tracking-wider"
                    >
                      <div class="flex">
                        <p class="w-11/12">Sections</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
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
                      class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase outline-none tracking-wider"
                    >
                      <div class="flex">
                        <p class="w-11/12">Status</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
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
                      class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase outline-none tracking-wider"
                    >
                      <div class="flex">
                        <p class="w-11/12">created</p>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          class="w-5 h-5 cursor-pointer update"
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
                  <tr v-for="task in this.$store.state.taskList" :key="task.id">
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="">
                          <div class="text-sm font-medium text-gray-900">
                            {{ task.taskID }}
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
                        v-if="task.status === 'started'"
                        
                      >
                        {{ task.status }}
                      </span>
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"
                        v-if="task.status === 'done'"
                        
                      >
                        {{ task.status }}
                      </span>
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"
                        v-if="task.status === 'failed'"
                        
                      >
                        {{ task.status }}
                      </span>
                    </td>
                    <td
                      class="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
                    >
                      {{ task.created }}
                    </td>
                    <td
                      class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                    >
                      <a href="#" class="text-indigo-600 hover:text-indigo-900"
                        >Download</a
                      >
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
  },
};
</script>

<style>
</style>