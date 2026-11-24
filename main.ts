// News-image entry for make.fun competition news-image-20261124.
// Node 22, standard library only. Copies the entry.png held in this
// repository to the grader's output directory, deterministically.
//
// Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// The grader runs it with no network; MAKEFUN_OUTPUT_DIR stands in
// for /output outside the grader container.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
const bytes = readFileSync(source);
writeFileSync(target, bytes);
console.log(`wrote ${bytes.length} bytes to ${target}`);
