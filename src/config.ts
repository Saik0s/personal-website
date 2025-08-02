export const SITE = {
  website: "https://www.igortarasenko.com/", // replace this with your deployed domain
  author: "Igor Tarasenko",
  profile: "https://github.com/Saik0s",
  desc: "Technical blog about iOS development, AI/ML integration, and developer productivity",
  title: "Igor Tarasenko",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: false,
  postPerIndex: 4,
  postPerPage: 4,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true, // show back button in post detail
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "https://github.com/Saik0s/personal-website/edit/main/",
  },
  dynamicOgImage: true,
  dir: "ltr", // "rtl" | "auto"
  lang: "en", // html lang code. Set this empty and default will be "en"
  timezone: "Europe/Warsaw", // Default global timezone (IANA format) https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
} as const;
