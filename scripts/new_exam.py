#!/usr/bin/env python3
import os
import csv
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exam-name', required=True)
    parser.add_argument('--template', required=True)
    parser.add_argument('--students-file', required=True)
    args = parser.parse_args()
    # — Aquí se copiaría el template y se generaría el examen —
    print(f"Exam '{args.exam_name}' created from template '{args.template}'")

if __name__ == '__main__':
    main()

