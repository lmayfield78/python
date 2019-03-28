from tests.Test_sps.Test_sps_funnel import SpsFunnelTest
from tests.Test_aa40.aa40_funnel_test import aa40FunnelTest
from tests.Test_aa40Advanced.test_aa40advanced_funnel import Test_aa40Advanced_Funnel
from tests.Test_TestReload.Test_TestReload_Funnel import Test_TestReload
from tests.Test_LeptinShred.Test_LeptinShred_Funnel import LeptinShredFunnel
from tests.Test_sbsp.Test_sbsp_funnel import sbspFunnelTest
from tests.Test_TestMax.Test_TestMax_Funnel import Test_TestMax
from BigBrother.Shops_Pass import Shop_passes


def oneForAll():
    '''
    This will go through all of the passes in one.
    :return:
    '''

    #sps2
    print("========  Starting SPS2 ===========")
    sps = SpsFunnelTest()
    sps.Sps_Pass_Test()

    #aa40
    print("===========  Starting aa40 =============")
    aa40 = aa40FunnelTest()
    aa40.test_aa40_funnel()

    #aa40a
    print("=========== Starting aa40a ==============")
    aa40a = Test_aa40Advanced_Funnel()
    aa40a.Test_aa40Advanced_Pass()

    #testreload
    print("======== Starting test Reload ============")
    testReload = Test_TestReload()
    testReload.TestReload_Funnel()

    #leptin shred
    print("===========  Starting Leptin ============")
    #leptin = LeptinShredFunnel()
    #leptin.leptinShred_funnel_normal_pass()

    #sbsp
    print("=========== Starting SBSP ==============")
    sbsp = sbspFunnelTest()
    sbsp.sbsp_funnel_pass()

    #tmax
    print("========== Starting Tmax ==============")
    tmax = Test_TestMax()
    tmax.Tmax_normal_funnel_pass_test()

    #sixpackabs
    print("========== Starting Shop sixpackabs =============")
    shops = Shop_passes()
    shops.Shop_Abs_Max()
    shops.Shop_Abs_Mobile()

    #seniorityHealth
    print("======= Shop Seniorityhealth ================")

    shops.Shop_Senior_Pass_Max()
    shops.Shop_Senior_Pass_Mobile()


    print("All for one complete.")

    print("All for one pass has finished")

oneForAll()
