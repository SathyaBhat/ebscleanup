# ebscleanup
Small, simple serverless function to clean up EBS volumes that are detached. 

I have some ephemeral Folding at Home infrastructure which leaves behind EBS volumes when terminated. I should actually be modifying the Launch Templates to delete the volumes on termiantion, but for now this cleans up any old volumes as well. 


