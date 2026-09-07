"""Unit tests for FastMCP server tools and SSG route introspection."""

from typing import Any

from tools.mcp.server import (
    get_openwiki_concept,
    get_route_content,
    get_sitemap_routes,
    list_ssg_routes,
    search_ssg_routes,
)


def test_list_ssg_routes() -> None:
    """Verifies that list_ssg_routes returns active SSG routes with required metadata fields."""
    routes: list[dict[str, Any]] = list_ssg_routes()
    assert isinstance(routes, list)
    assert len(routes) > 0

    route_slugs = [r["slug"] for r in routes]
    assert "index" in route_slugs
    assert "about" in route_slugs
    assert "lab-manual" in route_slugs

    for r in routes:
        assert "route" in r
        assert "title" in r
        assert "description" in r
        assert "source_file" in r


def test_get_route_content() -> None:
    """Verifies fetching route content for both valid and invalid routes."""
    res_index: dict[str, Any] = get_route_content("index")
    assert res_index["found"] is True
    assert res_index["route"] == "/"
    assert isinstance(res_index["frontmatter"], dict)
    assert len(res_index["body"]) > 0

    res_about: dict[str, Any] = get_route_content("/about")
    assert res_about["found"] is True
    assert res_about["route"] == "/about"

    res_missing: dict[str, Any] = get_route_content("non-existent-route-12345")
    assert res_missing["found"] is False
    assert "error" in res_missing


def test_search_ssg_routes() -> None:
    """Verifies keyword search across SSG routes."""
    results: list[dict[str, Any]] = search_ssg_routes("Astro")
    assert isinstance(results, list)
    assert len(results) > 0

    slugs = [r["slug"] for r in results]
    assert len(slugs) > 0

    empty_results: list[dict[str, Any]] = search_ssg_routes("xyz123nonexistentkeyword")
    assert len(empty_results) == 0


def test_get_sitemap_routes() -> None:
    """Verifies parsing published URLs from sitemap.txt."""
    sitemap_urls: list[str] = get_sitemap_routes()
    assert isinstance(sitemap_urls, list)
    assert len(sitemap_urls) > 0
    assert any("cmsfornerd" in url.lower() for url in sitemap_urls)


def test_get_openwiki_concept() -> None:
    """Verifies querying spatial memory concepts."""
    res: dict[str, Any] = get_openwiki_concept("DSOM")
    assert res["found"] is True
    assert res["matches_count"] > 0
    assert len(res["matches"]) > 0
