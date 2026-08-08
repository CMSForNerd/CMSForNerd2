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

  return allPages
    .map(page => {
      const cleanId = getCleanSlug(page.id);
      return { ...page, cleanId };
    })
    .filter(page => page.cleanId !== 'index')
    .map(page => {
      // Split on '|' to extract the human-readable display title, e.g. "About | CmsForNerd" -> "About"
      const label = page.data.title.split('|')[0].trim();

      const suffix = isAmp ? '/amp' : '';
      const url = `${base}${page.cleanId}${suffix}`;

      return {
        id: page.cleanId,
        url,
        label
      };
    });
}
