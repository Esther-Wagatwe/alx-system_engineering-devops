POST-MOTERM/INCIDENT REPORT
Issue summary
Start time: 17/06/24 10:00 AM (EAT); End time: 17/06/24 2:30 PM (EAT).
Impact: The website's product pages were inaccessible, resulting in users being unable to view or purchase products. Approximately 60% of the website's traffic was affected during the outage.
Root cause: The issue was caused by a misconfiguration in the website's content delivery network (CDN) after a software update.
Timeline
10:15 AM - The issue was detected by the website's monitoring system, which triggered an alert for a high volume of 404 errors.
10:30 AM - The incident was escalated to the website operations team, and initial investigations began.
11:00 AM - The team checked the website's server logs and found no apparent issues with the application code or server configurations.
11:45 AM - The CDN provider was contacted, and they confirmed a recent software update had caused a misconfiguration in caching rules.
12:30 PM - The CDN team worked on rolling back the software update and updating the caching rules.
2:00 PM - The CDN team completed the rollback, and the website's 404 errors started to decrease.
2:30 PM - The website was fully operational, and the incident was resolved.
Root Cause and Resolution
The root cause of the 404 Not Found error on the online shopping website was a misconfiguration in the website's CDN after a recent software update. The update introduced a caching rule that incorrectly handled URL paths, resulting in product pages being cached as 404 errors.
To resolve the issue, the CDN team rolled back the software update and updated the caching rules to properly handle URL paths. This corrected the misconfiguration and allowed the website's product pages to be served correctly.
Corrective and Preventative Measures
Improvements and fixes:
Enhance monitoring and alerting systems to detect CDN-related issues more quickly.
Implement a more robust testing process for CDN updates and configuration changes.
Improve communication and collaboration between the website operations team and the CDN provider.
Tasks:
Set up monitoring for CDN error rates and response times.
Implement automated testing for CDN configuration changes before deployment.
Schedule regular meetings with the CDN provider to review upcoming updates and potential impacts.
Document and share incident response procedures for CDN-related issues.
Conduct training for the website operations team on CDN configurations and troubleshooting.
