/**
 * Resolves high quality icons/favicons for tools.
 * Priority:
 * 1. GitHub repo owner avatar for GitHub links (crystal clear official logo)
 * 2. Google High-Res Favicon service for website domains
 */
export function getToolIcon(url: string, githubUrl?: string | null): string {
  if (githubUrl && githubUrl.includes("github.com/")) {
    try {
      const clean = githubUrl.replace(/^https?:\/\/(www\.)?github\.com\//, "");
      const owner = clean.split("/")[0];
      if (owner && !owner.startsWith("?")) {
        return `https://github.com/${owner}.png?size=96`;
      }
    } catch {
      // Fall through to domain favicon
    }
  }

  try {
    const parsed = new URL(url);
    const domain = parsed.hostname;
    return `https://www.google.com/s2/favicons?domain=${domain}&sz=128`;
  } catch {
    return "";
  }
}
