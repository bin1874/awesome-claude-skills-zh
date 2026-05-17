<script setup>
defineProps({
  refs: { type: Array, required: true }
})
</script>

<template>
  <sup class="cite">
    <a
      v-for="(ref, i) in refs"
      :key="i"
      :href="`#ref-${ref}`"
      class="cite-link"
    >[{{ ref }}]</a>
  </sup>
</template>

<style scoped>
.cite {
  font-size: 0.75em;
  vertical-align: super;
  margin: 0 1px;
}

.cite-link {
  color: var(--vp-c-accent);
  text-decoration: none;
}

.cite-link:hover {
  text-decoration: underline;
}

.cite-link + .cite-link::before {
  content: ",";
}
</style>
