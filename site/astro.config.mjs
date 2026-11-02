// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://lordorange.top',
  integrations: [
    sitemap({
      serialize(item) {
        // Explicitly set ISO lastmod timestamp so Google Search Console recognizes recent overhaul
        item.lastmod = new Date();
        
        const url = item.url;
        if (url === 'https://lordorange.top/' || url === 'https://lordorange.top') {
          item.changefreq = 'daily';
          item.priority = 1.0;
        } else if (url.includes('/best/')) {
          item.changefreq = 'weekly';
          item.priority = 0.9;
        } else if (url.includes('/tool/')) {
          item.changefreq = 'weekly';
          item.priority = 0.8;
        } else if (url.includes('/vs/')) {
          item.changefreq = 'monthly';
          item.priority = 0.6;
        } else {
          item.changefreq = 'monthly';
          item.priority = 0.5;
        }
        return item;
      }
    })
  ]
});
