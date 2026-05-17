<script setup>
defineProps({
  id: { type: String, required: true },
  title: { type: String, required: true }
})
</script>

<template>
  <section :id="id" class="doc-section">
    <h2 class="section-title">
      <span class="section-marker">§</span>
      {{ title }}
    </h2>
    <slot />
  </section>
</template>

<style scoped>
.doc-section {
  margin: 48px 0;
}

.section-title {
  font-family: var(--vp-font-family-serif);
  font-size: 22px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin: 0 0 20px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--vp-c-divider);
}

.section-marker {
  color: var(--vp-c-gold);
  margin-right: 8px;
}
</style>
