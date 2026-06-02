declare module "@pagefind/default-ui" {
  export interface PagefindUIOptions {
    element: string;
    showSubResults?: boolean;
    showImages?: boolean;
    processTerm?: (term: string) => string;
  }

  export class PagefindUI {
    constructor(options: PagefindUIOptions);
    triggerSearch(term: string): void;
  }
}
