"""
__title__ = nuke_pickStuffs_tools.py
__author__ = zhangben 
__mtime__ = 2019/3/8 : 18:02
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import os, re, sys
import subprocess
def modifyReadNode(eaRd, targDir, allFrms):
#targDir = copy2Dri
    src_stuff = eaRd['file'].getValue()
    #src_stuff = r'//192.168.80.221/Images/MSS/sc15/sh01/chenshuh/MSS_sc15_sh01_LG_DY_15_L_v301/masterLayer/sc15_camL_L/beauty/sc15_camL_L.%04d.exr'
    #src_stuff2 = r"M:/COMP/MSS/DY/render/sc15/MSS_sc15_sh01_LG_DY_bg_A_v309/masterLayer/sc15_camL_L/beauty/sc15_camL_L.%04d.exr"
    #src_stuff3 = r"M:/COMP/CDFKBS/DY/render/SC05_sh01/CDFKBS_sc05_sh01_lg_DY_lgt_v013_0213_waifa/CDFKBS_sc05_sh01_lg_DY_lgt_v013_0213_waifa/masterLayer/cameraL/ID_shitou/cameraL.ID_shitou.%04d.png"
    #idex = sc_foder_index[-1]
    #rpl_folder = "/".join(dir_splt[:idex+1])
    src_stuff_splpth = os.path.split(src_stuff)
    cmp_stf_path = compile_path(src_stuff)
    new_stuff_path =  "{}{}".format(targDir,cmp_stf_path['makeDir'])
    new_stuff_value = "{}{}/{}".format(targDir,cmp_stf_path['makeDir'],src_stuff_splpth[-1])
    print new_stuff_path
    print new_stuff_value
    stuff_name_spl = []
    stuff_name_spl_tmp = src_stuff_splpth[1].split('.')
    connector = '.'
    if len(stuff_name_spl_tmp) == 3:
        stuff_name_spl.extend(stuff_name_spl_tmp)
    else:
        connector = "_"
        # stuff_name_spl_tmp.append(stuff_name_spl_tmp)
        stuff_name_spl2 = stuff_name_spl_tmp[0].split('_')
        stuff_name_spl.append("_".join(stuff_name_spl2[:-1]))
        stuff_name_spl.append(stuff_name_spl2[-1])
        stuff_name_spl.append(stuff_name_spl_tmp[-1])
    for ea_frm in allFrms:
        #ea_frm = allFrms[2]
        singleStfnm = "{}{}{}.{}".format(stuff_name_spl[0], connector, ea_frm, stuff_name_spl[2])
        print singleStfnm
        src_stfnm_full = os.path.abspath(os.path.join(src_stuff_splpth[0], singleStfnm))
        # src_stfnm_full = os.path.join(r"\\192.168.80.224\Images\CDMSS\sc04\sh01\yanglei1\CDMSS_sc04_sh01_xy_color_CH_v01_fx\masterLayer\CDMSS_sc04_sh01_an_c001_cam4L\crypto_material",singleStfnm)
        new_stf_full = os.path.abspath(os.path.join(new_stuff_path, singleStfnm))
        if not os.path.isfile(src_stfnm_full) :
            #or os.path.isfile(new_stf_full): continue
            print("there is not a stuff named :{} in the source directory\n{}".format(singleStfnm,src_stuff_splpth[0]))
            continue
        #
        targDir = os.path.abspath(new_stuff_path)
        if not os.path.isdir(targDir): os.makedirs(targDir)
        subprocess.Popen(["copy", src_stfnm_full, targDir], shell=True)
        if not os.path.isfile(new_stf_full):
            print("file copped FAILED ------------{}".format(new_stf_full))
        else:
            print("file copyed frome :{}  \nto   \n{}".format(src_stfnm_full,new_stf_full))
    eaRd['file'].setValue(new_stuff_value)
    print("value reset")
    eaRd['on_error'].setValue('checkerboard')
    print("set if missing  of node {}".format(eaRd.name()))
def compile_path(src_stuff):
    #src_stuff = src_stuff_splpth
    src_stuff_splpth = os.path.split(src_stuff)
    stuf_dir = src_stuff_splpth[0]
    dir_splt = stuf_dir.split('/')
    #ea_folder = 'sc15'
    #ea_folder = 'sc15_camL_L'
    #ea_folder = 'SC05_sh01'
    sc_folder_lst = []
    index = 0
    for ea_folder in dir_splt:
        if re.search('^(sc\d+)',ea_folder,re.I):
            print("now check {}".format(ea_folder))
            sc_fd_nm = re.search('^(sc\d+)',ea_folder,re.I).group()
            if not re.search("[^{}]\w+\d+".format(sc_fd_nm),ea_folder,re.I):
                if not re.search("[^{}]+".format(sc_fd_nm),ea_folder,re.I):
                    sc_folder_lst.append(ea_folder)
                    id = dir_splt.index(ea_folder)
                    index = id
                    if re.search('^(sh)\d+',dir_splt[id+1],re.I):
                        sc_folder_lst.extend(dir_splt[(id+1):(id+3)])
                        index = id+3
            else:
                sc_folder_lst.append(ea_folder)
                index = dir_splt.index(ea_folder)

    rpl_dir = "/".join(dir_splt[:index+1])
    mk_dir =  "/".join(dir_splt[index+1:])
    return {'replace_dir':rpl_dir,'makeDir':mk_dir}
def _createPannel():
    panel = nuke.Panel('Test')
    panel.addFilenameSearch('烤到哪', '/tmp')
    panel.addSingleLineInput('frames', '{}-{}'.format(nuke.root().firstFrame(), nuke.root().lastFrame()))
    return panel, panel.show()
def pick_stuff_panel():
    # if __name__ == "__main__":
    (p, ret) = _createPannel()
    # ==get all need frames
    copy2Dri = p.value('烤到哪')
    frms = p.value('frames')
    frm_splt_comma = frms.split(',')
    allFrms = []
    for ea in frm_splt_comma:
        if not re.search('-', ea) and ea not in allFrms:
            allFrms.append(int(ea))
        else:
            frm_rang = nuke.FrameRange(ea)
            for ea_frm in (range(frm_rang.first(), frm_rang.last()+1)):
                if ea_frm not in allFrms: allFrms.append(ea_frm)
    return {'dir':copy2Dri,'frms':allFrms}

def main():
    for eaRd in nuke.selectedNodes('Read'):
        print ("Now start set read node ::{}".format(eaRd.name()))
        ret = pick_stuff_panel()
        ret_path  = ret['dir']
        copy2Dri = re.sub("\\\\",'/',ret_path)
        copy2Dri = re.sub(".$","{}/".format(re.search(".$",copy2Dri).group()),copy2Dri)
        allFrms = ret['frms']
        modifyReadNode(eaRd, copy2Dri, allFrms)


if __name__ == "__main__":
    main()










