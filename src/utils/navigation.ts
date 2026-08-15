import { getCollection } from 'astro:content';

/**
 * Strips file extensions from content collection item IDs to match clean slug structure.
 *
 * @param id The original content ID (e.g. 'index.md', 'about.md')
 * @returns A clean slug (e.g. 'index', 'about')
 */
export function getCleanSlug(id: string): string {
  return id.replace(/\.[^/.]+$/, "");
}

interface NavigationPage {
  id: string;
  url: string;
  label: string;
}

/**
 * Fetches, cleans, and formats navigation-ready page lists for the layouts,
 * avoiding duplicate rendering and manual page ID manipulation in templates.
 *
 * @param base The dynamic BASE_URL prefix (e.g. '/CMSForNerd2/' or '/')
 * @param isAmp Whether to format URL paths for Accelerated Mobile Pages (AMP)
 * @returns A list of cleanly formatted navigation items
 */
export async function getNavigationPages(base: string, isAmp = false): Promise<NavigationPage[]> {
  const allPages = await getCollection('pages');
  const result: NavigationPage[] = [];
  const suffix = isAmp ? '/amp' : '';

  // Single-pass O(N) traversal avoiding redundant array allocations and traversals
  for (let i = 0; i < allPages.length; i++) {
    const page = allPages[i];
    const cleanId = getCleanSlug(page.id);

    if (cleanId !== 'index') {
      // Split on '|' to extract the human-readable display title, e.g. "About | CmsForNerd" -> "About"
      const label = page.data.title.split('|')[0].trim();
      const url = `${base}${cleanId}${suffix}`;

      result.push({
        id: cleanId,
        url,
        label
      });
    }
  }

  return result;
}
