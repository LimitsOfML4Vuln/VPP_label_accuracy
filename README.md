# VPP Label Accuracy Analysis

We carried out a label accuracy analysis of 100 functions randomly sampled from VulnPatchPairs, that were labelled as 'vulnerable' by the Devign authors. The results are displayed in this repository.

## How to view the results

[load_results.py](https://github.com/LimitsOfML4Vuln/VPP_LABEL_ACCURACY/blob/main/load_results.py) is a script that loads and displays the results stored in [label_accuracy_analysis.json](https://github.com/LimitsOfML4Vuln/VPP_LABEL_ACCURACY/blob/main/label_accuracy_analysis.json). We used Python 3.9.16 and Pandas 1.5.1.

## General Information

```
.
├── label_accuracy_analysis.json... Results of the label accuracy analysis.
├── load_results.py................ Script that loads the results.
└── README.md
```

## Structure

Below is an annotated map of the JSON structure of label_accuracy_analysis.json.

```
.
├── project........................ Source project (either Qemu or Ffmpeg).
├── patch_commit_id................ Commit ID of the patch.
├── label.......................... Label that we assigned during the label accuracy analysis (0, 1 or 2).
├── type........................... Vulnerability type that we assigned during the label accuracy analysis.
└── vulnerable_func................ The function.
```

## Labelling Criteria and Process

We adopted our labeling criteria based on the [supplementary materials](https://sites.google.com/view/devign) provided by the Devign authors, categorizing all potential denial of service issues, such as "buffer overflow, memory leak, crash, and corruption," as vulnerabilities. This was our process:

1. We randomly sampled 100 functions from VulnPatchPairs that were labeled as 'vulnerable' by the Devign authors.
2. For each function, we did the following:
3. We opened the corresponding patch commit on GitHub.
4. We verified that the function was actually modified in the patch commit. If not, we assigned the label 0 to the function.
5. We read and tried to understand the commit message. If the message did not mention fixing a vulnerability or a safety problem, we assigned the label 0 to the function.
6. We checked whether the function was actually changed to address the vulnerability/safety problem, or whether it was changed for some other purpose. If it was changed for another purpose, we assigned the label 0 to the function.
7. We checked whether the problem was actually a security vulnerability. To simplify, we considered potential denial of service issues, such as "buffer overflow, memory leak, crash, and corruption," as vulnerabilities. If no vulnerability was found, we assigned the label 0 to the function. Otherwise, we assigned the label 1 to the function.
8. If we could not determine the label after 10-15 minutes of effort, we assigned the label 2 to the function.
