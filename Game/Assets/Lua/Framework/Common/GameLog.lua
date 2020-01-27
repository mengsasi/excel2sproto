require "Framework/Common/TableUtils"

local tdump = table.dump
local tconcat = table.concat
local tpack = table.pack
local type = type

local LogType = {
	LOG = 1,
	WARN = 2,
	ERROR = 3
}

local function gettimestr(content)
	local date = os.date("*t")
	return string.format("%d-%02d-%02d %02d:%02d:%02d\t%s", date.year, date.month, date.day, date.hour, date.min, date.sec, content)
end

GameLog = {}

local function LogTable(level, ...)
	local content
	if select("#", ...) == 1 then
		local one = ...
		if type(one) == "table" then
			content = tdump(one)
		else
			content = tostring(one)
		end
	else
		local packed = tpack(...)
		for i,v in pairs(packed) do
			if not v then
				packed[i] = "nil"
			else
				local t = type(v)
				if t == "table" then
					packed[i] = tdump(v)
				else
					packed[i] = tostring(v)
				end
			end
		end
		content = tconcat(packed, "\t");
    end
    local logtext = gettimestr(content)
    if level == LogType.LOG then 
        Debug.Log(logtext)
    elseif level == LogType.WARN then 
        Debug.LogWarning(logtext)
    elseif level == LogType.ERROR then 
        Debug.LogError(logtext)
    end
end

function GameLog.SkyLog(...)
    LogTable(LogType.LOG, ...)
end

function GameLog.SkyWarn(...)
    LogTable(LogType.WARN, ...)
end

function GameLog.SkyError(...)
    LogTable(LogType.ERROR, ...)
end

return GameLog
