# Maintainers

See [Governance](https://github.com/flatcar/Flatcar/blob/main/governance.md) for governance, access, and voting guidelines as well as maintainer responsibilities. Everybody listed in this file is a maintainer as per governance definition. See also [Onboarding](https://github.com/flatcar/Flatcar/blob/main/ONBOARDING.md) for the new maintainer onboarding checklist, [Contributing](https://github.com/flatcar/Flatcar/blob/main/CONTRIBUTING.md) for contribution guidelines, [README](https://github.com/flatcar/Flatcar/blob/main/README.md) for general project information, and [Security](https://github.com/flatcar/Flatcar/blob/main/SECURITY.md) for security policies and reporting.


## Flatcar Maintainers

Official Flatcar project maintainers. All maintainers listed here should also be present in the [CNCF project maintainers list](https://github.com/cncf/foundation/blob/main/project-maintainers.csv).

| Name              | GitHub                                                 |
| ----------------- | ------------------------------------------------------ |
| James Le Cuirot   | [@chewi](https://github.com/chewi)                     |
| Thilo Fromm       | [@t-lo](https://github.com/t-lo)                       |
| Krzesimir Nowak   | [@krnowak](https://github.com/krnowak)                 |
| Sayan Chowdhury   | [@sayanchowdhury](https://github.com/sayanchowdhury)   |
| Gabriel Samfira   | [@gabriel-samfira](https://github.com/gabriel-samfira) |
| Kai Lüke          | [@pothos](https://github.com/pothos)                   |
| Adrian Vladu      | [@ader1990](https://github.com/ader1990)               |
| Daniel Zatovic    | [@danzatt](https://github.com/danzatt)                 |
| Jeremi Piotrowski | [@jepio](https://github.com/jepio)                     |
| Dongsu Park       | [@dongsupark](https://github.com/dongsupark)           |
| Danielle Tal      | [@miao0miao](https://github.com/miao0miao)             |
| Mathieu Tortuyaux | [@tormath1](https://github.com/tormath1)               |
| Ervin Racz        | [@ervcz](https://github.com/ervcz)                     |
| Jan Bronicki      | [@John15321](https://github.com/John15321)             |
| Lexi Nadolski     | [@lexinadolski](https://github.com/lexinadolski)       |
| Robin Schneider   | [@robinschneider](https://github.com/robinschneider)   |

## Flatcar Security Team

The Flatcar Security Task Force.

| Name              | GitHub                                               |
| ----------------- | ---------------------------------------------------- |
| Vincent Batts     | [@vbatts](https://github.com/vbatts)                 |
| Thilo Fromm       | [@t-lo](https://github.com/t-lo)                     |
| Krzesimir Nowak   | [@krnowak](https://github.com/krnowak)               |
| Sayan Chowdhury   | [@sayanchowdhury](https://github.com/sayanchowdhury) |
| Kai Lüke          | [@pothos](https://github.com/pothos)                 |
| Dongsu Park       | [@dongsupark](https://github.com/dongsupark)         |
| Mathieu Tortuyaux | [@tormath1](https://github.com/tormath1)             |

## Maintainer Subgroups

Subgroups are teams of maintainers responsible for specific sets of repositories. They serve as primary reviewers and first responders for changes in their area. These subgroups are enforced via [GitHub teams](https://github.com/orgs/flatcar/teams) and `CODEOWNERS` files in each repository. All groups and subgroups listed in this document are sourced from the [Flatcar GitHub teams page](https://github.com/orgs/flatcar/teams). Repositories not listed below have `@flatcar/flatcar-maintainers` assigned in their `CODEOWNERS`, meaning all maintainers will be requested for review.

| Subgroup                  | Description                                                     | Members                                                                                                                                                                                                                                                                                                            | Repositories                                                                                                                                                                                                                                                           |
| ------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **nebraska-maintainers**  | Reviews Nebraska-related update and Omaha projects for Flatcar. | [@t-lo](https://github.com/t-lo)<br>[@pothos](https://github.com/pothos)<br>[@jepio](https://github.com/jepio)<br>[@miao0miao](https://github.com/miao0miao)<br>[@tormath1](https://github.com/tormath1)<br>[@ervcz](https://github.com/ervcz)                                                                     | [flatcar-maintainer-private](https://github.com/flatcar/flatcar-maintainer-private)<br>[go-omaha](https://github.com/flatcar/go-omaha)<br>[nebraska](https://github.com/flatcar/nebraska)<br>[nebraska-update-agent](https://github.com/flatcar/nebraska-update-agent) |
| **flatcar-integrations**  | Reviews integrations and extension projects for Flatcar.        | [@t-lo](https://github.com/t-lo)<br>[@danzatt](https://github.com/danzatt)<br>[@tormath1](https://github.com/tormath1)<br>[@John15321](https://github.com/John15321)<br>[@pothos](https://github.com/pothos)                                                                                                       | [sysext-bakery](https://github.com/flatcar/sysext-bakery)<br>[flatcar-app-minecraft](https://github.com/flatcar/flatcar-app-minecraft)<br>[flatcar-app-jitsi](https://github.com/flatcar/flatcar-app-jitsi)                                                            |
| **flatcar-communication** | Reviews website, social, and communication content for Flatcar. | [@sayanchowdhury](https://github.com/sayanchowdhury)<br>[@pothos](https://github.com/pothos)<br>[@LexiNadolski](https://github.com/LexiNadolski)<br>[@tormath1](https://github.com/tormath1)<br>[@ervcz](https://github.com/ervcz)<br>[@John15321](https://github.com/John15321)                                   | [flatcar-website](https://github.com/flatcar/flatcar-website)<br>[flatcar-socials](https://github.com/flatcar/flatcar-socials)                                                                                                                                         |
| **flatcar-ci**            | Reviews CI/CD and build automation for Flatcar.                 | [@tormath1](https://github.com/tormath1)<br>[@jepio](https://github.com/jepio)<br>[@sayanchowdhury](https://github.com/sayanchowdhury)<br>[@chewi](https://github.com/chewi)<br>[@pothos](https://github.com/pothos)<br>[@dongsupark](https://github.com/dongsupark)<br>[@John15321](https://github.com/John15321) | [mantle](https://github.com/flatcar/mantle)<br>[jenkins-os](https://github.com/flatcar/jenkins-os)<br>[jenkins-secret](https://github.com/flatcar/jenkins-secret)                                                                                                      |
| **flatcar-infra**         | Reviews infrastructure and secrets management for Flatcar.      | [@tormath1](https://github.com/tormath1)<br>[@John15321](https://github.com/John15321)<br>[@sayanchowdhury](https://github.com/sayanchowdhury)<br>[@jepio](https://github.com/jepio)<br>[@pothos](https://github.com/pothos)<br>[@dongsupark](https://github.com/dongsupark)                                       | [flatcar-linux-build-secrets](https://github.com/flatcar/flatcar-linux-build-secrets)<br>[flatcar-linux-infra-secrets](https://github.com/flatcar/flatcar-linux-infra-secrets)<br>[flatcar-linux-infra](https://github.com/flatcar/flatcar-linux-infra)                |
