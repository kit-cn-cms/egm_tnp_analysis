from libPython.tnpClassUtils import tnpSample

#github branches
#LegacyReReco2016: https://github.com/swagata87/egm_tnp_analysis/tree/Legacy2016_94XIDv2 
#ReReco2017: https://github.com/swagata87/egm_tnp_analysis/tree/tnp_2017datamc_IDV2_10_2_0
#PromptReco2018: https://github.com/swagata87/egm_tnp_analysis/tree/egm_tnp_Prompt2018_102X_10222018_MC102XECALnoiseFix200kRelVal
#UL2017: https://github.com/swagata87/egm_tnp_analysis/blob/UL2017Final/etc/inputs/tnpSampleDef.py

### eos repositories
eosLegacyReReco2016 = '/eos/cms/store/group/phys_egamma/swmukher/egmNtuple_V2ID_2016/'
eosReReco2017 = '/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/'
eosReReco2018 = '/eos/cms/store/group/phys_egamma/swmukher/rereco2018/ECAL_NOISE/'
#eosUL2017 = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017/'
eosUL2017 = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017_MINIAOD_Nm1/'
eosUL2018 = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_MINIAOD_Nm1/'
eosUL2016 = '/eos/cms/store/group/phys_egamma/akapoor/Tag-and-Probe_Tree/UL2016_ntuples/'

customUL = '/eos/cms/store/user/avargash/EGammaSF/2022-03-16/'


ReReco2017 = {


    'DY_madgraph'              : tnpSample('DY_madgraph',
                                       eosReReco2017 + 'DYJetsToLL.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_1j_madgraph'              : tnpSample('DY_1j_madgraph',
                                       eosReReco2017 + 'DY1JetsToLLM50madgraphMLM.root',
                                       isMC = True, nEvts =  -1 ),
#    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
#                                       eosMoriond18 + 'DYJetsToLLM50amcatnloFXFX.root',
#                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnloext'                 : tnpSample('DY_amcatnloext',
                                       eosReReco2017 + 'DYJetsToLLM50amcatnloFXFXext.root',
                                       isMC = True, nEvts =  -1 ),


    'data_Run2017B' : tnpSample('data_Run2017B' , eosReReco2017 + 'RunB.root' , lumi = 4.793 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosReReco2017 + 'RunC.root' , lumi = 9.753),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosReReco2017 + 'RunD.root' , lumi = 4.320 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosReReco2017 + 'RunE.root' , lumi = 8.802),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosReReco2017 + 'RunF.root' , lumi = 13.567),

    }

LegacyReReco2016 = {

    'DY_madgraph' : tnpSample('DY_madgraph', 
                                        eosLegacyReReco2016 + 'TnPTree_DY_M50_madgraphMLM.root',
                                        isMC = True, nEvts =  -1 ),
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', 
                                        eosLegacyReReco2016 + 'TnPTree_DY_M50_amcatnloFXFX.root',
                                        isMC = True, nEvts =  -1 ),

    'data_Run2016Bv2' : tnpSample('data_Run2017Bv2' , eosLegacyReReco2016 + 'TnPTree_2016B_2.root' , lumi = 5.785 ),
    'data_Run2016C' : tnpSample('data_Run2017C' , eosLegacyReReco2016 + 'TnPTree_2016C.root' , lumi = 2.573 ),
    'data_Run2016D' : tnpSample('data_Run2017D' , eosLegacyReReco2016 + 'TnPTree_2016D.root' , lumi = 4.248 ),
    'data_Run2016E' : tnpSample('data_Run2017E' , eosLegacyReReco2016 + 'TnPTree_2016E.root' , lumi = 3.947 ),
    'data_Run2016F' : tnpSample('data_Run2017F' , eosLegacyReReco2016 + 'TnPTree_2016F.root' , lumi = 3.102 ),
    'data_Run2016G' : tnpSample('data_Run2017G' , eosLegacyReReco2016 + 'TnPTree_2016G.root' , lumi = 7.540 ),
    'data_Run2016H' : tnpSample('data_Run2017H' , eosLegacyReReco2016 + 'TnPTree_2016H.root' , lumi = 7.813 ),



}


ReReco2018 = {
    ### MiniAOD TnP for IDs scale 

    'DY_madgraph'              : tnpSample('DY_madgraph',
                                            eosReReco2018 + 'DYJetsToLLmadgraphMLM.root',
                                            isMC = True, nEvts =  -1 ),

    'DY_powheg'              : tnpSample('DY_powheg',
                                            eosReReco2018 + 'DYToEEpowheg.root',
                                            isMC = True, nEvts =  -1 ),
    

    'data_Run2018A' : tnpSample('data_Run2018A' , eosReReco2018 + 'RunA.root' , lumi = 10.723),  
    'data_Run2018B' : tnpSample('data_Run2018B' , eosReReco2018 + 'RunB.root' , lumi = 5.964),
    'data_Run2018C' : tnpSample('data_Run2018C' , eosReReco2018 + 'RunC.root' , lumi = 6.382),
    'data_Run2018D' : tnpSample('data_Run2018D' , eosReReco2018 + 'RunD.root' , lumi = 29.181), 

    }


UL2017 = {
    'DYToLL_NLO' : tnpSample('DYToLL_NLO', customUL + 'UL2017_DYToLL_NLO.root ', isMC = True, nEvts =  -1 ),
    'DYToLL_LO' : tnpSample('DYToLL_LO', customUL + 'UL2017_DYToLL_LO.root', isMC = True, nEvts =  -1 ),
    'data_Run2017B' : tnpSample('data_Run2017B' , customUL + 'UL2017_SERun2017B.root' , lumi = 4.793961427),
    'data_Run2017C' : tnpSample('data_Run2017C' , customUL + 'UL2017_SERun2017C.root' , lumi = 9.631214821 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , customUL + 'UL2017_SERun2017D.root' , lumi = 4.247682053 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , customUL + 'UL2017_SERun2017E.root' , lumi = 9.313642402 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , customUL + 'UL2017_SERun2017F.root' , lumi = 13.510934811),
    }

UL2018 = {
    'DYToLL_NLO'   : tnpSample('DYToLL_NLO', customUL + 'UL2018_DYToLL_NLO.root', isMC = True, nEvts =  -1 ),
    'DYToLL_LO': tnpSample('DYToLL_LO', customUL + 'UL2018_DYToLL_LO.root', isMC = True, nEvts =  -1 ),
    'data_Run2018A' : tnpSample('data_Run2018A' , customUL + 'UL2018_EGRun2018A.root' , lumi = 14.02672485),
    'data_Run2018B' : tnpSample('data_Run2018B' , customUL + 'UL2018_EGRun2018B.root' , lumi = 7.060617355),
    'data_Run2018C' : tnpSample('data_Run2018C' , customUL + 'UL2018_EGRun2018C.root' , lumi = 6.894770971),
    'data_Run2018D' : tnpSample('data_Run2018D' , customUL + 'UL2018_EGRun2018D.root' , lumi = 31.74220577),
    }


UL2016_preVFP = {
    'DYToLL_NLO' : tnpSample('DYToLL_NLO', customUL + 'UL2016preVFP_DYToLL_NLO.root',isMC = True, nEvts =  -1 ),
    'DYToLL_LO'  : tnpSample('DYToLL_LO', customUL + 'UL2016preVFP_DYToLL_LO.root',isMC = True, nEvts =  -1 ),
#    'data_Run2016B' : tnpSample('data_Run2016B' , customUL + 'UL2016_SERun2016B.root' , lumi = 0.030493962),
    'data_Run2016B' : tnpSample('data_Run2016B' , customUL + 'UL2016preVFP_SERun2016BHIPMv2.root' , lumi = 5.879330594),
    'data_Run2016C' : tnpSample('data_Run2016C' , customUL + 'UL2016preVFP_SERun2016CHIPM.root' , lumi = 2.64992914),
    'data_Run2016D' : tnpSample('data_Run2016D' , customUL + 'UL2016preVFP_SERun2016DHIPM.root' , lumi = 4.292865604),
    'data_Run2016E' : tnpSample('data_Run2016E' , customUL + 'UL2016preVFP_SERun2016EHIPM.root' , lumi = 4.185165152),
    'data_Run2016F' : tnpSample('data_Run2016F' , customUL + 'UL2016preVFP_SERun2016FHIPM.root' , lumi = 2.725508364),
    }

UL2016_postVFP = {
    'DYToLL_NLO' : tnpSample('DYToLL_NLO', customUL + 'UL2016postVFP_DYToLL_NLO.root', isMC = True, nEvts =  -1 ),
    'DYToLL_LO' : tnpSample('DYToLL_LO', customUL + 'UL2016postVFP_DYToLL_LO.root', isMC = True, nEvts =  -1 ),
    'data_Run2016F_postVFP' : tnpSample('data_Run2016F_postVFP' , customUL + 'UL2016postVFP_SERun2016F.root' , lumi = 0.414987426),
    'data_Run2016G' : tnpSample('data_Run2016G' , customUL + 'UL2016postVFP_SERun2016G.root' , lumi = 7.634508755),
    'data_Run2016H' : tnpSample('data_Run2016H' , customUL + 'UL2016postVFP_SERun2016H.root' , lumi = 8.802242522),
    }
