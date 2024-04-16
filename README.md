# VPP Label Accuracy Analysis

We carried out a label accuracy analysis of 100 function sampled from VulnPatchPairs, that were labelled as 'vulnerable' by the Devign authors. The results are displayed in this repository.

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

## Labelling Process

1. Randomly sample 100 functions from VulnPatchPairs that were labelled as 'vulnerable' by the Devign authors.
2. For each of the functions, do the following:
3. Open the corresponding patch commit on GitHub.
4. Verify, that the function was actually modified in the patch commit. If no, assign the label 0 to the function.
5. Read and try to understand the commit message. Does the message actually talk about fixing a vulnerability or a safety problem? If no, assign the label 0 to the function.
6. Check, whether the function is actually changed to address the vulnerability/safety problem, or if it was changed for some other purpose. If it was changed for some other purpose, assign the label 0 to the function.
7. Check whether the problem is actually a security vulnerability (this was sometimes a bit tricky). If no, assign the label 0 to the function. If yes, assign the label 1 to the function.
8. If the label could not be determined after 10-15 minutes of effort, assign the label 2 to the function.

## Labelling Criteria

We adopted our labeling criteria based on the [supplementary materials](https://sites.google.com/view/devign) provided by the Devign authors, categorizing all potential denial of service issues, such as "buffer overflow, memory leak, crash, and corruption", as vulnerabilities.
