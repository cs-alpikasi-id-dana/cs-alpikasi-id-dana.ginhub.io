# cs-alpikasi-id-dana.ginhub.io
# Demo Aplikasi - Pengujian Pembelajaran

Ini adalah proyek **Demo Aplikasi** yang dibuat untuk tujuan pembelajaran dan pengujian dalam membuat aplikasi web. Aplikasi ini tidak bertujuan untuk meniru atau menggunakan aplikasi yang sudah ada. Semua kode dan struktur hanya untuk tujuan eksperimen dan pembelajaran.

## Deskripsi

Proyek ini adalah aplikasi web yang dibuat untuk mendemonstrasikan penggunaan berbagai teknologi web seperti HTML, CSS, dan JavaScript dalam pembuatan aplikasi. Ini adalah aplikasi **demo** untuk tujuan belajar membuat aplikasi yang dapat digunakan untuk memahami konsep dasar pengembangan aplikasi web.

## Tujuan

- Menyediakan contoh pembuatan aplikasi demo sederhana.
- Memahami dasar pengembangan aplikasi menggunakan HTML, CSS, dan JavaScript.
- Menguji integrasi dan penggunaan berbagai framework dan alat pengembangan.

## Fitur

- Antarmuka pengguna yang responsif dan sederhana.
- Fungsi dasar seperti **form input**, **tampilan data**, dan **interaksi pengguna**.
- Penggunaan **GitHub Pages** untuk hosting aplikasi secara gratis.

## Teknologi yang Digunakan

- **HTML5**: Untuk struktur dasar halaman.
- **CSS3**: Untuk styling dan desain responsif.
- **JavaScript**: Untuk logika interaktif dan manipulasi DOM.
- **GitHub Pages**: Untuk hosting aplikasi web secara gratis.

## Cara Menjalankan Proyek
https://github.com/username/cs-alpikasi-id-dana.git
==> Service Root Directory "/opt/render/project/src/cs-alpikasi-id-dana" is missing.
Supplementary details
Local interpretation
local interpretation
# https://github.com/NetManAIOps/DejaVu/blob/master/figures/local_interpretation.png
Since the DejaVu model is trained with historical failures, it is straightforward to interpret how it diagnoses a given failure by figuring out from which historical failures it learns to localize the root causes. Therefore, we propose a pairwise failure similarity function based on the aggregated features extracted by the DejaVu model. Compared with raw metrics, the extracted features are of much lower dimension and contain little useless information, which the DejaVu model ignores. However, computing failure similarity is not trivial due to the generalizability of DejaVu. For example, suppose that the features are 
1
 for root-cause failure units and 
0
 for other failure units and there are four failure units (
𝑣
1
, 
𝑣
2
, 
𝑣
3
, 
𝑣
4
). Then for two similar failures which occur at 
𝑣
1
 and 
𝑣
2
 respectively, their feature vectors are 
(
1
,
0
,
0
,
0
)
 and 
(
0
,
1
,
0
,
0
)
 respectively, which are dissimilar with respect to common similarity metrics (e.g., Manhattan or Euclidean).

To solve this problem, we calculate similarities based on failure classes rather than single failure units. As shown in \cref{fig:local-interpretation}, for each failure units at an in-coming failure 
𝑇
1
, we compare it with each unit of the corresponding failure classes at a historical failure 
𝑇
2
 and take the minimal similarity as its similarity to 
𝑇
2
. Then, we average the similarities to T2 if all units with their suspicious scores (of 
𝑇
1
) as the weights. It is because we only care about those failure units that matter in the current failure when finding similar historical failures. In summary, the similarity function to compare 
𝑇
1
 and 
𝑇
2
 can be formalized as follows: $$ d(T_1, T_2)=\frac{1}{|V|}\sum_{v\in V}s_{T_1}(v)(\min_{v' \in N_c(v;G)}||\boldsymbol{\hat{f}}^{(T_1, v)}-\boldsymbol{\hat{f}}^{(T_2, v')}||_1) $$ where 
𝑁
𝑐
(
𝑣
;
𝐺
)
 denotes the failure units of the same class as 
𝑣
 in 
𝐺
, and 
|
|
⋅
|
|
1
 denotes 
𝐿
1
 norm.

For an in-coming failure, we calculate its similarity to each historical failure and recommend the top-k most similar ones to engineers. Our model is believed to learn localizing the root causes from these similar historical failures. Furthermore, engineers can also directly refer to the failure tickets of these historical failures for their diagnosis and mitigation process. Note that sometimes the most similar historical failures may have different failure classes to the localization results due to imperfect similarity calculation. In such cases, we discard and ignore such historical failures.

Global interpretation
The selected time-series features are listed as follows:
# https://github.com/NetManAIOps/DejaVu/blob/master/figures/global_interpretation_time_series_features.png
