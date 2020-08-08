Summary: We created an end to end (e2e) CI/CD pipeline with a new domain, a python flask app deployed to AWS Elastic Beanstalk service.

Reference for AWS hosting: You can check July 15 video.

1. Have to find a domain name in one of the domain name providers:
    - https://www.freenom.com/ (Free)
    - SquareSpace (Free)
    - https://www.pythonanywhere.com/ (Free)
    - Go Daddy
    - domain.com
    - AWS
    - NameCheap
    - Namesilo
    - Wix
    - Shopify
    - Hostgator
    - Shopify (Ecomm provider)
    - Digital Ocean
    - Enom
    - WebNames
    - Google Cloud
    - Azure
    - Siteground

    :: Allow you to register a domain name (site) and some offer hosting, website builder, DNS management, payment management
    :: Don't spend too much money if you are buying. It's mostly for practice.

2. Find a hosting provider
    - AWS
    - Netlify (free)
    - Google Cloud
    - Azure (Microsoft)
    - Shopify (Ecomm hosting)
    - Heroku (PaaS ?)
    - SquareSpace (free)
    - HostBuddy (Really good price for Windows hosting) .Net (C#, VB.NET) - SQL Server
    - https://www.alibabacloud.com/

    :: Create an account, find their tool to generate the NS entries
    :: The NS entries are the ones you will use to route your domain.

3. Configure the NS (Name Server)
    - AWS - Services / Route 53
    - Freenom  - Client Area / Management tools / NameServers
    - GoDaddy - Domains / NameServers

4. Host my application
    - Python Flask app using AWS (https://github.com/emersonmellado/mydevopsbc.com)
        - You have to create your own github repository
        - You create your own python flask app (https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)

        :: On July 15 video I used a simple index.html page as a testing step hosted on AWS S3. You don't necessarely need to do it every domain you host. 
    - Simple portolio based on a downloaded template from html5up.net
        Step 1: Choose a template, 
        Step 2: Change it however you like
        Step 3: Drag and drop to Netlify deploy
        - To change your site, you just redo step 2 and 3

        :: Kind of a strech, but you can install netlify cli (Command Line Interface sometimes is just client) and run your deployments from your terminal, like "eb deploy"
        :: https://docs.netlify.com/cli/get-started/

5. Create the automation link
    - On July 15 video (the python flask app) I used a local Jenkins instance to connect github to AWS EB to automate the deployment

    - On today's example (Netlify) You just need a github repository.
        - This is true for static (simple sites only)
        - More complex sites will require a few more steps (nodejs, nuxt, next.js, React)
        - Let's create mydevopsbc.ml repo :)
        - On Netlify we used the "Link to git" on Deploys / Deploy settings / Build & Deploy / Continuos Deployment 
    
