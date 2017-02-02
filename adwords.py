#!/usr/bin/python
#  https://github.com/googleads/googleads-python-lib#how-do-i-get-started

import logging
import sys
from googleads import adwords

YAML_FILE = "E:\Sophie\Gitkraken\connecteurs\lib\googleads\googleads.yaml"

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def main(client):
  report_downloader = client.GetReportDownloader(version='v201605')

  # Create report definition.
  report = {
      'reportName': 'Last 7 days CRITERIA_PERFORMANCE_REPORT',
      'dateRangeType': 'LAST_7_DAYS',
      'reportType': 'CRITERIA_PERFORMANCE_REPORT',
      'downloadFormat': 'CSV',
      'selector': {
          'fields': ['CampaignId', 'AdGroupId', 'Id', 'CriteriaType',
                     'Criteria', 'FinalUrls', 'Impressions', 'Clicks', 'Cost']
      }
  }

  # You can provide a file object to write the output to. For this demonstration
  # we use sys.stdout to write the report to the screen.
  report_downloader.DownloadReport(
      report, sys.stdout, skip_report_header=False, skip_column_header=False,
      skip_report_summary=False)


if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage(YAML_FILE)
  main(adwords_client)