import maya.cmds as mc
import maya.mel as mm
def p_arm():
    tarPos=[[-4.2968839335636559, 10.568842766860165, -1.6455076007594422], [-3.222662950172742, 10.568842766860165, -1.6605579961257786], [-1.8440814290103056, 10.568842766860165, -1.5473380763955766], [-0.62256510292105771, 10.568842766860165, -1.0295703555885876], [0.0, 10.568842766860165, -1.0295703555885876], [0.62256510292105771, 10.568842766860165, -1.0295703555885876], [1.8440814290103056, 10.568842766860165, -1.5473380763955766], [3.222662950172742, 10.568842766860165, -1.6605579961257786], [4.2968839335636559, 10.568842766860165, -1.6455076007594422], [-4.2968839335636559, 11.161083130671857, -1.6455076007594422], [-3.222662950172742, 11.161083130671857, -1.6605579961257786], [-1.8440814290103056, 11.161083130671857, -1.5473380763955766], [-0.62256510292105771, 11.161083130671857, -1.0295703555885876], [0.0, 11.161083130671857, -1.0295703555885876], [0.62256510292105771, 11.161083130671857, -1.0295703555885876], [1.8440814290103056, 11.161083130671857, -1.5473380763955766], [3.222662950172742, 11.161083130671857, -1.6605579961257786], [4.2968839335636559, 11.161083130671857, -1.6455076007594422], [-4.2968839335636559, 11.753323494483549, -1.6455076007594422], [-3.222662950172742, 11.753323494483549, -1.6605579961257786], [-1.8440814290103056, 11.753323494483549, -1.5473380763955766], [-0.62256510292105771, 11.753323494483549, -1.0295703555885876], [0.0, 11.753323494483549, -1.0295703555885876], [0.62256510292105771, 11.753323494483549, -1.0295703555885876], [1.8440814290103056, 11.753323494483549, -1.5473380763955766], [3.222662950172742, 11.753323494483549, -1.6605579961257786], [4.2968839335636559, 11.753323494483549, -1.6455076007594422], [-4.2968839335636559, 12.345563858295241, -1.6455076007594422], [-3.222662950172742, 12.345563858295241, -1.6605579961257786], [-1.8440814290103056, 12.345563858295241, -1.5473380763955766], [-0.62256510292105771, 12.345563858295241, -1.0295703555885876], [0.0, 12.345563858295241, -1.0295703555885876], [0.62256510292105771, 12.345563858295241, -1.0295703555885876], [1.8440814290103056, 12.345563858295241, -1.5473380763955766], [3.222662950172742, 12.345563858295241, -1.6605579961257786], [4.2968839335636559, 12.345563858295241, -1.6455076007594422], [-4.2968839335636559, 12.937804222106934, -1.6455076007594422], [-3.222662950172742, 12.937804222106934, -1.6605579961257786], [-1.8440814290103056, 12.937804222106934, -1.5473380763955766], [-0.62256510292105771, 12.937804222106934, -1.0295703555885876], [0.0, 12.937804222106934, -1.0295703555885876], [0.62256510292105771, 12.937804222106934, -1.0295703555885876], [1.8440814290103056, 12.937804222106934, -1.5473380763955766], [3.222662950172742, 12.937804222106934, -1.6605579961257786], [4.2968839335636559, 12.937804222106934, -1.6455076007594422], [-4.2968839335636559, 13.530044585918626, -1.6455076007594422], [-3.222662950172742, 13.530044585918626, -1.6605579961257786], [-1.8440814290103056, 13.530044585918626, -1.5473380763955766], [-0.67880484350261627, 13.530044585918626, -1.2456390110715554], [0.0, 13.530044585918626, -1.2456390110715554], [0.67880484350261627, 13.530044585918626, -1.2456390110715554], [1.8440814290103056, 13.530044585918626, -1.5473380763955766], [3.222662950172742, 13.530044585918626, -1.6605579961257786], [4.2968839335636559, 13.530044585918626, -1.6455076007594422], [-4.2968839335636559, 14.122284949730318, -1.6455076007594422], [-3.222662950172742, 14.115679442800138, -1.6440762041313792], [-1.8826929908513277, 14.190137293775781, -1.5781812163563007], [-0.78314837572661178, 14.222593911359718, -1.4501263490705276], [0.0, 14.122284949730318, -1.4501263490705276], [0.78314837572661178, 14.222593911359718, -1.4501263490705276], [1.8229658411195377, 14.170122702303022, -1.571774343854579], [3.222662950172742, 14.118329148113196, -1.6415420791441948], [4.2968839335636559, 14.122284949730318, -1.6455076007594422], [-4.2968839335636559, 14.71452531354201, -1.6455076007594422], [-3.222662950172742, 14.714525313542012, -1.6445709507021622], [-1.9201030981804288, 14.714525313542012, -1.562106579929784], [-1.0147556755144886, 14.71452531354201, -1.6040777356140627], [0.0, 14.71452531354201, -1.6040777356140627], [1.0147556755144886, 14.71452531354201, -1.6040777356140627], [1.8440814290103056, 14.714525313542012, -1.571774343854579], [3.222662950172742, 14.714525313542012, -1.6415420791441948], [4.2968839335636559, 14.71452531354201, -1.6455076007594422], [-4.2968839335636559, 15.306765677353702, -1.6455076007594422], [-3.222662950172742, 15.311193934751595, -1.644416241448363], [-1.9547952900147409, 15.266756345416255, -1.5781821976322996], [-1.074220983390914, 15.200684448787911, -1.6455076007594422], [0.0, 15.206768005125664, -1.6455076007594422], [1.074220983390914, 15.217412924085423, -1.6455076007594422], [1.8440814290103054, 15.246606788071842, -1.571774343854579], [3.222662950172742, 15.309711663127251, -1.6415420791441948], [4.2968839335636559, 15.306765677353702, -1.6455076007594422], [-4.2968839335636559, 10.568842766860165, -0.66887510712112841], [-3.222662950172742, 10.568842766860165, -0.66887510712112841], [-2.148441966781828, 10.568842766860165, -0.66887510712112841], [-0.62256510292105771, 10.568842766860165, -0.463562692064177], [0.0, 10.568842766860165, -0.463562692064177], [0.62256510292105771, 10.568842766860165, -0.463562692064177], [2.148441966781828, 10.568842766860165, -0.66887510712112841], [3.222662950172742, 10.568842766860165, -0.66887510712112841], [4.2968839335636559, 10.568842766860165, -0.66887510712112841], [-4.2968839335636559, 11.161083130671857, -0.66887510712112841], [-3.222662950172742, 11.161083130671857, -0.66887510712112841], [-2.148441966781828, 11.161083130671857, -0.66887510712112841], [-0.62256510292105771, 11.161083130671857, -0.463562692064177], [0.0, 11.161083130671857, -0.463562692064177], [0.62256510292105771, 11.161083130671857, -0.463562692064177], [2.148441966781828, 11.161083130671857, -0.66887510712112841], [3.222662950172742, 11.161083130671857, -0.66887510712112841], [4.2968839335636559, 11.161083130671857, -0.66887510712112841], [-4.2968839335636559, 11.753323494483549, -0.66887510712112841], [-3.222662950172742, 11.753323494483549, -0.66887510712112841], [-2.148441966781828, 11.753323494483549, -0.66887510712112841], [-0.62256510292105771, 11.753323494483549, -0.463562692064177], [0.0, 11.753323494483549, -0.463562692064177], [0.62256510292105771, 11.753323494483549, -0.463562692064177], [2.148441966781828, 11.753323494483549, -0.66887510712112841], [3.222662950172742, 11.753323494483549, -0.66887510712112841], [4.2968839335636559, 11.753323494483549, -0.66887510712112841], [-4.2968839335636559, 12.345563858295241, -0.66887510712112841], [-3.222662950172742, 12.345563858295241, -0.66887510712112841], [-2.148441966781828, 12.345563858295241, -0.66887510712112841], [-0.62256510292105771, 12.345563858295241, -0.463562692064177], [0.0, 12.345563858295241, -0.463562692064177], [0.62256510292105771, 12.345563858295241, -0.463562692064177], [2.148441966781828, 12.345563858295241, -0.66887510712112841], [3.222662950172742, 12.345563858295241, -0.66887510712112841], [4.2968839335636559, 12.345563858295241, -0.66887510712112841], [-4.2968839335636559, 12.937804222106934, -0.66887510712112841], [-3.222662950172742, 12.937804222106934, -0.66887510712112841], [-2.148441966781828, 12.937804222106934, -0.66887510712112841], [-0.62256510292105771, 12.937804222106934, -0.59749369643249417], [0.0, 12.937804222106934, -0.59749369643249417], [0.62256510292105771, 12.937804222106934, -0.59749369643249417], [2.148441966781828, 12.937804222106934, -0.66887510712112841], [3.222662950172742, 12.937804222106934, -0.66887510712112841], [4.2968839335636559, 12.937804222106934, -0.66887510712112841], [-4.2968839335636559, 13.530044585918626, -0.66887510712112841], [-3.222662950172742, 13.530044585918626, -0.66887510712112841], [-2.148441966781828, 13.530044585918626, -0.66887510712112841], [-0.67880484350261627, 13.530044585918626, -0.66951658159348315], [0.0, 13.530044585918626, -0.66951658159348315], [0.67880484350261627, 13.530044585918626, -0.66951658159348315], [2.148441966781828, 13.530044585918626, -0.66887510712112841], [3.222662950172742, 13.530044585918626, -0.66887510712112841], [4.2968839335636559, 13.530044585918626, -0.66887510712112841], [-4.2968839335636559, 14.122284949730318, -0.66887510712112841], [-3.222662950172742, 14.115679442800138, -0.66887510712112841], [-2.1294492512994654, 14.198049992025867, -0.66887510712112841], [-0.80345665120080911, 14.222593911359718, -0.66887510712112841], [0.0, 14.122284949730318, -0.66887510712112841], [0.80345665120080911, 14.222593911359718, -0.66887510712112841], [2.1323842693716295, 14.170122702303022, -0.66887510712112841], [3.222662950172742, 14.118329148113196, -0.66887510712112841], [4.2968839335636559, 14.122284949730318, -0.66887510712112841], [-4.2968839335636559, 14.71452531354201, -0.66887510712112841], [-3.222662950172742, 14.714525313542012, -0.66887510712112841], [-2.148441966781828, 14.714525313542012, -0.66887510712112841], [-1.074220983390914, 14.71452531354201, -0.66887510712112841], [0.0, 14.71452531354201, -0.66887510712112841], [1.074220983390914, 14.71452531354201, -0.66887510712112841], [2.148441966781828, 14.714525313542012, -0.66887510712112841], [3.222662950172742, 14.714525313542012, -0.66887510712112841], [4.2968839335636559, 14.71452531354201, -0.66887510712112841], [-4.2968839335636559, 15.306765677353702, -0.66887510712112841], [-3.222662950172742, 15.312046967500613, -0.66887510712112841], [-2.1484419667818275, 15.223766790178368, -0.66887510712112841], [-1.074220983390914, 15.200684448787911, -0.66887510712112841], [0.0, 15.206768005125664, -0.66887510712112841], [1.074220983390914, 15.217412924085423, -0.66887510712112841], [2.1484419667818275, 15.246606788071842, -0.66887510712112841], [3.222662950172742, 15.309711663127251, -0.66887510712112841], [4.2968839335636559, 15.306765677353702, -0.66887510712112841], [-4.2968839335636559, 10.568842766860165, 0.30775738651718537], [-3.222662950172742, 10.568842766860165, 0.30775738651718537], [-2.148441966781828, 10.568842766860165, 0.26461724462660996], [-0.62256510292105771, 10.568842766860165, 0.10244497146023401], [0.0, 10.568842766860165, 0.10244497146023401], [0.62256510292105771, 10.568842766860165, 0.10244497146023401], [2.148441966781828, 10.568842766860165, 0.26461724462660996], [3.222662950172742, 10.568842766860165, 0.30775738651718537], [4.2968839335636559, 10.568842766860165, 0.30775738651718537], [-4.2968839335636559, 11.161083130671857, 0.30775738651718537], [-3.222662950172742, 11.161083130671857, 0.30775738651718537], [-2.148441966781828, 11.161083130671857, 0.26461724462660996], [-0.62256510292105771, 11.161083130671857, 0.10244497146023401], [0.0, 11.161083130671857, 0.10244497146023401], [0.62256510292105771, 11.161083130671857, 0.10244497146023401], [2.148441966781828, 11.161083130671857, 0.26461724462660996], [3.222662950172742, 11.161083130671857, 0.30775738651718537], [4.2968839335636559, 11.161083130671857, 0.30775738651718537], [-4.2968839335636559, 11.753323494483549, 0.30775738651718537], [-3.222662950172742, 11.753323494483549, 0.30775738651718537], [-2.148441966781828, 11.753323494483549, 0.26461724462660996], [-0.62256510292105771, 11.753323494483549, 0.10244497146023401], [0.0, 11.753323494483549, 0.10244497146023401], [0.62256510292105771, 11.753323494483549, 0.10244497146023401], [2.148441966781828, 11.753323494483549, 0.26461724462660996], [3.222662950172742, 11.753323494483549, 0.30775738651718537], [4.2968839335636559, 11.753323494483549, 0.30775738651718537], [-4.2968839335636559, 12.345563858295241, 0.30775738651718537], [-3.222662950172742, 12.345563858295241, 0.30775738651718537], [-2.148441966781828, 12.345563858295241, 0.26461724462660996], [-0.62256510292105771, 12.345563858295241, 0.10244497146023401], [0.0, 12.345563858295241, 0.10244497146023401], [0.62256510292105771, 12.345563858295241, 0.10244497146023401], [2.148441966781828, 12.345563858295241, 0.26461724462660996], [3.222662950172742, 12.345563858295241, 0.30775738651718537], [4.2968839335636559, 12.345563858295241, 0.30775738651718537], [-4.2968839335636559, 12.937804222106934, 0.30775738651718537], [-3.222662950172742, 12.937804222106934, 0.30775738651718537], [-2.148441966781828, 12.937804222106934, 0.26461724462660996], [-0.62256510292105771, 12.937804222106934, 0.10244497146023401], [0.0, 12.937804222106934, 0.10244497146023401], [0.62256510292105771, 12.937804222106934, 0.10244497146023401], [2.148441966781828, 12.937804222106934, 0.26461724462660996], [3.222662950172742, 12.937804222106934, 0.30775738651718537], [4.2968839335636559, 12.937804222106934, 0.30775738651718537], [-4.2968839335636559, 13.530044585918626, 0.30775738651718537], [-3.222662950172742, 13.530044585918626, 0.30775738651718537], [-2.148441966781828, 13.530044585918626, 0.26461724462660996], [-0.67880484350261627, 13.530044585918626, 0.17446785662122299], [0.0, 13.530044585918626, 0.17446785662122299], [0.67880484350261627, 13.530044585918626, 0.17446785662122299], [2.148441966781828, 13.530044585918626, 0.26461724462660996], [3.222662950172742, 13.530044585918626, 0.30775738651718537], [4.2968839335636559, 13.530044585918626, 0.30775738651718537], [-4.2968839335636559, 14.122284949730318, 0.30775738651718537], [-3.222662950172742, 14.115679442800138, 0.3012176709965565], [-2.1563908544029897, 14.197095448783511, 0.24377458666253488], [-0.79807781408702616, 14.222593911359718, 0.18458065694325071], [0.0, 14.122284949730318, 0.30775738651718537], [0.75807684605308145, 14.222593911359718, 0.19786825182258888], [2.164950065878906, 14.170122702303022, 0.26024859547819318], [3.222662950172742, 14.118329148113196, 0.29655577711614156], [4.2968839335636559, 14.122284949730318, 0.30775738651718537], [-4.2968839335636559, 14.71452531354201, 0.30775738651718537], [-3.222662950172742, 14.714525313542012, 0.3012176709965565], [-2.148441966781828, 14.714525313542012, 0.23987239346860462], [-1.2584266405667368, 14.71452531354201, 0.21470060935975138], [0.0, 14.71452531354201, 0.30775738651718537], [1.2346348603442125, 14.71452531354201, 0.22798820423908966], [2.148441966781828, 14.714525313542012, 0.26527757124023954], [3.222662950172742, 14.714525313542012, 0.29663426906813611], [4.2968839335636559, 14.71452531354201, 0.30775738651718537], [-4.2968839335636559, 15.306765677353702, 0.30775738651718537], [-3.222662950172742, 15.311193934751595, 0.3012176709965565], [-2.1484419667818275, 15.225978465454201, 0.24377483902775815], [-1.074220983390914, 15.200684448787911, 0.30775738651718537], [0.0, 15.206768005125664, 0.30775738651718537], [1.074220983390914, 15.217412924085423, 0.30775738651718537], [2.1484419667818275, 15.246606788071842, 0.26024831529852327], [3.222662950172742, 15.309711663127251, 0.29660969767446821], [4.2968839335636559, 15.306765677353702, 0.30775738651718537], [-4.2968839335636559, 10.568842766860165, 1.2843898801554992], [-3.222662950172742, 10.568842766860165, 1.2843898801554992], [-2.148441966781828, 10.568842766860165, 1.2843898801554992], [-0.62256510292105771, 10.568842766860165, 0.66845263498464469], [0.0, 10.568842766860165, 0.66845263498464469], [0.62256510292105771, 10.568842766860165, 0.66845263498464469], [2.148441966781828, 10.568842766860165, 1.2843898801554992], [3.222662950172742, 10.568842766860165, 1.2843898801554992], [4.2968839335636559, 10.568842766860165, 1.2843898801554992], [-4.2968839335636559, 11.161083130671857, 1.2843898801554992], [-3.222662950172742, 11.161083130671857, 1.2843898801554992], [-2.148441966781828, 11.161083130671857, 1.2843898801554992], [-0.62256510292105771, 11.161083130671857, 0.66845263498464469], [0.0, 11.161083130671857, 0.66845263498464469], [0.62256510292105771, 11.161083130671857, 0.66845263498464469], [2.148441966781828, 11.161083130671857, 1.2843898801554992], [3.222662950172742, 11.161083130671857, 1.2843898801554992], [4.2968839335636559, 11.161083130671857, 1.2843898801554992], [-4.2968839335636559, 11.753323494483549, 1.2843898801554992], [-3.222662950172742, 11.753323494483549, 1.2843898801554992], [-2.148441966781828, 11.753323494483549, 1.2843898801554992], [-0.62256510292105771, 11.753323494483549, 0.66845263498464469], [0.0, 11.753323494483549, 0.66845263498464469], [0.62256510292105771, 11.753323494483549, 0.66845263498464469], [2.148441966781828, 11.753323494483549, 1.2843898801554992], [3.222662950172742, 11.753323494483549, 1.2843898801554992], [4.2968839335636559, 11.753323494483549, 1.2843898801554992], [-4.2968839335636559, 12.345563858295241, 1.2843898801554992], [-3.222662950172742, 12.345563858295241, 1.2843898801554992], [-2.148441966781828, 12.345563858295241, 1.2843898801554992], [-0.62256510292105771, 12.345563858295241, 0.66845263498464469], [0.0, 12.345563858295241, 0.66845263498464469], [0.62256510292105771, 12.345563858295241, 0.66845263498464469], [2.148441966781828, 12.345563858295241, 1.2843898801554992], [3.222662950172742, 12.345563858295241, 1.2843898801554992], [4.2968839335636559, 12.345563858295241, 1.2843898801554992], [-4.2968839335636559, 12.937804222106934, 1.2843898801554992], [-3.222662950172742, 12.937804222106934, 1.2843898801554992], [-2.148441966781828, 12.937804222106934, 1.2843898801554992], [-0.62256510292105771, 12.937804222106934, 0.66845263498464469], [0.0, 12.937804222106934, 0.66845263498464469], [0.62256510292105771, 12.937804222106934, 0.66845263498464469], [2.148441966781828, 12.937804222106934, 1.2843898801554992], [3.222662950172742, 12.937804222106934, 1.2843898801554992], [4.2968839335636559, 12.937804222106934, 1.2843898801554992], [-4.2968839335636559, 13.530044585918626, 1.2843898801554992], [-3.222662950172742, 13.530044585918626, 1.2843898801554992], [-2.148441966781828, 13.530044585918626, 1.2843898801554992], [-0.67880484350261627, 13.530044585918626, 0.8845212904676123], [0.0, 13.530044585918626, 0.8845212904676123], [0.67880484350261627, 13.530044585918626, 0.8845212904676123], [2.148441966781828, 13.530044585918626, 1.2843898801554992], [3.222662950172742, 13.530044585918626, 1.2843898801554992], [4.2968839335636559, 13.530044585918626, 1.2843898801554992], [-4.2968839335636559, 14.122284949730318, 1.2843898801554992], [-3.222662950172742, 14.122284949730318, 1.2843898801554992], [-2.1496686503322793, 14.137943989393138, 1.2843898801554992], [-0.80345665120080911, 14.222593911359718, 1.1017178716771818], [0.0, 14.122284949730318, 1.1017178716771818], [0.80345665120080911, 14.222593911359718, 1.1017178716771818], [2.1496686503322793, 14.137943989393138, 1.2843898801554992], [3.222662950172742, 14.122284949730318, 1.2843898801554992], [4.2968839335636559, 14.122284949730318, 1.2843898801554992], [-4.2968839335636559, 14.71452531354201, 1.2843898801554992], [-3.222662950172742, 14.71452531354201, 1.2843898801554992], [-2.148441966781828, 14.71452531354201, 1.2843898801554992], [-1.074220983390914, 14.71452531354201, 1.2843898801554992], [0.0, 14.71452531354201, 1.2843898801554992], [1.074220983390914, 14.71452531354201, 1.2843898801554992], [2.148441966781828, 14.71452531354201, 1.2843898801554992], [3.222662950172742, 14.71452531354201, 1.2843898801554992], [4.2968839335636559, 14.71452531354201, 1.2843898801554992], [-4.2968839335636559, 15.306765677353702, 1.2843898801554992], [-3.222662950172742, 15.306765677353702, 1.2843898801554992], [-2.1484419667818275, 15.214850117107837, 1.2843898801554992], [-1.074220983390914, 15.200684448787911, 1.2843898801554992], [0.0, 15.206768005125664, 1.2843898801554992], [1.074220983390914, 15.217412924085423, 1.2843898801554992], [2.1484419667818275, 15.214850117107837, 1.2843898801554992], [3.222662950172742, 15.306765677353702, 1.2843898801554992], [4.2968839335636559, 15.306765677353702, 1.2843898801554992]]
    latticeName=mc.ls('sk_sc*plum*:body_ffd13Lattice')[0]
    i=0
    for z in range(4):
        for y in range(9):
            for x in range(9):
                mc.xform(latticeName+'.pt[%d][%d][%d]'%(x,y,z),ws=1,t=tarPos[i])
                i+=1

