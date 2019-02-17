# Qatar National Library (QNL) Harvesting Documentation

* QNL requires IP's to be whitelisted before harvesting from their OAI-PMH server
* A one-time harvest can be made from an individual machine, but if regular harvesting is required, we need to create a static IP address for this purpose
* There are two separate metadata records for each resource: one in Arabic and one in English; these are contained in the same record element and can be mapped to the same field in the config file
* Images are available through IIIF
* Records have been harvested but there is no obvious way of separating them aside from the <physicalLocation> element, since sets are not used.

