const CACHE='mcc-v6';
const ASSETS=['./','./index.html','./assets/css/styles.css','./assets/js/main.js','./assets/img/mark.svg'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS))));
self.addEventListener('fetch',e=>e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request))));
