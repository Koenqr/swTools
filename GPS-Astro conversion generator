-- Author: koenqr
-- GitHub: https://github.com/Koenqr
-- Workshop: https://steamcommunity.com/id/koenqr
--This code is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license.

--Script for generating asteral values for a series of points outputted over debug.log

sep=";"
debug.log("#; time; x; y; z; ax; ay; az")

addonName="Asteral2Debug"

xmin,xmax=-5000,220000
ymin,ymax=0,240000
zmin,zmax=-5000,5000
interval=2500

g_savedata = {}

xPos = xmin
yPos = ymin
zPos = zmin

logging=false
perTick=3 --3 logs and calculations per tick

printOut=false

printPos=1


function onCreate(is_world_create)
    if is_world_create then
    -- initialise series
        g_savedata.series={} --x,y,z,ax,ay,az
    end
    server.announce(addonName, "loaded")
end

function log(x,y,z)
    matrix1=matrix.translation(x,y,z)
    asteral = server.getAstroPos(matrix1)
    xo,yo,zo = asteral[13],asteral[14],asteral[15]
    debug.log(x..sep..y..sep..z..sep..xo..sep..yo..sep..zo)
    return {x,y,z,xo,yo,zo}
end


function onCustomCommand(full_message, user_peer_id, is_admin, is_auth, command, arg1)
    if command=="?log" then
        logging = not logging
        server.announce(addonName, "logging: "..tostring(logging))
    end
    if command=="?print" then
        printOut = not printOut and not logging
        if logging then
            server.announce(addonName, "loggingis ongoings, please wait")
        else
            server.announce(addonName, "printOut: "..tostring(printOut))
        end
    end
    if command=="?clear" then
        g_savedata.series={}
        server.announce(addonName, "cleared")
    end
    if command=="?pos" then
        m=server.getPlayerPos(user_peer_id)
        x,y,z=matrix.position(m)
        server.announce(addonName, "x: "..x.." y: "..y.." z: "..z, user_peer_id)
    end
    if command=="?time" then
        --calculate run time of log and print
        logRun=((xmax-xmin)/interval*(ymax-ymin)/interval*(zmax-zmin)/interval)/perTick/60
        printRun=#g_savedata.series/60
        server.announce(addonName, "log run time: "..logRun.." seconds, print run time: "..printRun.." seconds")
    end
end

function onTick()
    if logging then
        for i=1,perTick do
            g_savedata.series[#g_savedata.series+1]=log(xPos,yPos,zPos)
            xPos=xPos+interval
            if xPos>xmax then
                xPos=xmin
                yPos=yPos+interval
                if yPos>ymax then
                    yPos=ymin
                    zPos=zPos+interval
                    if zPos>zmax then
                        server.announce(addonName, "finished")
                        logging=false
                        server.announce(addonName, "logging: "..tostring(logging))
                        break
                    end
                end
            end
        end
    elseif printOut then
        for i=1,perTick do
            if printPos>#g_savedata.series then
                printOut=false
                server.announce(addonName, "finished printing")
                break
            end
            debug.log(g_savedata.series[printPos][1]..sep..g_savedata.series[printPos][2]..sep..g_savedata.series[printPos][3]..sep..g_savedata.series[printPos][4]..sep..g_savedata.series[printPos][5]..sep..g_savedata.series[printPos][6])
            printPos=printPos+1
        end
    end
end
