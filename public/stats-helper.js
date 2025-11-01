// Enhanced tracking for user interactions
(function() {
    'use strict';

    // Make sure stats (plausible) is available
    window.stats = window.stats || function() { (window.stats.q = window.stats.q || []).push(arguments) };

    function getLinkEl(link) {
        while (link && (typeof link.tagName === 'undefined' || link.tagName.toLowerCase() !== 'a' || !link.href)) {
            link = link.parentNode;
        }
        return link;
    }

    function shouldFollowLink(event, link) {
        // If default has been prevented by an external script, don't intercept navigation
        if (event.defaultPrevented) { return false; }

        var targetsCurrentWindow = !link.target || link.target.match(/^_(self|parent|top)$/i);
        var isRegularClick = !(event.ctrlKey || event.metaKey || event.shiftKey) && event.type === 'click';
        return targetsCurrentWindow && isRegularClick;
    }

    function getDatasetTracking(link) {
        if (!link.dataset) { return null; }

        var eventName = link.dataset.statsEvent;
        if (!eventName) { return null; }

        var category = link.dataset.statsCategory || "custom";
        var props = {};

        if (link.dataset.statsProps) {
            try {
                props = JSON.parse(link.dataset.statsProps);
            } catch (error) {
                console.warn("Could not parse data-stats-props JSON", error);
            }
        }

        return { eventName: eventName, category: category, props: props };
    }

    function getSpecificButtonTracking(link) {
        var href = link.href;
        var linkText = link.textContent.trim();
        var className = link.className || '';
        var parentText = link.parentElement ? link.parentElement.textContent.trim() : '';
        
        // Pick My Brain buttons
        if (href.includes('cal.com/tarasenko')) {
            if (href.includes('/30min')) {
                return { eventName: 'Button Click: Pick My Brain 30min', category: 'consultation' };
            }
            if (href.includes('/60min')) {
                if (className.includes('pushable') || parentText.includes('Pick My Brain')) {
                    return { eventName: 'Button Click: Pick My Brain 60min - Home', category: 'consultation' };
                }
                return { eventName: 'Button Click: Pick My Brain 60min - About', category: 'consultation' };
            }
        }

        // Codementor button
        if (href.includes('codementor.io')) {
            return { eventName: 'Button Click: Codementor Session', category: 'consultation' };
        }

        // Social media specific tracking
        if (href.includes('github.com/Saik0s')) {
            return { eventName: 'Social Click: GitHub', category: 'social' };
        }
        if (href.includes('x.com/sa1k0s') || href.includes('twitter.com/sa1k0s')) {
            return { eventName: 'Social Click: X/Twitter', category: 'social' };
        }
        if (href.includes('buymeacoffee.com/saik0s')) {
            return { eventName: 'Social Click: Buy Me Coffee', category: 'social' };
        }
        if (href.includes('linkedin.com')) {
            return { eventName: 'Social Click: LinkedIn', category: 'social' };
        }

        // Social sharing buttons
        if (href.includes('wa.me') || href.includes('whatsapp')) {
            return { eventName: 'Share Click: WhatsApp', category: 'sharing' };
        }
        if (href.includes('facebook.com/sharer')) {
            return { eventName: 'Share Click: Facebook', category: 'sharing' };
        }
        if (href.includes('x.com/intent/post') || href.includes('twitter.com/intent')) {
            return { eventName: 'Share Click: X/Twitter Share', category: 'sharing' };
        }
        if (href.includes('t.me/share')) {
            return { eventName: 'Share Click: Telegram', category: 'sharing' };
        }
        if (href.includes('pinterest.com/pin')) {
            return { eventName: 'Share Click: Pinterest', category: 'sharing' };
        }
        if (href.includes('mailto:')) {
            return { eventName: 'Share Click: Email', category: 'sharing' };
        }

        return null;
    }

    function categorizeLink(link) {
        var href = link.href;
        var hostname = link.hostname;
        var currentHostname = window.location.hostname;
        
        // Highest priority: explicit data attributes
        var datasetTracking = getDatasetTracking(link);
        if (datasetTracking) {
            return datasetTracking;
        }

        // First check for specific button tracking
        var specificTracking = getSpecificButtonTracking(link);
        if (specificTracking) {
            return specificTracking;
        }
        
        // Internal links (same domain)
        if (hostname === currentHostname) {
            // Blog post links
            if (href.includes('/posts/') || href.includes('/blog/')) {
                return { eventName: 'Link Click: Internal - Blog Post', category: 'internal' };
            }
            // Navigation links
            if (href.includes('/about') || href.includes('/contact') || href.includes('/projects') || href.includes('/tags')) {
                return { eventName: 'Link Click: Internal - Navigation', category: 'internal' };
            }
            // Other internal links
            return { eventName: 'Link Click: Internal - Other', category: 'internal' };
        }
        
        // External links (catch-all for non-specific external links)
        else {
            // Documentation/reference links
            if (hostname.includes('docs.') || hostname.includes('developer.') || 
                hostname.includes('reference.') || hostname.includes('api.') ||
                hostname.includes('stackoverflow.com') || hostname.includes('github.io') ||
                hostname.includes('mozilla.org') || hostname.includes('w3.org')) {
                return { eventName: 'Link Click: External - Documentation', category: 'external' };
            }
            // Other external links
            return { eventName: 'Link Click: External - Other', category: 'external' };
        }
    }

    var MIDDLE_MOUSE_BUTTON = 1;

    function handleLinkClick(event) {
        if (event.type === 'auxclick' && event.button !== MIDDLE_MOUSE_BUTTON) { return; }

        var link = getLinkEl(event.target);

        if (link && shouldTrackLink(link)) {
            var linkInfo = categorizeLink(link);
            if (!linkInfo) { return; }
            
            var eventProps = { 
                url: link.href,
                text: link.textContent.trim().substring(0, 100), // First 100 chars of link text
                domain: link.hostname,
                path: link.pathname,
                page: window.location.pathname
            };

            if (linkInfo.props) {
                for (var key in linkInfo.props) {
                    if (Object.prototype.hasOwnProperty.call(linkInfo.props, key)) {
                        eventProps[key] = linkInfo.props[key];
                    }
                }
            }
            
            return sendLinkClickEvent(event, link, linkInfo.eventName, eventProps);
        }
    }

    function sendLinkClickEvent(event, link, eventName, eventProps) {
        var followedLink = false;

        function followLink() {
            if (!followedLink) {
                followedLink = true;
                window.location = link.href;
            }
        }

        if (shouldFollowLink(event, link)) {
            stats(eventName, { props: eventProps, callback: followLink });
            setTimeout(followLink, 5000);
            event.preventDefault();
        } else {
            stats(eventName, { props: eventProps });
        }
    }

    function shouldTrackLink(link) {
        // Skip tracking for:
        // - Links with no href
        // - Hash links to same page
        // - Download links (handled by Plausible separately)
        var href = link.href;
        
        if (!href) return false;
        if (href.startsWith('#') || href === window.location.href + '#') return false;
        
        // Skip common file downloads (these might be handled by Plausible's built-in tracking)
        var fileExtensions = /\.(pdf|doc|docx|xls|xlsx|ppt|pptx|zip|rar|tar|gz|mp3|mp4|avi|mov|wmv|flv|swf)$/i;
        if (fileExtensions.test(href)) return false;
        
        return true;
    }

    // Add event listeners when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            document.addEventListener('click', handleLinkClick);
            document.addEventListener('auxclick', handleLinkClick);
        });
    } else {
        document.addEventListener('click', handleLinkClick);
        document.addEventListener('auxclick', handleLinkClick);
    }
})();
