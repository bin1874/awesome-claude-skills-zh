<script setup>
defineProps({
  title: { type: String, default: '摘要' },
  keywords: { type: Array, default: () => [] }
})
</script>

<template>
  <div class="abstract-block">
    <div class="abstract-header">
      <span class="abstract-label">{{ title }}</span>
    </div>
    <div class="abstract-content">
      <slot />
    </div>
    <div v-if="keywords.length" class="abstract-keywords">
      <span class="keywords-label">关键词:</span>
      <span v-for="kw in keywords" :key="kw" class="keyword">{{ kw }}</span>
    </div>
  </div>
</template>

<style scoped>
.abstract-block {
  margin: 32px 0;
  padding: 24px;
  background: var(--vp-c-bg-alt);
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
}

.abstract-header {
  margin-bottom: 12px;
}

.abstract-label {
  font-family: var(--vp-font-family-serif);
  font-weight: 600;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--vp-c-accent);
}

.abstract-content {
  font-size: 15px;
  line-height: 1.8;
  color: var(--vp-c-text-2);
}

.abstract-keywords {
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px solid var(--vp-c-divider);
  font-size: 13px;
}

.keywords-label {
  font-weight: 500;
  color: var(--vp-c-text-3);
  margin-right: 8px;
}

.keyword {
  display: inline-block;
  background: var(--vp-c-bg-soft);
  padding: 2px 8px;
  margin: 2px 4px 2px 0;
  border-radius: 3px;
  font-size: 12px;
  color: var(--vp-c-accent);
}
</style>
