/**
 * NOTE: this code file was automatically migrated to TypeScript using ts-migrate and
 * may contain multiple `any` type annotations and `@ts-expect-error` directives.
 * If possible, please improve types while making changes to this file. If the type
 * annotations are already looking good, please remove this comment.
 */

import { MLFLOW_INTERNAL_PREFIX } from '../../common/utils/TagUtils';

export const NOTE_CONTENT_TAG = MLFLOW_INTERNAL_PREFIX + 'note.content';

export class NoteInfo {
  constructor(content: any) {
    this.content = content;
  }

  static fromTags = (tags: any) => {
    const contentTag = Object.values(tags).find((t) => (t as any).getKey() === NOTE_CONTENT_TAG);
    if (contentTag === undefined) {
      return undefined;
    }
    return new NoteInfo((contentTag as any).getValue());
  };
  content: any;
}
