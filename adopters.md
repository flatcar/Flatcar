Who is using Flatcar?
====================

The following is a list of adopters who have publicly spoken about their use of Flatcar, or who have added themselves to this list.


Adding yourself as a user
-------------------------

If you are using Flatcar, please consider adding yourself as a user with a quick description of your use case by opening a pull request to this file and adding a section describing your usage of Flatcar. If you are open to others contacting you about your use of Flatcar on Slack or Matrix, include your Slack/Matrix nickname or email as well.
    
    * N: Name of user (company or individual) 
      D: Description 
      L: Link with further information (optional) 
      C: Contacts available for questions (optional)

Example entry:

    * N: Flatcar Example User Inc.
      D: Using Flatcar for running Kubernetes in Azure via Cluster API
      L: https://www.exampleuser.com 
      C: Slack: @slacknick and/or Matrix: @Matrixnick and/or Email: nick [at] exampleuser [dot] com
    

Requirements to be listed
-------------------------

* You must represent the user listed. Do not add entries on behalf of
   other users, unless adding a link to a public announcement / blog post.
* Commercial or production use is not required. A user can be an end user, cloud service provider or consultant as long as it is a permanent deployment and not a trial deployment. A well-done home lab setup can be equally
   interesting as a large-scale commercial deployment.


Users 
-----
 
    * N: Adobe
      D: Adobe runs Flatcar on over 18,000 nodes in our fleet of Kubernetes clusters across multiple cloud providers and private data centers in 22 different regions worldwide.
      C: Mike Tougeron (Slack: @Mike Tougeron) and Tony Gosselin (Slack: @Tony Gosselin).
    
    * N: AloPeyk
      D: We are an on-demand delivery business that every day serve millions of requests on a consistent bare metal infrastructure have this concern to choose a reliable and atomic operations system but none of the common OS couldn't satisfy us for such heavy workloads. Since we migrated our production Kubernetes cluster nothing can break this consistent and solid cluster which is powered by amazing Flatcoar OS.
    
    * N: AT&T 
      L: https://medium.com/cloud-native-the-gathering/certified-kubernetes-administrator-join-our-team-its-a-good-thing-7e27ab34dc88
      D: "We are integrating Flatcar Container Linux, Istio, OPA, Multi-Region, KNative, and so many other technologies and concepts it makes the mind hurt a bit."
      
    * N: Cloud house
      D: Flatcar OS has been useful for us for our on-premise solution to our customers 

    * N: Digital Science 
      L: https://digital-science.com
      D: We're running Flatcar on all our self-hosted Kubernetes clusters on AWS, used for all data processing behind Dimensions (https://dimensions.ai). We choose Flatcar for security and simplicity.
      C: soren [at] uberresearch.com

    * N: Equinix Metal
      L: https://kinvolk.io/blog/2021/02/case-study-equinix-metal-builds-on-flatcar/
      D: Equinix uses Flatcar as the OS for its bare metal cloud control plane, which runs in Kubernetes
      
    * N: Finleap Connect
      D: Finleap Connect - At finleap connect we serve over a million financial transactions per day. As a regulated company using a pure cloud-native stack based on Kubernetes, using Flatcar as our foundational building block for reliable, secure and immutable nodes across the public clouds and on bare-metal deployments was a day one decision we never regretted. Today Flatcar serves all of our 12 production clusters with over 300 nodes on public clouds in 3 countries and on our bare-metal private-cloud setup.
    
    * N: Giant Swarm 
      L: https://www.giantswarm.io/blog/time-to-catch-a-new-train-flatcar-linux
      D: Giant Swarm uses Flatcar within their Kubernetes Distribution. Flatcar is used on all providers (Azure, AWS, Google, OpenStack and Vmware). Giant Swarm manages 100s of clusters with 1000s of nodes running on Flatcar across the planet.

    * N: Planetary Quantum GmbH
       L: https://www.planetary-quantum.com/
       D: Planetary Quantum is a berlin-based provider of Docker-hosting and application hosting. Our sister company Planetary Networks colocates their private cloud in two (fiber-)interconnected datacenters in Berlin and Quantum offers container-based solutions (Docker Swarm and a custom tailored application hosting) on top of Flatcar Linux. Flatcar Linux is a great choice for us because it's a modern Linux, well-suited for Docker and Kubernetes due to recent versions of Kernel, SystemD, immutable root and a well-tested userland. Simple and straight-forward updates of the OS make running Flatcar a no-brainer for us. We currently operate over 50 clusters for our customers in our private cloud — all based on Flatcar Linux.
    
    * N: Intersys AG 

    * N: Spinoco Czech Republic, a.s.
      D: Using Flatcar on Bare Metal to run Kubernetes for Spinoco SaaS
      L: www.spinoco.com
      C: pavel.chlupacek@spinoco.com 
   
   
    * N: Skilld.cloud
      L: https://www.skilld.cloud
      D: Flatcar choice was a no-brainer for Skilld: Flatcar is a perfect fit for running Kubernetes workloads. On premise as well as on public clouds. We rely on Flatcar to power up our cutting-edge NRT data-driven ops platforms. A key asset for building distributed & asset management based businesses such as our Community-as-a-service IT platform, or our customers Train fleet's or smart grid's ones.

    * N: Memzo 
      D: Kinvolk was a valuable source of knowledge when troubleshooting installation issues with our platform vendor. They were able to join us and the vendor on a call and sort out the issues quickly.The use of the Flatcar Update Server gave us confidence about what software/OS versions were running in each of our environments. This allowed us to better test upgrades before promoting the change to production environments.

    * N: Mettle
      L https://swade1987.medium.com/upgrading-to-flatcar-linux-746751e89ab4

    * N: STACKIT
      D: Flatcar is used in our Kubernetes as a Service (KaaS) offering called SKE 
      L: https://www.stackit.de/de/produkt/stackit-kubernetes-engine/
      C: [info@stackit.de](mailto:info@stackit.de)

    * N: The @ Company 
      L: https://twitter.com/cpswan/status/1534481517887512577?s=20&t=ODnO_TPa4nhC62KNAB9Stw
      C: Chris Swan https://twitter.com/cpswan/

    * N: Wipro
      D: Wipro Business Solutions uses Flatcar Linux to power their hybrid/multi-cloud PostgreSQL containerized DBaaS platform. Each provisioned database is running on a dedicated lightweight stack with Flatcar Linux as the foundational OS running on each database VM. In addition the DBaaS API itself and all supporting machines use Flatcar Linux as well. Flatcar Linux has proven to be a well-supported rock solid OS with minimal attack surface, built in update mechanism and integrated docker daemon. Ignition brings in an early boot provisioning utility that perfectly adds to the full automation approach of the PostgreSQL DBaaS platform. We use it at scale on-prem with OpenStack cloud but also with public clouds like Google and Tencent
      
    * N: 1&1 Mail & Media (GMX, WEB.DE, mail.com)
      D: 1&1 Mail & Media is happily using FlatCar as the underlying OS in their large on-premise bare-metal Kubernetes installation, hosting the majority of services for their >40M users
      C: stephan.fudeus [at] 1und1 [dot] de

    * N: Genesis Cloud
      D: Genesis Cloud is using Flatcar Linux as the base for its public cloud offering for instances with GPUs and other accelerators
      L: https://genesiscloud.com/
      C: Slack: @Philipp Riederer / @Lukas Stockner
