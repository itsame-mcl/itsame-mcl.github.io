// Rendu des diagrammes Mermaid, chargé uniquement sur les pages qui en contiennent.
(() => {
  const nodes = document.querySelectorAll('pre.mermaid')
  if (!nodes.length || !window.mermaid) return
  const dark = window.matchMedia('(prefers-color-scheme: dark)').matches
  window.mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'strict',
    theme: dark ? 'dark' : 'default'
  })
  window.mermaid.run({ nodes })
})()
