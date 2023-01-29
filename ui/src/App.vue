<template>
  <div>
      <h1 v-for="e in examples" :key="e.id">
        {{ e.id }} - {{ e.example }}
      </h1>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    const examples = ref([])

    const load = async () => {
      const response = await fetch("/things", {
        method: "GET"
      })
      examples.value = await response.json()
    }

    load()

    return { examples }
  }
}
</script>
