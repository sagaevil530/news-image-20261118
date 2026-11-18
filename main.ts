// News image entry for make.fun competition news-image-20261118.
// The image (entry.png) is a newspaper-style summary of the world news of
// Wednesday 18 November 2026, composed in this repository. This program
// copies it to the grader's output directory. Node 22, standard library only.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const source = new URL('./entry.png', import.meta.url);
if (!existsSync(source)) {
  throw new Error('entry.png is missing from the repository');
}
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? join(dirname(fileURLToPath(import.meta.url)), 'out');
mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, 'entry.png'));
